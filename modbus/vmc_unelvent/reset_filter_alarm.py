#!/usr/bin/python

from pymodbus.client.sync import ModbusSerialClient
import sys

client = ModbusSerialClient(method='rtu', port='/dev/ttyUSB0', baudrate=19200, bytesize=8, stopbits=1, parity="E")
client.connect()
result=client.read_input_registers(address=36,count=1,unit=1)
print "Current filter alarm : ",result.registers[0]
client.write_coil(address=12,value=1,unit=1)
result=client.read_input_registers(address=36,count=1,unit=1)
print "New filter alarm : ",result.registers[0]
