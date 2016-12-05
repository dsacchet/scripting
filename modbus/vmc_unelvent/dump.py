#!/usr/bin/python

from pymodbus.client.sync import ModbusSerialClient
import pprint

pp = pprint.PrettyPrinter(indent=4)

client = ModbusSerialClient(method='rtu', port='/dev/ttyUSB0', baudrate=19200, bytesize=8, stopbits=1, parity="E")
client.connect()

#import logging
#logging.basicConfig()
#log = logging.getLogger()
#log.setLevel(logging.DEBUG)

def convert_bit_to_string(bit,false_value,true_value):
  if bit:
    return true_value
  else:
    return false_value

result = client.read_discrete_inputs(address=0x00, count=15, unit=0x01)
print "===================================================="
print "DISCRETES INPUT"
print "===================================================="
print "[00] ** UNDOCUMENTED / UNSED ** ................ : ",convert_bit_to_string(result.bits[0],"False","True")
print "[01] version ................................... : ",convert_bit_to_string(result.bits[1],"STANDARD+ABSENCE","ALLEMAGNE+STANDBY")
print "[02] free contact .............................. : ",convert_bit_to_string(result.bits[2],"NO","NC")
print "[03] ** UNDOCUMENTED / UNSED ** ................ : ",convert_bit_to_string(result.bits[3],"False","True")
print "[04] ** UNDOCUMENTED / UNSED ** ................ : ",convert_bit_to_string(result.bits[4],"False","True")
print "[05] defroost mode ............................. : ",convert_bit_to_string(result.bits[5],"desactivated","actived")
print "[06] extract motor state ....................... : ",convert_bit_to_string(result.bits[6],"ok","error")
print "[07] input motor state ......................... : ",convert_bit_to_string(result.bits[7],"ok","error")
print "[08] ** UNDOCUMENTED / UNSED ** ................ : ",convert_bit_to_string(result.bits[8],"False","True")
print "[09] ** UNDOCUMENTED / UNSED ** ................ : ",convert_bit_to_string(result.bits[9],"False","True")
print "[10] inside temperature sensor state (tint) .... : ",convert_bit_to_string(result.bits[10],"ok","error")
print "[11] outside temperature sensor state (tout) ... : ",convert_bit_to_string(result.bits[11],"ok","error")
print "[12] extract temperature sensor state (text) ... : ",convert_bit_to_string(result.bits[12],"ok","error")
print "[13] input temperature sensor state (tinp) ..... : ",convert_bit_to_string(result.bits[13],"ok","error")
print "[14] alarm filters state ....................... : ",convert_bit_to_string(result.bits[14],"off","on")

result = client.read_coils(address=0x00, count=14, unit=0x01)
print "===================================================="
print "COILS"
print "===================================================="
print "[00] ** UNDOCUMENTED / UNSED ** ................ : ",convert_bit_to_string(result.bits[0],"False","True")
print "[01] ** UNDOCUMENTED / UNSED ** ................ : ",convert_bit_to_string(result.bits[1],"False","True")
print "[02] pre heating battery ....................... : ",convert_bit_to_string(result.bits[2],"not installed","installed")
print "[03] post heating battery ...................... : ",convert_bit_to_string(result.bits[3],"not installed","installed")
print "[04] sense of switch ........................... : ",convert_bit_to_string(result.bits[4],"no","nc")
print "[05] ** UNDOCUMENTED / UNSED ** ................ : ",convert_bit_to_string(result.bits[5],"False","True")
print "[06] selection of version ...................... : ",convert_bit_to_string(result.bits[6],"STANDBY+ABSENCE","ALLEMAGNE+STANDBY")
print "[07] activation mode stanby absence ............ : ",convert_bit_to_string(result.bits[7],"STANBY/ABSENCE ON","STANDBY/ABSENCE OFF")
print "[08] bypass auto control ....................... : ",convert_bit_to_string(result.bits[8],"actived","desactivated")
print "[09] manual bypass ............................. : ",convert_bit_to_string(result.bits[9],"desactivated","activated")
print "[10] ** UNDOCUMENTED / UNSED ** ................ : ",convert_bit_to_string(result.bits[10],"False","True")
print "[11] ** UNDOCUMENTED / UNSED ** ................ : ",convert_bit_to_string(result.bits[11],"False","True")
print "[12] reset filter alarm ........................ : ",convert_bit_to_string(result.bits[12],"actived","error reset")
print "[13] reset factory parameters .................. : ",convert_bit_to_string(result.bits[13],"actived","error")

result = client.read_input_registers(address=0x00, count=41, unit=0x01)

if result.registers[9] == 0:
  type_of_heat_recovery = "D2EC: DOMEO 210 FL"
elif result.registers[9] == 1:
  type_of_heat_recovery = "D2HU: DOMEO 210 + HYGRO SENSOR"
elif result.registers[9] == 2:
  type_of_heat_recovery = "D2FL: DOMEO 210 CONSTANT AIRFLOW FL"
elif result.registers[9] == 3:
  type_of_heat_recovery = "D2RF: DOMEO 210 CONSTANT AIRFLOW RADIO"
elif result.registers[9] == 4:
  type_of_heat_recovery = "DHY: DOMEO HYGRO"
elif result.registers[9] == 5:
  type_of_heat_recovery = "F2FL: FLEXEO 210 FL"
elif result.registers[9] == 6:
  type_of_heat_recovery = "F3FL: FLEXEO 325 FL"
elif result.registers[9] == 7:
  type_of_heat_recovery = "F2RF: FLEXEO 210 CONSTANT AIRFLOW RADIO"
elif result.registers[9] == 8:
  type_of_heat_recovery = "F3RF: FLEXEO 325 CONSTANT AIRFLOW RADIO"
elif result.registers[9] == 9:
  type_of_heat_recovery = "C3Q: CAD HE MINI/IDEO 300 CONSTANT AIRFLOW"
elif result.registers[9] == 10:
  type_of_heat_recovery = "C4Q: CAD HE MINI/IDEO 450 CONSTANT AIRFLOW"
elif result.registers[9] == 11:
  type_of_heat_recovery = "C3P: CAD HE MINI/IDEO 300 CONSTANT PRESSURE"
elif result.registers[9] == 12:
  type_of_heat_recovery = "C4P: CAD HE MINI/IDEO 450 CONSTANT PRESSURE"
elif result.registers[9] == 13:
  type_of_heat_recovery = "C3LC: CAD HE MINI/IDEO 300 CONSTANT SPEED"
elif result.registers[9] == 14:
  type_of_heat_recovery = "C4LC: CAD HE MINI/IDEO 450 CONSTANT SPEED"
else:
  type_of_heat_recovery = "** UNDOCUMENTED VALUE **"

if result.registers[10] == 0:
  type_of_control = "CONSTANT PRESSURE"
elif result.registers[10] == 1:
  type_of_control = "CONSTANT AIRFLOW"
elif result.registers[10] == 2:
  type_of_control = "CONSTANT SPEED"
elif result.registers[10] == 3:
  type_of_control = "PROPORTIONNAL BY HUMIDITY"
elif result.registers[10] == 4:
  type_of_control = "PROPORTIONNAL BY 0-10V"
elif result.registers[10] == 5:
  type_of_control = "SWITCH (ON/OFF)"
else:
  type_of_control = "** UNDOCUMENTED VALUE **"

tint = result.registers[21]/10.0
tout = result.registers[22]/10.0
text = result.registers[23]/10.0
timp = result.registers[24]/10.0

if result.registers[25] == 0:
  state_of_bypass = "desactivated"
elif result.registers[25] == 1:
  state_of_bypass = "activated"
elif result.registers[25] == 2:
  state_of_bypass = "error"
else:
  state_of_bypass = "** UNDOCUMENTED VALUE **"

if result.registers[26] == 0:
  state_of_preheating = "off"
elif result.registers[26] == 1:
  state_of_preheating = "on"
elif result.registers[26] == 2:
  state_of_preheating = "error"
else:
  state_of_preheating = "** UNDOCUMENTED VALUE **"

if result.registers[27] == 0:
  state_of_postheating = "off"
elif result.registers[27] == 1:
  state_of_postheating = "on"
elif result.registers[27] == 2:
  state_of_postheating = "error"
else:
  state_of_postheating = "** UNDOCUMENTED VALUE **"

print "===================================================="
print "INPUT REGISTER"
print "===================================================="
print "[00] ** UNDOCUMENTED / UNSED ** ................ : ",result.registers[0]
print "[01] ** UNDOCUMENTED / UNSED ** ................ : ",result.registers[1]
print "[02] ** UNDOCUMENTED / UNSED ** ................ : ",result.registers[2]
print "[03] ** UNDOCUMENTED / UNSED ** ................ : ",result.registers[3]
print "[04] ** UNDOCUMENTED / UNSED ** ................ : ",result.registers[4]
print "[05] ** UNDOCUMENTED / UNSED ** ................ : ",result.registers[5]
print "[06] software version main electronic .......... : ",result.registers[6]
print "[07] software version remote control ........... : ",result.registers[7]
print "[08] software version programmation unit ....... : ",result.registers[8]
print "[09] type of heat recovery ..................... : ",result.registers[9]," <=> ",type_of_heat_recovery
print "[10] type of control ........................... : ",result.registers[10]," <=> ",type_of_control
print "[11] ** UNDOCUMENTED / UNSED ** ................ : ",result.registers[11]
print "[12] dephasage des debits ...................... : ",result.registers[12],"%"
print "[13] low airflow ............................... : ",result.registers[13],"?? UNIT ??"
print "[14] temporized boost .......................... : ",result.registers[14],"?? UNIT ??"
print "[15] free cooling .............................. : ",result.registers[15],"?? UNIT ??"
print "[16] current airflow ........................... : ",result.registers[16],"V"
print "[17] power 0-10v ............................... : ",result.registers[17],"mV"
print "[18] ** UNDOCUMENTED / UNSED ** ................ : ",result.registers[18]
print "[19] extract motor speed ....................... : ",result.registers[19],"Tr/mn"
print "[20] input motor speed ......................... : ",result.registers[20],"Tr/mn"
print "[21] temperature tint .......................... : ",tint,"oC (original value : ",result.registers[21],")"
print "[22] temperature tout .......................... : ",tout,"oC (original value : ",result.registers[22],")"
print "[23] temperature text .......................... : ",text,"oC (original value : ",result.registers[23],")"
print "[24] temperature timp .......................... : ",timp,"oC (original value : ",result.registers[24],")"
print "[25] state of bypass ........................... : ",result.registers[25]," <=> ",state_of_bypass
print "[26] state of pre heating battery .............. : ",result.registers[26]," <=> ",state_of_preheating
print "[27] state of post heating battery ............. : ",result.registers[27]," <=> ",state_of_postheating
print "[28] ** UNDOCUMENTED / UNSED ** ................ : ",result.registers[28]
print "[29] ** UNDOCUMENTED / UNSED ** ................ : ",result.registers[29]
print "[30] ** UNDOCUMENTED / UNSED ** ................ : ",result.registers[30]
print "[31] ** UNDOCUMENTED / UNSED ** ................ : ",result.registers[31]
print "[32] ** UNDOCUMENTED / UNSED ** ................ : ",result.registers[32]
print "[33] ** UNDOCUMENTED / UNSED ** ................ : ",result.registers[33]
print "[34] ** UNDOCUMENTED / UNSED ** ................ : ",result.registers[34]
print "[35] ** UNDOCUMENTED / UNSED ** ................ : ",result.registers[35]
print "[36] filter alarm .............................. : ",result.registers[36],"months"
print "[37] temperature tin pre heating battery ....... : ",result.registers[37]
print "[38] temperature tout pre heating battery ...... : ",result.registers[38]
print "[39] temperature tin post heating battery ...... : ",result.registers[39]
print "[40] temperature tout post heating battery ..... : ",result.registers[40]

result = client.read_holding_registers(address=0x00, count=34, unit=0x01)
print "===================================================="
print "HOLDING REGISTERS"
print "===================================================="

if result.registers[1]==5:
  baudrate = "4800"
elif result.registers[1]==6:
  baudrate = "9600"
elif result.registers[1]==8:
  baudrate = "19200"
elif result.registers[1]==10:
  baudrate = "38400"
else:
  baudrate = "** UNDOCUMENTED VALUE **"

if result.registers[2] == 0:
  parity = "none"
elif result.registers[2] == 1:
  parity = "odd"
elif result.registers[2] == 2:
  parity = "even"
else:
  parity = "** UNDOCUMENTED VALUE **"

if result.registers[15] == 0:
  airflow_set = "low"
elif result.registers[15] == 1:
  airflow_set = "boost"
elif result.registers[15] == 2:
  airflow_set = "bypass"
else:
  airflow_set = "** UNDOCUMENTED VALUE **"

print "[00] modbus network nude ....................... : ",result.registers[0]," (default: 1)"
print "[01] modbus network baudrate ................... : ",result.registers[1]," <=> ",baudrate," (default: 19200)"
print "[02] modbus network parity ..................... : ",result.registers[2]," <=> ",parity," (default: even)"
print "[03] ** UNDOCUMENTED / UNSED ** ................ : ",result.registers[3]
print "[04] ** UNDOCUMENTED / UNSED ** ................ : ",result.registers[4]
print "[05] ** UNDOCUMENTED / UNSED ** ................ : ",result.registers[5]
print "[06] ** UNDOCUMENTED / UNSED ** ................ : ",result.registers[6]
print "[07] ** UNDOCUMENTED / UNSED ** ................ : ",result.registers[7]
print "[08] unbalance airflow selection ............... : ",result.registers[8],"% (default: 0 %)"
print "[09] low airflow setting ....................... : ",result.registers[9],"V (default: 5 V)"
print "[10] temporised 1/2h boost airflow setting ..... : ",result.registers[10],"V (default: 10 V)"
print "[11] freecooling airflow setting ............... : ",result.registers[11],"V (default: 10 V)"
print "[12] ** UNDOCUMENTED / UNSED ** ................ : ",result.registers[12]
print "[13] ** UNDOCUMENTED / UNSED ** ................ : ",result.registers[13]
print "[14] ** UNDOCUMENTED / UNSED ** ................ : ",result.registers[14]
print "[15] airflow set ............................... : ",result.registers[15]," <=> ",airflow_set, " (default: low)"
print "[16] minimum set 0-10v ......................... : ",result.registers[16],"V (default: 0 V)"
print "[17] maximum set 0-10v ......................... : ",result.registers[17],"V (default: 10 V)"
print "[18] ** UNDOCUMENTED / UNSED ** ................ : ",result.registers[18]
print "[19] ** UNDOCUMENTED / UNSED ** ................ : ",result.registers[19]
print "[20] ** UNDOCUMENTED / UNSED ** ................ : ",result.registers[20]
print "[21] ** UNDOCUMENTED / UNSED ** ................ : ",result.registers[21]
print "[22] bypass auto text mini ..................... : ",result.registers[22],"oC (default 12 oC)"
print "[23] bypass auto tint mini ..................... : ",result.registers[23],"oC (default 24 oC)"
print "[24] timer manual bypass ....................... : ",result.registers[24],"hours (default 8 hours)"
print "[25] pre heating battery t on .................. : ",result.registers[25],"oC (no default documented)"
print "[26] pre heating battery t off ................. : ",result.registers[26],"oC (no default documented)"
print "[27] post heating battery t on ................. : ",result.registers[27],"oC (no default documented)"
print "[28] post heating battery t off ................ : ",result.registers[28],"oC (default 18 oC)"
print "[29] ** UNDOCUMENTED / UNSED ** ................ : ",result.registers[29]
print "[30] ** UNDOCUMENTED / UNSED ** ................ : ",result.registers[30]
print "[31] timer filter alarm set .................... : ",result.registers[31],"months (default 6 months)"
print "[32] tension minimum en 0-10v .................. : ",result.registers[32],"V (default: 0 V)"
print "[33] tension maximum en 0-10v .................. : ",result.registers[33],"V (default: 10 V)"
