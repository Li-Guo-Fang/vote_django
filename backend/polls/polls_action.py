import xlwt
from io import BytesIO

def get_style(name,color=0,bold=False,italic=False):
    font = xlwt.Font()
    font.name,font.colour_index,font.bold,font.italic =  name,color,bold,italic
    style = xlwt.XFStyle()
    style.font = font
    return style







