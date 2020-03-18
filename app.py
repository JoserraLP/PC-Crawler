from PyQt5 import QtWidgets, QtCore,uic
from crawler import Crawler
import thesaurus as Thesaurus
import sys


filename=""
win=None
thesaurus=None
crawler=None

def getDirFile():
    filename= str(QtWidgets.QFileDialog.getExistingDirectory(win, "Select Directory"))
    win.selectedDir.setText(filename)
    if (not crawler is None) and filename!="":
        win.words_freq = crawler.get_frequencies(filename)
        print(win.words_freq)

def searchFrequency():
    word=win.searchText.toPlainText()
    win.listResults.clear()
    words_freq=win.words_freq
    if not words_freq is None:
        sinonims = thesaurus.get(word)
        total_freq = 0
        if(sinonims is not None):
            for sinonim in sinonims:
                freq = words_freq.get(sinonim)
                win.listResults.addItem(f'{sinonim}: {freq if not freq is None else 0}')
                print(f'-{sinonim}: {freq if not freq is None else 0}')
                if not freq is None:
                    total_freq += freq
            win.totalFrequency.setText(str(total_freq))
        


if __name__ == "__main__":
    with open("file_ext_accept.txt", "r") as file_ext_accept:
        exts=tuple(file_ext_accept.read().split())
    thesaurus = Thesaurus.createThesaurus('Thesaurus_es_ES.txt')
    crawler = Crawler(exts, thesaurus.keys())

    #Qt code
    app = QtWidgets.QApplication([])

    win = uic.loadUi("user-interface.ui") #specify the location of your .ui file
    win.setWindowTitle("PC Crawler - Recuperación y busqueda en la web")
    win.loadFilesButton.clicked.connect(getDirFile)
    win.searchButton.clicked.connect(searchFrequency)


    win.setWindowFlags(win.windowFlags()
                    ^ QtCore.Qt.WindowContextHelpButtonHint)
    win.show()
    
    sys.exit(app.exec())

    """
    

    

    while True:
        word = input("\nIntroduzca su busqueda de sinónimos: \n(Salir => /exit)\nBusqueda: ")
        print(word)
        if (word != '/exit'):
            
        else:
            break
        """
