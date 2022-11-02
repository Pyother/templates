from fpdf import FPDF

class PDF():

    file = FPDF()
    array_elements = []

    def __init__(self, array_elements):

        self.array_elements = array_elements
        self.names = ["Pracodawca", "System", "Nazwa", "Plec", "Dane 1", "Stawka", "Data", "Dodatek", "Dane 2",
        "Dane 3", "Dane 4"]
        
        self.file.add_page()
        self.file.set_fill_color(184, 200, 227)
        self.file.set_font("Arial", "", 10)
        self.file.multi_cell(w=190, h=10, txt="INDYWIDUALNA PROPOZYCJA ZATRUDNIENIA", align="C")
        self.file.set_font("Arial", "", 8)
        self.file.multi_cell(w=190, h=5, txt="""W obecnej chwili trwaja prace nad przetwarzaniem danych.
        Ten dokument jest przykladem wizualizacji danych pobranych z formularza.""", align="C")
        self.file.multi_cell(w=1, h=10, txt="")
        for i in range(len(self.names)):
            self.file.cell(w=17, h=10, txt=self.names[i], fill=True, border=1)
        self.file.multi_cell(w=1, h=10, txt="")
        
        for i in range(len(array_elements)):
            self.file.cell(w=17, h=10, txt=array_elements[i], border=1)
        self.file.multi_cell(w=1, h=10, txt="")

        self.file.output('calculator\output\Results.pdf')

    def __str__(self):
        print(f"OUTPUT: {self.array_elements}")



