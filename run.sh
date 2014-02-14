#!/bin/bash

hadoop jar /usr/local/hadoop/contrib/streaming/hadoop-streaming-1.2.1.jar -file /home/aganguly/airlinedata/mapper.py -mapper mapper.py -file /home/aganguly/airlinedata/reducer.py -reducer reducer.py -input /user/aganguly/test/1987.csv -output /user/aganguly/myoutput