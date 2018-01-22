from xlrd import open_workbook
import xlwt
from  xlutils.copy import copy
"""
wb = xlrd.open_workbook("D:\\Autotest\\data\\RanzhiAutoCases.xlsx")
wb.sheet_names()
sh = wb.sheet_by_name("login")
for rownum in range(sh.nrows):
    print(sh.row_values(rownum))

first_column = sh.col_values(0)
print(first_column)
cell_A1 = sh.cell(0,0).value
print(cell_A1)
cell_C4 = sh.cell(3,4).value
print(cell_C4)



new = xlwt.Workbook()
sheet = new.add_sheet("me")
sheet.write(0,1,"test test")
sheet.write(0,2,"djfjd")
new.save("C:\\Users\\Administrator\\Desktop\\test.xls")

"""
rb = open_workbook("C:\\Users\\Administrator\\Desktop\\test.xls")

#rs = rb.sheet_by_name("me")

wb = copy(rb)

ws = wb.get_sheet(0)
ws.write(0,5,"changes")
wb.save("C:\\Users\\Administrator\\Desktop\\test.xls")
