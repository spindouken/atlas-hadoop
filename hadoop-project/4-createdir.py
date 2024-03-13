#!/usr/bin/env python2.7
from snakebite.client import Client


def list_directory(client, directory):
    """
    attempt to list a directory in HDFS
    
    returns true if the directory exists, false otherwise
    """
    try:
        # convert generator to list for evaluation
        list(client.ls([directory]))
        return True
    except:
        return False

def createdir(l):
    """
    function to create directory in HDFS
    """
    client = Client('hadoop3', 9000)
    for directory in l:
        # check if the directory already exists
        if not list_directory(client, directory):
            # if the directory doesn't exist, make it
            result = client.mkdir([directory], create_parent=True)
            print({'path': directory, 'result': next(result)['result']})
        else:
            print("Directory {} already exists.".format(directory))
