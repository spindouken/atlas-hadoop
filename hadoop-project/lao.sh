#!/bin/bash
# full script checks if a specified directory exists in HDFS, creates it if it doesn't,
#   and then uploads a file to that directory, echoing the status of each operation

# check if the given directory exists in HDFS
#   and return the check's exit status
check_dir_exists() {
    hadoop fs -test -e $1 # $1 is the directory to check
    return $? # return the exit status of the test command
}

# check if the /holbies/input directory exists and create it if not
#   ensuring the directory exists before attempting file upload
if check_dir_exists /holbies/input; then
    echo "Directory /holbies/input already exists in HDFS." # directory exists
else
    # if the directory doesn't exist, it's created
    hadoop fs -mkdir -p /holbies/input
    echo "Directory /holbies/input created in HDFS." # directory creation confirmation
fi

# attempt to upload the file to the directory
#   echoing the outcome of the operation
if hadoop fs -put data/lao.txt /holbies/input/lao.txt; then
    # if the put command was successful, echo success
    echo "File lao.txt uploaded to /holbies/input successfully."
else
    # if the put command failed, echo failure
    echo "Failed to upload lao.txt to /holbies/input."
fi
