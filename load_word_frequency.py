from os import listdir, path
import sys, re, json, unidecode

def getWordFrequencyOnDirectory(directory,file_ext_accept=(),wordsMap=dict()):
    for file in listdir(directory):
        dirFile=directory+'\\'+file
        if path.isdir(dirFile):
            getWordFrequencyOnDirectory(dirFile,file_ext_accept=file_ext_accept,wordsMap=wordsMap)
        else:
            print(dirFile)
            if dirFile.endswith(file_ext_accept):
                processFile(dirFile,wordsMap)

def processFile(filename, wordsMap):
    with open(filename, encoding='utf-8') as file:
        words = [word.lower() for word in re.split(r'\W+',unidecode.unidecode(file.read()))]
        for word in words:
            updateMap(word,wordsMap)

def updateMap(word, wordsMap):
    if wordsMap.get(word) is None:
        wordsMap[word]=1
    else:
        wordsMap[word]+=1

def loadFrequencies(dir_name,exts=tuple()):
    try:
        dict_file=open(f'.cache/{dir_name}.cache', 'r')
        wordFrequency=json.load(dict_file)
        print(f'Loaded file .cache/{dir_name}.cache')
    except:
        wordFrequency=dict()
        getWordFrequencyOnDirectory(dir_name,exts,wordsMap=wordFrequency)

    with open(f'.cache/{dir_name}.cache', "w+") as file:
        json.dump(dict(sorted(wordFrequency.items())),file)
    
    return wordFrequency