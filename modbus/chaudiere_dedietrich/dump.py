#!/usr/bin/python

from pymodbus.client.sync import ModbusSerialClient
import pprint
import time
import logging
pp = pprint.PrettyPrinter(indent=4)

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

client = ModbusSerialClient(method='rtu', port='/dev/ttyVMC1', baudrate=9600, bytesize=8, stopbits=1, parity='N', timeout = 0.5)
client.connect()

for i in range (1, 10):
	print i
	client.connect()
	result = client.read_input_registers(address=7, count=1, unit=0xA)
	if result is not None:
		print "temperature exterieur (0.1C) : ",result.registers[0]
	result = client.read_input_registers(address=75, count=1, unit=0xA)
	if result is not None:
		print "temperature chaudiere (0.1C) : ",result.registers[0]
	client.close()
