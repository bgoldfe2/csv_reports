import csv
import textwrap
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
                val_str = self.indent_txt(value,indent+1,4)
                #print (val_str)
                self.multi_cell(0,6,txt=str(val_str))

    def indent_txt(self,data='',indent=0,char_num=4):
    
        every = 120 - indent * char_num
        spaces = char_num * indent

        data_lf = textwrap.fill(data, every)
        return (textwrap.indent(data_lf, ' ' * spaces, lambda line: True))

pdf = PDF()
filename ="sample_data.csv"
pdf.create_body(filename)
pdf.output('example4.pdf', 'F')
