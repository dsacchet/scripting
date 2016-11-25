#!/usr/bin/python

from pymodbus.client.sync import ModbusSerialClient
import sys

value=['low','boost','bypass']

if len(sys.argv) == 2:
  newvalue=int(sys.argv[1])
  client = ModbusSerialClient(method='rtu', port='/dev/ttyUSB0', baudrate=19200, bytesize=8, stopbits=1, parity="E")
  client.connect()
  result=client.read_holding_registers(address=15,count=1,unit=1)
  print "Current setting : ",value[result.registers[0]]
  if newvalue != result.registers[0]:
    print "Change setting to : ",value[newvalue]
    client.write_register(address=15,value=newvalue,unit=1)
    result=client.read_holding_registers(address=15,count=1,unit=1)
    print "New setting : ",value[result.registers[0]]
  else:
    print "Same value, nothing to do"
else:
  print "Usage : ",sys.argv[0]," <0|1|2>"
