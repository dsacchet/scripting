#!/usr/bin/python

import subprocess
import re
import os

p = subprocess.Popen(['/usr/bin/whisper-dump','/var/lib/graphite/whisper/servers/kwazii/vmc/text.wsp'],
                         stdout=subprocess.PIPE,
                         shell=False)

search_first_line = re.compile(r'^86153: ')
search_last_line = re.compile(r'^89045: ')
parse_data_line = re.compile(r'^([0-9]*): *([0-9]*), *([0-9\.]*)$')

start=False
for line in p.stdout:
	if start is False:
		#print "On cherche la premiere ligne"
		result = search_first_line.match(line)
		if result is not None:
			print "On a trouve la premiere ligne"
			start = True
	else:
		result = search_last_line.match(line)
		if result is not None:
			print "On a trouve la derniere ligne"
			break
		result = parse_data_line.match(line)
		if result is not None:
			timestamp = int(result.group(2))
			try:
				value = int(result.group(3))
			except ValueError:
				continue
			if value % 5 == 0 and value != 5 and value != 0:
				new_value = float(value)/10.0
				os.system("/usr/bin/whisper-update /var/lib/graphite/whisper/servers/kwazii/vmc/text.wsp %d:%0.2f" % (timestamp,new_value))
		
p.kill()	
