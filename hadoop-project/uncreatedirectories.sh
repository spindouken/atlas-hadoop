#!/bin/bash

# remove the directory if it exists
#   and check if the parent directory is empty afterwards
#   to remove it as well
remove_directory_if_exists() {
    directory_path=$1 # directory to remove will be given by 1st arg
    # check if the directory exists
    hdfs dfs -test -e $directory_path

    # if the directory exists, remove it
    if [ $? -eq 0 ]; then
        hdfs dfs -rm -r $directory_path
        echo "Directory $directory_path removed from HDFS."

        # check if parent directory is empty and remove if it is
        parent_dir=$(dirname $directory_path)
        if [ "$(hdfs dfs -ls $parent_dir | wc -l)" -eq 0 ]; then
            hdfs dfs -rm -r $parent_dir
            echo "Parent directory $parent_dir removed from HDFS as it was empty."
        fi
    else
        echo "Directory $directory_path does not exist in HDFS."
    fi
}

# attempt to remove the /holbies/input directory and then /holbies
remove_directory_if_exists /holbies/input
remove_directory_if_exists /holbies
