#!/usr/bin/env python2.7
from snakebite.client import Client
import os

def download(l):
    # initialize snakebite client to interact with HDFS
    client = Client('hadoop3', 9000)
    for file_path in l:
        # construct target path in /tmp directory
        # this is where the file will be saved after download
        target_path = '/tmp/' + os.path.basename(file_path)  # ensures the filename is correctly appended to /tmp/
        
        # check if the file already exists
        if os.path.exists(target_path):
            # if the file exists, print a message and skip to the next file
            print({'path': target_path, 'result': False, 'error': 'file exists', 'source_path': file_path})
            continue  # move to the next file without attempting download
        
        try:
            # attempt to download the file to location
            for x in client.copyToLocal([file_path], '/tmp'):
                # print the result of the download attempt
                # default to True for 'result' and empty string for 'error' if not given
                result = x.get('result', True)  # assume success if 'result' key is missing
                error = x.get('error', '')  # assume no error if 'error' key is missing
                print({'path': target_path, 'result': result, 'error': error, 'source_path': file_path})
        except Exception as e:
            # handle any exceptions that occur during the download
            #   and print the error along with the file path
            print({'path': target_path, 'result': False, 'error': str(e), 'source_path': file_path})
