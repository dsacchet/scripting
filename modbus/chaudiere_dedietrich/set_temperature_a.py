#!/usr/bin/python

import minimalmodbus
import sys
import time

mapping={
  'jour': {
    'address': 14,
    'minimum': 5.0,
    'maximum': 30.0
  },
  'nuit': {
    'address': 15,
    'minimum': 5.0,
    'maximum': 30.0
  },
  'antigel': {
    'address': 16,
    'minimum': 0.5,
    'maximum': 20.0
  }
}

minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL=True
instrument = minimalmodbus.Instrument('/dev/ttyBOILER1',0xA,mode='rtu')
instrument.serial.baudrate = 9600
instrument.serial.bytesize = 8
instrument.serial.parity = 'N'
instrument.serial.stopbits = 1
instrument.serial.timeout = 1

def usage(message = ''):
  print "Usage : ",sys.argv[0]," <jour|nuit|antigel> <temperature>"
  if not message == '':
    print message

def read_temperature(plage):
  global mapping
  while True:
    try:
      result = instrument.read_register(mapping[plage]['address'],1)
    except ValueError, IOError:
      time.sleep(1)
      continue
    break
  return result

def write_temperature(plage,value):
  global mapping
  while True:
    try:
      instrument.write_register(mapping[plage]['address'],value,1)
    except ValueError, IOError:
      time.sleep(1)
      continue
    break
  return True

if len(sys.argv) == 3:
  plage=sys.argv[1]
  if not plage in mapping:
    usage()
    exit(1)
  newvalue=float(sys.argv[2])
  if newvalue < mapping[plage]['minimum'] or newvalue > mapping[plage]['maximum']:
    usage("Temperature pour %s doit etre comprise entre %0.2f et %0.2f"%(plage,mapping[plage]['minimum'],mapping[plage]['maximum']))
    exit(1)
  print "Requested setting : ",newvalue
  currentvalue = read_temperature(plage)
  print "Current setting : ",currentvalue
  if newvalue != currentvalue:
    write_temperature(plage,newvalue)
    result = read_temperature(plage)
    print "New setting : ",result
  else:
    print "Same value, nothing to do"
else:
  usage()
  exit(1)

exit(0)
