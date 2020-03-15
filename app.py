import load_word_frequency as Loader
import sys

if __name__ == "__main__":
    with open("file_ext_accept.txt", "r") as file_ext_accept:
        exts=tuple(file_ext_accept.read().split())
    
    words_freq = Loader.loadFrequencies(sys.argv[1],exts=exts)

    while True:
        word=input("\nIntroduzca su busqueda: \n(Salir => /exit)\nWord: ")
        if (word != '/exit'):
            freq = words_freq.get(word)
            print(f'Freq: {freq}') if freq is not None else print(f'Freq: 0')
        else:
            break
