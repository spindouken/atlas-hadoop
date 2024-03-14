#!/bin/bash
# work in progress

mapred streaming \
    -input /holbies/input/salaries.csv \
    -output /holbies/output \
    -mapper mapper.py \
    -reducer reducer.py
