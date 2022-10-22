from fpdf import FPDF

class PDF():

    file = FPDF()

    def __init__(self, array_elements):
        
        self.file.add_page()
        self.file.set_font("Arial", "", 10)
        self.file.multi_cell(w=190, h=10, txt="New page created")
        self.file.multi_cell(w=190, h=10, txt=array_elements[2])

        self.file.output('calculator\output\Results.pdf')



