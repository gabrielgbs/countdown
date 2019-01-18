#!/usr/bin/python3

import sys
import time
import datetime
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('time', help='Time to wait, in format D:H:M:S');
arg_parser.add_argument('-v', '--verbose', help='More detailed output', action='store_true')
arg_parser.add_argument('-n', '--newline', help='Uses new line (\\n) instead of carriage return (\\r) in output', action='store_true')
args = arg_parser.parse_args()

def time_now():
	return int(time.mktime(time.localtime()))

line_clear = '\x1b[2K\r'
arg_time = args.time
arg_time = arg_time.split(':')
arg_time = list(reversed(arg_time))
days = 0
hours = 0
minutes = 0
seconds = 0

try:
	seconds = int(arg_time[0])
	minutes = int(arg_time[1])
	hours = int(arg_time[2])
	days = int(arg_time[3])
except ValueError:
	arg_parser.print_help()
	sys.exit(1)
except IndexError:
	pass

time_goal = seconds
time_goal += minutes*60
time_goal += hours*3600
time_goal += days*86400
time_goal += time_now()

str_time_goal = ', ends in '+ time.strftime('%c', time.localtime(time_goal))

while time_now() < time_goal:
	output_text = str(datetime.timedelta(seconds=time_goal - time_now()))
	
	if args.verbose:
		output_text += str_time_goal

	if not args.newline:
		print(line_clear, end='', flush=True)

	print(output_text , end='', flush=True)

	try :
		time.sleep(1)
	except KeyboardInterrupt:
		print(line_clear + 'Countdown interrupted by user')
		sys.exit(1)

	if args.newline:
		print('')


if args.verbose:
	print(('' if args.newline else line_clear) + args.time + ' countdown finished.')
else:
	if not args.newline:
		print(line_clear, end='')
#end
