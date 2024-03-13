#!/usr/bin/env python2.7
from snakebite.client import Client

def deletedir(l):
    client = Client('hadoop3', 9000)
    for directory in l:
        # check if the directory exists by trying to list it
        try:
            # if we can list the directory, it exists
            list(client.ls([directory]))
            # remove directory
            result = client.rmdir([directory])
            for r in result:
                print("Removed directory: {}".format(r['path']))
        except:
            # if the directory doesn't exist, catch the exception and continue
            print("Directory {} does not exist or could not be removed.".format(directory))

