from os import listdir, path
import sys, re, json, unidecode
from file_parser import Parser
class Crawler:

    def __init__(self, file_ext_accept, accepted_words):
        self.file_ext_accept = file_ext_accept
        self.accepted_words = accepted_words
        self.words_map = dict()
        self.parser=Parser()

    def get_word_frequency(self, name):
        """
        Get the frequency of every word in a directory or a file
    
        Parameters: 
        name (str): name of the directory or file to be processed 
        """
        elems = [] 
        elems.append(name)
        while len(elems) > 0:
            elem = elems.pop()
            if path.isdir(elem):
                for file in listdir(elem):
                    elems.append(elem + '\\' + str(file))
            else:
                print(elem)
                if elem.endswith(self.file_ext_accept):
                    words=self.parser.process_file(elem)
                    for word in words:
                        self.update_map(word)

    def update_map(self, word):
        """
        Update the word count map  
    
        If a word is in the map it increases the count, if not the word is insert in the map 
    
        Parameters: 
        word (str): word to be processed 
        """
        if word in self.accepted_words:
            if self.words_map.get(word) is None:
                self.words_map[word] = 1
            else:
                self.words_map[word] += 1

    def get_frequencies(self,dir_name):
        """
        Gets frequencies if they have been processed before
    
        If the directory has been processed before it loads the frequency,
        if not it process it. Finally, it saves the map in a file.
    
        Parameters: 
        dir_name (str): name of the directory to be processed 
        """
        dir_name_cache = dir_name.replace('\\', '').replace('/','').replace('.', '').replace(':', '-')
        try:
            dict_file = open(f'.cache/{dir_name_cache}.cache', 'r')
            self.words_map = json.load(dict_file)
            print(f'Loaded file .cache/{dir_name_cache}.cache')
        except:
            self.get_word_frequency(dir_name)

        with open(f'.cache/{dir_name_cache}.cache', "w+") as file:
            json.dump(dict(sorted(self.words_map.items())),file)
        
        return self.words_map