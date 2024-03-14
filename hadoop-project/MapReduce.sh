#!/bin/bash
# attempt to setup jar job for mapreduce
# work in progress

hdfs dfs -mkdir -p /holbies/input/

# upload file if it doesn't exist in holbies/input
hadoop fs -put data/salaries.csv /holbies/input/salaries.csv

echo "File salaries.csv uploaded to /holbies/input successfully."

# remove any previous output
hdfs dfs -rm -r /holbies/output/

hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.2.2.jar \
    -files mapper.py,reducer.py \
    -input /holbies/input/salaries.csv \
    -output /holbies/output \
    -mapper /scripts/hadoop-project/mapper.py \
    -reducer /scripts/hadoop-project/reducer.py
