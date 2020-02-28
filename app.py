from os import listdir, path
import sys

wordsMap = dict()

def getCurrentFiles(directory,ext_ignore=()):
    for file in listdir(directory):
        dirFile=directory+'\\'+file
        print(dirFile)
        if path.isdir(dirFile):
            getCurrentFiles(dirFile,ext_ignore=ext_ignore)
        else:
            if not dirFile.endswith(ext_ignore):
                processFile(dirFile)

def processFile(filename):
    with open(filename) as file:
        words = file.read().split()
        for word in words:
            updateMap(word)

def updateMap(word):
    if wordsMap.get(word) is None:
        wordsMap[word]=1
    else:
        wordsMap[word]+=1

if __name__ == "__main__":
    with open("file_ext_ignore.txt", "r") as file_ext_ignore:
        exts=tuple(file_ext_ignore.read().split())

    getCurrentFiles(sys.argv[1],exts)
    
    with open(sys.argv[2], "w+") as file:
        for key, value in sorted(wordsMap.items()):
            file.write(f'{key} : {value} \n')