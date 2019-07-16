# Countdown timer

A more sophisticated "sleep" function for consoles.
Comes from the need of a sleep function with visual output, when the user needs to know how much time is left to wait until the next command of a shell script.

## Requirements

Python 3. Thtat's it.

## Examples

For the examples, the path to the file countdown.py is aliased as "countdown"

### Sleep for 30 seconds:
```sh
$ countdown 30
```
Initial output:
```sh
30
```

### Sleep for 5 minutes:
```sh
$ countdown 5:0
```
Initial output:
```sh
5:00
```

### Sleep for 1 hour and 10 seconds:
```sh
$ countdown 1:0:10
```
Initial output:
```sh
1:00:10
```

### Sleep for 1 day
```sh
$ countdown 1:0:0:0
```
Initial output:
```sh
1 day, 0:00:00
```

### Scenario: It's 1:20PM and I need my script to sleep until 11PM:
```sh
$ countdown 10:-20:0 # Sleeps for 10 hours minus 20 minutes
```
Initial output:
```sh
9:40:00
```

### Scenario: It's 1:20PM and I need a script to sleep until tomorrow at noon:
```sh
$ countdown 1:-1:-20:0 # Sleeps for 1 day, minus 1 hour, minus 20 minutes
```
Initial output:
```sh
22:40:00
```

### Scenario: I need a script to sleep for 1 day and 1 hour
You could use, for example:
```sh
$ countdown 1:1:0:0 # 1 day and 1 hour
```
or:
```sh
$ countdown 25:0:0 # 25 hours
```
or:
```sh
$ countdown 24:60:0 # 24 hours plus 60 minutes
```
or:
```sh
$ countdown 2:-23:0:0 # 2 days minus 23 hours
```
... I think you got the idea. For all those cases, the initial output will be:
```sh
1 day, 1:00:00
```
## Optional arguments:

### -v, --verbose

Prints a more detailed output. For example, for the command:
```sh
$ countdown 1:1:0:0 # 1 day and 1 hour
```
The initial output was (at the time this guide was written):
```sh
1 day, 1:00:00, ends in Fri Jan 18 15:42:30 2019
```

### -n, --newline

Uses the "new line" character (\n) instead of  "carriage return" (\r) in output. This is useful when you're writing the output of a script to a log file. As an example, for the command:
```sh
$ countdown 10 -n
```
The full output is:
```sh
0:00:10
0:00:09
0:00:08
0:00:07
0:00:06
0:00:05
0:00:04
0:00:03
0:00:02
0:00:01
```
You can combine the arguments as well. For instance, the command
```sh
$ countdown 10 -nv
```
Generated the output (at the time this guide was witten):
```sh
0:00:10, ends in Thu Jan 17 14:50:29 2019
0:00:09, ends in Thu Jan 17 14:50:29 2019
0:00:08, ends in Thu Jan 17 14:50:29 2019
0:00:07, ends in Thu Jan 17 14:50:29 2019
0:00:06, ends in Thu Jan 17 14:50:29 2019
0:00:05, ends in Thu Jan 17 14:50:29 2019
0:00:04, ends in Thu Jan 17 14:50:29 2019
0:00:03, ends in Thu Jan 17 14:50:29 2019
0:00:02, ends in Thu Jan 17 14:50:29 2019
0:00:01, ends in Thu Jan 17 14:50:29 2019
10 countdown finished.
```
