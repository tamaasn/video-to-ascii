import sys
import os
import time

def run(path):
    ascii_dir = os.listdir(path)
    count=0
    while count < len(ascii_dir):
        with open(path+"/frame{}.txt".format(count) , "r") as f:
            sys.stdout.write(f.read())

        time.sleep(1/30)
        count += 1

    '''for ascii_file in ascii_dir:
        filename = path+"/"+ascii_file
        with open(filename , "r") as f:
            sys.stdout.write(f.read())
        time.sleep(1/30)
        sys.stdout.flush()
'''

