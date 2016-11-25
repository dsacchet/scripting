#!/usr/bin/python

from pymodbus.client.sync import ModbusSerialClient
import sys

value=['low','boost','bypass']

client = ModbusSerialClient(method='rtu', port='/dev/ttyUSB0', baudrate=19200, bytesize=8, stopbits=1, parity="E")
client.connect()
result=client.read_holding_registers(address=15,count=1,unit=1)
print "Current setting : ",value[result.registers[0]]
