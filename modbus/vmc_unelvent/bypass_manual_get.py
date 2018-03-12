#!/usr/bin/python

import minimalmodbus
import sys

value=['off','on']

instrument = minimalmodbus.Instrument('/dev/ttyVMC1',0)
instrument.serial.baudrate = 19200
instrument.serial.bytesize = 8
instrument.serial.parity = 'E'
instrument.serial.stopbits = 1

result = instrument.read_bit(9,1)
print "Current setting : ",value[result]
