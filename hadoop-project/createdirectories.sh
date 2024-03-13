#!/bin/bash

# this function will check if the directory (1 arg given with function)
#   exists and create it if it doesn't exist
check_and_create_directory() {
    directory_path=$1 # directory to create will be given by 1st arg
    # check if the directory exists
    hdfs dfs -test -e $directory_path

    # check if the last command was successful 
    if [ $? -eq 0 ]; then # success means the directory exists
        echo "Directory $directory_path already exists in HDFS."
    else
        # if the directory doesn't exist, create it
        hdfs dfs -mkdir -p $directory_path
        echo "Directory $directory_path created successfully in HDFS."
    fi
}

# use function to check and create /holbies directory in HDFS
check_and_create_directory /holbies

# use function to check and create /holbies/input directory in HDFS
check_and_create_directory /holbies/input
