#!/bin/bash
# script to remmove uploaded file if it exists


remove_file_if_exists() {
    file_path=$1 # file to remove will be given by 1st arg
    # check if the file exists
    hdfs dfs -test -e $file_path

    # if the file exists, remove it
    if [ $? -eq 0 ]; then
        hdfs dfs -rm $file_path
        echo "File $file_path removed from HDFS."
    else
        echo "File $file_path does not exist in HDFS."
    fi
}

# remove lao.txt from /holbies/input if it exists
remove_file_if_exists /holbies/input/lao.txt
