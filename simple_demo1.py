# simple_demo.py

from fpdf import FPDF
import csv
import pprint

def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))


filename ="sample_data.csv"
  
a_csv_file = open(filename, "r")
dict_reader = csv.DictReader(a_csv_file)

dict_list = []

for line in dict_reader:
    dict_list.append(line)

pprint.pprint(dict_list)


for dline in dict_list:

    for key, value in dline.items():
        print(key, '--',value)
        
        


"""
pdf = FPDF()
pdf = FPDF(orientation='P', unit='mm', format='letter')
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Welcome to Python!", ln=1, align="C")
#pdf.output("simple_demo.pdf")
"""
