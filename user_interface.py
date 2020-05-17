from PyQt5 import QtWidgets, QtCore,uic
import sys

class UserInterface:
    """
    Class containing the loader of the user interface for the web crawler
    """
    def __init__(self, thesaurus, crawler):
        self.thesaurus = thesaurus
        self.crawler = crawler
        self.words_freq = dict()

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
            print(self.words_freq)

    def search_frequency(self):
        """
        Search a word in the map and get its frequency. The word is selected in the UI
        """
        word = self.win.search_text.toPlainText().lower()
        self.win.list_results.clear()
        self.win.list_sinonimos.clear()
        if not self.words_freq is None and word != '':
            sinonims = self.thesaurus.get(word)
            total_freq = 0
            if sinonims is not None:
                #De aqui
                freq_word = self.words_freq.get(word)
                files=list(zip(self.crawler.file_names,self.crawler.file_lengths))
                print(files)
                freq_locales=freq_word["frecuencias_locales"]
                freq_files=list()
                for k,v in freq_locales.items():
                    file=files[int(k)]
                    freq_files.append( (file[0],file[1],v) )

                result=sorted(freq_files,key=lambda x: x[2]/x[1],reverse=True)
                for res in result:
                    self.win.list_results.addItem(f'{res[0]} => {res[2]/res[1]}')
                #Hasta aqui - liarla parda
                for sinonim in sinonims:
                    freq = self.words_freq.get(sinonim)
                    self.win.list_sinonimos.addItem(f'{sinonim} => {str(freq["frecuencia_total"]) if not freq is None else 0}')
                    print(f' - {sinonim}: {freq if not freq is None else 0}')
                
            else:
                self.win.list_results.addItem('No se ha encontrado la palabra buscada')
        else:
            self.win.list_results.addItem('Por favor, busca una palabra')
            total_freq = 0
        self.win.total_frequency.setText(str(total_freq))

    def loadGUI(self):
        """
        Load the GUI for the application
        """
        app = QtWidgets.QApplication([])

        self.win = uic.loadUi("user-interface.ui") #specify the location of your .ui file
        self.win.setWindowTitle("PC Crawler - RIBW")
        self.win.load_files_btn.clicked.connect(self.get_dir_file)
        self.win.search_button.clicked.connect(self.search_frequency)

        self.win.setWindowFlags(self.win.windowFlags()
                        ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.win.show()
        
        sys.exit(app.exec())