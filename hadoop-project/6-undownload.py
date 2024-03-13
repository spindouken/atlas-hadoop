#!/usr/bin/env python2.7
import os

def remove_downloaded_file(file_path):
    target_path = '/tmp/' + os.path.basename(file_path)
    
    # check if the file exists at the location
    if os.path.exists(target_path):
        try:
            # if the file exists, attempt to remove it
            os.remove(target_path)
            # print a message indicating successful removal
            print({'path': target_path, 'result': True, 'error': '', 'action': 'removed'})
        except Exception as e:
            # handle any exceptions that occur during file removal
            #   and print the error along with the file path
            print({'path': target_path, 'result': False, 'error': str(e), 'action': 'remove_failed'})
    else:
        # if the file does not exist, print a message indicating it's already removed or was never downloaded
        print({'path': target_path, 'result': False, 'error': 'file does not exist', 'action': 'no_action_needed'})

files_to_remove = "/holbies/input/lao.txt"
remove_downloaded_file(files_to_remove)
