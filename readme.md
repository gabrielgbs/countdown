# Countdown timer

A more sophisticated "sleep" function for consoles.
Rises from the need of a sleep function with visual output, when the user needs to know how much time is left to wait until, let's say, the next command of a shell script.

# Requirements

Python 3. Thtat's it.

# Examples

For the examples, the path to the file countdown.py is aliased as "countdown"

## To sleep for 30 seconds:
```sh
$ countdown 30
```
Initial output:
```sh
30
```

## To sleep for 5 minutes:
```sh
$ countdown 5:0
```
Initial output:
```sh
5:00
```

## To sleep for 1 hour and 10 seconds:
```sh
$ countdown 1:0:10
```
Initial output:
```sh
1:00:10
```

## Scenario: It's 1:20PM and I need to sleep until 11PM:
```sh
$ countdown 10:-20:0 # Sleeps for 10 hours minus 20 minutes
```
Initial output:
```sh
9:40:00
```

## Scenario: It's 1:20PM and I need to sleep until tomorrow at noon:
```sh
$ countdown 1:-1:-20:0 # Sleeps for 1 day, minus 1 hour, minus 20 minutes
```
Initial output:
```sh
22:40:00
```

## Scenario: I need to sleep for 1 day and 1 hour
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
$ countdown 24:60:0 # 24 hours plus 60 seconds
```
or:
```sh
$ countdown 2:-23:0:0 # 2 days minus 23 hours
```
... I think you got the idea. For all those cases, the initial output will be:
```sh
1 day, 1:00:00
```