import csv
import textwrap



def pretty(d, indent=0):
    for key, value in d.items():
        print(key)
        #cell(0,10,txt=str(key),ln=1,align='L')
        if isinstance(value, dict):
            pretty(value, indent+1)
        else:
            val_str = indent_txt(value,indent+1,4)
            print (val_str)
            #cell(0,10,txt=str(val_str),ln=1,align='L')

def indent_txt(data='',indent=0,char_num=4):

    every = 70 - indent * char_num
    spaces = char_num * indent

    data_lf = textwrap.fill(data, every)
    return (textwrap.indent(data_lf, ' ' * spaces, lambda line: True))

# Read in CSV to loop and present
# Current format is a list of dictionaries, iterate list print out dictionaries
filename ="sample_data.csv"
csv_file = open(filename, "r")
dict_reader = csv.DictReader(csv_file)
dict_list = []

for line in dict_reader:
    dict_list.append(line)

for d in dict_list:
    pretty(d)