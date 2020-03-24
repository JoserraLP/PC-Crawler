from crawler import Crawler
import thesaurus as Thesaurus
from parser import Parser
from user_interface import UserInterface

if __name__ == "__main__":
    with open("file_ext_accept.txt", "r") as file_ext_accept:
        exts=tuple(file_ext_accept.read().split())
    
    parser=Parser('Thesaurus_es_ES.txt')

    crawler = Crawler(exts, thesaurus.keys(),parser.process_file)
    
    ui = UserInterface(thesaurus=thesaurus, crawler=crawler)
    ui.loadGUI()