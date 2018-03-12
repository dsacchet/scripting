#!/usr/bin/python

import minimalmodbus
import sys

instrument = minimalmodbus.Instrument('/dev/ttyVMC1',0)
instrument.serial.baudrate = 19200
instrument.serial.bytesize = 8
instrument.serial.parity = 'E'
instrument.serial.stopbits = 1

if len(sys.argv) == 2:
  register=int(sys.argv[1])
  result = instrument.read_register(register,0,4,False)
  print "Current setting : ",result
else:
  print "Usage : ",sys.argv[0]," <register>"
