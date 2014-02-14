#!/usr/local/bin/python
# mapper program
import sys
for line in sys.stdin:
    line.rstrip()
    delay = line.split(",")[14]
    try:
        x = int(delay)
        print '%d\t%d' % (x,1)
    except ValueError:
        pass
