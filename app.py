from PyQt5 import QtWidgets, QtCore,uic
from crawler import Crawler
import thesaurus as Thesaurus
import sys

class Main:

    def __init__(self, thesaurus, crawler):
        self.thesaurus = thesaurus
        self.crawler = crawler

    def get_dir_file(self):
        """
        Get the directory or file to be processed selected in the UI
        """
        if (self.win.is_file.isChecked()):
            act_name = str(QtWidgets.QFileDialog.getOpenFileName(self.win, "Select a file")[0])
        else:
            act_name = str(QtWidgets.QFileDialog.getExistingDirectory(self.win, "Select Directory"))
        self.win.selected_name.setText(act_name)
        if act_name != "":
            self.words_freq = self.crawler.get_frequencies(act_name)
            files_processed = self.crawler.get_files_count()
            if files_processed == -1 :
                self.win.label_6.setText("Loaded from cache")
                self.win.total_files.setVisible(False)
            elif files_processed == 0:
                self.win.label_6.setText("No files processed")
                self.win.total_files.setVisible(False)
            else:
                self.win.total_files.setText(str(files_processed))
            print(self.words_freq)

    def search_frequency(self):
        """
        Search a word in the map and get its frequency. The word is selected in the UI
        """
        word = self.win.search_text.toPlainText()
        self.win.list_results.clear()
        if not self.words_freq is None:
            sinonims = thesaurus.get(word)
            total_freq = 0
            if(sinonims is not None):
                for sinonim in sinonims:
                    freq = self.words_freq.get(sinonim)
                    self.win.list_results.addItem(f'{sinonim}: {freq if not freq is None else 0}')
                    print(f' - {sinonim}: {freq if not freq is None else 0}')
                    if not freq is None:
                        total_freq += freq
                self.win.total_frequency.setText(str(total_freq))
            else:
                self.win.list_results.addItem('No se ha encontrado la palabra buscada')

    def loadGUI(self):
        """
        Load the GUI for the application
        """
        #Qt code
        app = QtWidgets.QApplication([])

        self.win = uic.loadUi("user-interface.ui") #specify the location of your .ui file
        self.win.setWindowTitle("PC Crawler - Recuperación y busqueda en la web")
        self.win.load_files_btn.clicked.connect(self.get_dir_file)
        self.win.search_button.clicked.connect(self.search_frequency)

        self.win.setWindowFlags(self.win.windowFlags()
                        ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.win.show()
        
        sys.exit(app.exec())

if __name__ == "__main__":
    with open("file_ext_accept.txt", "r") as file_ext_accept:
        exts=tuple(file_ext_accept.read().split())
    thesaurus = Thesaurus.createThesaurus('Thesaurus_es_ES.txt')
    crawler = Crawler(exts, thesaurus.keys())

    main = Main(thesaurus=thesaurus, crawler=crawler)

    main.loadGUI()


