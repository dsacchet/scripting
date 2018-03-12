#!/usr/bin/python

import minimalmodbus
import sys

instrument = minimalmodbus.Instrument('/dev/ttyVMC1',0)
instrument.serial.baudrate = 19200
instrument.serial.bytesize = 8
instrument.serial.parity = 'E'
instrument.serial.stopbits = 1

if len(sys.argv) == 3:
  register=int(sys.argv[1])
  newvalue=int(sys.argv[2])
  result = instrument.read_register(register,0,3,False)
  print "Current setting : ",result
  if newvalue != result:
    print "Change setting to : ",newvalue
    instrument.write_register(register,newvalue,)
    result = instrument.read_register(register,0,3,False)
    print "New setting : ",result
  else:
    print "Same value, nothing to do"
else:
  print "Usage : ",sys.argv[0]," <register> <value>"
