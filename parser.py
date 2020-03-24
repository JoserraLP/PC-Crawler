import pandas as pd


def processXls(filename):
    sheets = pd.read_excel(filename)
    results = []
    for cell in sheets.values.flatten():
        results.extend(str(cell).split())
    return results

if __name__ == "__main__":
    processXls("Test/ejemplo.xlsx")