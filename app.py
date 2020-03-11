from os import listdir, path
import sys
import re

def getWordFrequencyOnDirectory(directory,file_ext_accept=(),wordsMap=dict()):
    for file in listdir(directory):
        dirFile=directory+'\\'+file
        print(dirFile)
        if path.isdir(dirFile):
            getWordFrequencyOnDirectory(dirFile,file_ext_accept=file_ext_accept,wordsMap=wordsMap)
        else:
            if dirFile.endswith(file_ext_accept):
                processFile(dirFile,wordsMap)

def processFile(filename,wordsMap):
    with open(filename) as file:
        words = [word.lower() for word in re.split(r'\W+',file.read())]
        for word in words:
            updateMap(word,wordsMap)

def updateMap(word,wordsMap):
    if wordsMap.get(word) is None:
        wordsMap[word]=1
    else:
        wordsMap[word]+=1

if __name__ == "__main__":
    with open("file_ext_accept.txt", "r") as file_ext_accept:
        exts=tuple(file_ext_accept.read().split())
    wordFrequency=dict()
    getWordFrequencyOnDirectory(sys.argv[1],exts,wordsMap=wordFrequency)

    with open(sys.argv[2], "w+") as file:
        for key, value in sorted(wordFrequency.items()):
            file.write(f'{key} : {value} \n')