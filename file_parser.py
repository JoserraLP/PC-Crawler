import pandas as pd
import PyPDF2
import unidecode, re
import thesaurus
import os
from bs4 import BeautifulSoup as bs

class Parser:
    def process_file(self,filename):
        extension=os.path.splitext(filename)[-1]
        process_fun_dict={
            ".html":self.process_html,
            ".xlsx":self.process_xls,
            ".xls":self.process_xls,
            ".pdf":self.process_pdf,
            ".xml":self.process_xml
        }
        words=process_fun_dict.get(extension,self.process_txt)(filename)
        result=list(map(lambda word : word.lower(),words))
        return result


    def process_xls(self,filename):
        sheets = pd.read_excel(filename)
        results = []
        for cell in sheets.values.flatten():
            results.extend( re.split(r'\W+',unidecode.unidecode(str(cell))))
        return results
    def process_pdf(self,filename):
        results=[]
        pdfFileObj = open(filename, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        for page in pdfReader.pages:
            text=page.extractText()
            results.extend( re.split(r'\W+',unidecode.unidecode(text)))
        pdfFileObj.close()
        return results

    def process_html(self,file_name):
        html_doc = open(file_name, 'r')
        soup = bs(html_doc, 'html.parser')
        text=soup.getText()
        html_doc.close()
        return re.split(r'\W+',unidecode.unidecode(text))

    def process_xml(self,file_name):
        xml_doc = open(file_name, 'r')
        soup = bs(xml_doc, 'lxml')
        text= soup.getText()
        xml_doc.close()
        return re.split(r'\W+',unidecode.unidecode(text))

    def process_txt(self,file_name):
        with open (file_name, 'r', encoding='utf-8') as file:
            text=file.read()
        return re.split(r'\W+',unidecode.unidecode(text))

if __name__ == "__main__":
    parser=Parser("Thesaurus_es_ES.txt")
    print(parser.process_file("Test/TestFolder/lorem.html"))
    print(parser.process_file("Test/TestFolder/rimas_y_leyendas.pdf"))
