from os import listdir, path
import sys
import re

wordsMap = dict()

def getWordFrequencyOnDirectory(directory,file_ext_accept=()):
    for file in listdir(directory):
        dirFile=directory+'\\'+file
        print(dirFile)
        if path.isdir(dirFile):
            getWordFrequencyOnDirectory(dirFile,file_ext_accept=file_ext_accept)
        else:
            if dirFile.endswith(file_ext_accept):
                processFile(dirFile)

def processFile(filename):
    with open(filename) as file:
        words = [word.lower() for word in re.split(r'\W+',file.read())]
        for word in words:
            updateMap(word)

def updateMap(word):
    if wordsMap.get(word) is None:
        wordsMap[word]=1
    else:
        wordsMap[word]+=1

if __name__ == "__main__":
    with open("file_ext_accept.txt", "r") as file_ext_accept:
        exts=tuple(file_ext_accept.read().split())

    getWordFrequencyOnDirectory(sys.argv[1],exts)

    with open(sys.argv[2], "w+") as file:
        for key, value in sorted(wordsMap.items()):
            file.write(f'{key} : {value} \n')