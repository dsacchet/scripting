#!/usr/bin/python

import minimalmodbus
import sys

value=['off','on']

instrument = minimalmodbus.Instrument('/dev/ttyVMC1',0)
instrument.serial.baudrate = 19200
instrument.serial.bytesize = 8
instrument.serial.parity = 'E'
instrument.serial.stopbits = 1

if len(sys.argv) == 2:
  newvalue=int(sys.argv[1])
  result = instrument.read_bit(9,1)
  print "Current setting : ",value[result]
  if newvalue != result:
    print "Change setting to : ",value[newvalue]
    instrument.write_bit(9,newvalue)
    result = instrument.read_bit(9,1)
    print "New setting : ",value[result]
  else:
    print "Same value, nothing to do"
else:
  print "Usage : ",sys.argv[0]," <0|1>"
