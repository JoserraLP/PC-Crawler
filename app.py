from os import listdir, path
import sys

def getCurrentFiles(directory):
    files = [f for f in listdir(directory)]
    print(files)

if __name__ == "__main__":
    getCurrentFiles(sys.argv[1])