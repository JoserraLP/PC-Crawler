import pandas as pd
from bs4 import BeautifulSoup as bs
import unidecode, re

def processXls(filename):
    sheets = pd.read_excel(filename)
    results = []
    for cell in sheets.values.flatten():
        results.extend(str(cell).split())
    return results

def process_html(file_name):
    html_doc = open(file_name, 'r')
    soup = bs(html_doc, 'html.parser')
    return soup.getText().split()

def process_xml(file_name):
    xml_doc = open(file_name, 'r')
    soup = bs(xml_doc, 'lxml')
    return soup.getText().split()

def process_txt(file_name):
    with open (file_name, 'r', encoding='utf-8') as file:
        return re.split(r'\W+',unidecode.unidecode(file.read()))

if __name__ == "__main__":
    processXls("Test/ejemplo.xlsx")
    print(process_txt("./Test/quijote.txt"))
