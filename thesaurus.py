import unidecode

def createThesaurus(filename):
    thesaurus_dict=dict()
    with open(filename,encoding='utf-8') as thesaurus_file:
        for line in thesaurus_file.readlines():
            sinonims=unidecode.unidecode(line[:-1]).split(';')
            for word in sinonims:
                thesaurus_dict[word]=tuple(sinonims)
    return thesaurus_dict
