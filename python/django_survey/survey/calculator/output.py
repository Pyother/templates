from fpdf import FPDF

class PDF():

    file = FPDF()
    array_elements = []

    def __init__(self, array_elements):

        self.array_elements = array_elements
        
        self.file.add_page()
        self.file.set_font("Arial", "", 10)
        self.file.multi_cell(w=190, h=10, txt="New page created")
        
        for i in range(len(array_elements)):
            self.file.multi_cell(w=190, h=10, txt=array_elements[i])

        self.file.output('calculator\output\Results.pdf')

    def __str__(self):
        print(f"OUTPUT: {self.array_elements}")



