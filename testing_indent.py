import textwrap

def indent_txt(data='',indent=0,char_num=4):
    
    every = 70 - indent * char_num
    spaces = char_num * indent

    data_lf = textwrap.fill(data, every)
    print(textwrap.indent(data_lf, ' ' * spaces, lambda line: True))

data = "The textwrap module provides some convenience functions, as well as TextWrapper, the class that does all the work. If you’re just wrapping or filling one or two text strings, the convenience functions should be good enough; otherwise, you should use an instance of TextWrapper for efficiency."

indent_txt(data,0,4)