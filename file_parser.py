import pandas as pd
import PyPDF2
import unidecode, re
import thesaurus
import os
from bs4 import BeautifulSoup as bs

class Parser:

    def process_file(self,file_name):
        """
        Process a file depending on its extension
    
        Parameters: 
        file_name (str): name of the file to be processed 
        """
        extension = os.path.splitext(file_name)[-1]
        process_fun_dict = {
            ".html":self.process_html,
            ".xlsx":self.process_xls,
            ".xls":self.process_xls,
            ".pdf":self.process_pdf,
            ".xml":self.process_xml
        }
        words = process_fun_dict.get(extension, self.process_txt)(file_name)
        result = list(map(lambda word : word.lower(), words))
        return result


    def process_xls(self,file_name):
        """
        Process a xls file

        Parameters: 
        file_name (str): name of the file to be processed 
        """
        sheets = pd.read_excel(file_name)
        results = []
        for cell in sheets.values.flatten():
            results.extend(re.split(r'\W+',unidecode.unidecode(str(cell))))
        return results

    def process_pdf(self,file_name):
        """
        Process a pdf file
    
        Parameters: 
        file_name (str): name of the file to be processed 
        """
        results = []
        pdfFileObj = open(file_name, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        for page in pdfReader.pages:
            text = page.extractText()
            results.extend(re.split(r'\W+', unidecode.unidecode(text)))
        pdfFileObj.close()
        return results

    def process_html(self,file_name):
        """
        Process a html file
    
        Parameters: 
        file_name (str): name of the file to be processed 
        """
        html_doc = open(file_name, 'r')
        soup = bs(html_doc, 'html.parser')
        text = soup.getText()
        html_doc.close()
        return re.split(r'\W+',unidecode.unidecode(text))

    def process_xml(self,file_name):
        """
        Process a xml file
    
        Parameters: 
        file_name (str): name of the file to be processed 
        """
        xml_doc = open(file_name, 'r')
        soup = bs(xml_doc, 'lxml')
        text = soup.getText()
        xml_doc.close()
        return re.split(r'\W+',unidecode.unidecode(text))

    def process_txt(self,file_name):
        """
        Process a txt file
    
        Parameters: 
        file_name (str): name of the file to be processed 
        """
        with open (file_name, 'r', encoding='utf-8') as file:
            text = file.read()
        return re.split(r'\W+',unidecode.unidecode(text))
