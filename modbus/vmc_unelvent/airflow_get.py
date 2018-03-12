#!/usr/bin/python

import minimalmodbus
import sys

value=['low','boost','bypass']

instrument = minimalmodbus.Instrument('/dev/ttyVMC1',0)
instrument.serial.baudrate = 19200
instrument.serial.bytesize = 8
instrument.serial.parity = 'E'
instrument.serial.stopbits = 1

result = instrument.read_register(15,0,3,False)
print "Current setting : ",value[result]
