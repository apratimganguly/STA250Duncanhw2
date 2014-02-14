#!/usr/local/bin/python
# the reducer program

from operator import itemgetter
import sys

ArrDelay = None
totalfreq = 0

for line in sys.stdin:
    line.strip()
    delay, freq = line.split('\t',1)
    freq = int(freq)
    if ArrDelay == delay:
        totalfreq += freq
    else:
        print '%s\t%s' % (ArrDelay,totalfreq)
        totalfreq = freq
        ArrDelay = delay
