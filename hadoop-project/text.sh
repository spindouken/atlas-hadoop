#!/bin/bash
# displays the content of lao.txt from the HDFS

# check if the file exists and display its content
display_file_content_if_exists() {
    file_path=$1

    # check if the file exists
    hadoop fs -test -e $file_path
    if [ $? -eq 0 ]; then
        # if the file exists, display its content
        hadoop fs -cat $file_path
    else
        # if the file does not exist, print an error message
        echo "The file $file_path does not exist in HDFS."
    fi
}

# use display file function to check for file
#   and display it's contents to stdout
display_file_content_if_exists /holbies/input/lao.txt
