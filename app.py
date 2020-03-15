import load_word_frequency as Loader
import thesaurus as Thesaurus
import sys

if __name__ == "__main__":
    with open("file_ext_accept.txt", "r") as file_ext_accept:
        exts=tuple(file_ext_accept.read().split())
    thes=Thesaurus.createThesaurus('Thesaurus_es_ES.txt')
    words_freq = Loader.loadFrequencies(sys.argv[1],exts=exts,acceptedWords=thes.keys())
    
    while True:
        word=input("\nIntroduzca su busqueda de sinónimos: \n(Salir => /exit)\nBusqueda: ")
        if (word != '/exit'):
            sinonims=thes.get(word)
            total_freq=0
            if(sinonims!=None):
                for sinonim in sinonims:
                    freq=words_freq.get(sinonim)
                    print(f'-{sinonim}: {freq if not freq is None else 0}')
                    if not freq is None:
                        total_freq+=freq
                print(f'Frequencia total: {total_freq}')
        else:
            break
