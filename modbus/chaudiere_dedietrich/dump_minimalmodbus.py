#!/usr/bin/python

import minimalmodbus

instrument = minimalmodbus.Instrument('/dev/ttyUSB1',0xA,mode='rtu')
instrument.serial.baudrate = 9600
instrument.serial.bytesize = 8
instrument.serial.parity = 'N'
instrument.serial.stopbits = 1
instrument.serial.timeout = 1

n=1
while n != 801:
	try:
		values = instrument.read_registers(n,50)
	except IOError:
		print "Failed IOError"
	except ValueError:
		print "Failed ValueError"
	else:
		for value in values:
			print "%d : %d" % (n,value)
			n=n+1
