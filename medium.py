import csv
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        #self.image('example.png', 50, 30, 100)
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Dissertation Schedule and Tasks', 1, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    def create_body(self,filename):
        # Set up page
        self.alias_nb_pages()
        self.add_page()
        self.set_font('Times', '', 12)
        
        # Read in CSV to loop and present
        # Current format is a list of dictionaries, iterate list print out dictionaries
        
        csv_file = open(filename, "r")
        dict_reader = csv.DictReader(csv_file)
        dict_list = []

        for line in dict_reader:
            dict_list.append(line)

        for d in dict_list:
            self.pretty(d)

    def pretty(self,d, indent=0):
        for key, value in d.items():
            self.cell(0,10,txt=str(key),ln=1,align='L')
            if isinstance(value, dict):
                self.pretty(value, indent+1)
            else:
                self.cell(0,10,txt=str(value),ln=1,align='L')


pdf = PDF()
filename ="sample_data.csv"
pdf.create_body(filename)
pdf.output('example4.pdf', 'F')
