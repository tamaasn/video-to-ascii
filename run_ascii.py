import os
import time

def run(path):
    ascii_dir = os.listdir(path)
    count=0
    while count < len(ascii_dir):
        with open(path+"/frame{}.txt".format(count) , "r") as f:
            print(f.read())

        time.sleep(1/30)
        count += 1
