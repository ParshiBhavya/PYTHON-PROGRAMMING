#To open excel sheet
import xlrd
loc=("C:\\Users\\parsi\\OneDrive\\Desktop\\Book1.xls")
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)

#To read cell value
print(sheet.cell_value(0,0))

#To extract no of rows and coloums in sheet
print(sheet.ncols)
print(sheet.nrows)

#To extract coloumn names and row names
for i in range(sheet.ncols):
    print(sheet.cell_value(0,i))
    print(sheet.cell_value(i,0))

#To extract row values and coloumn values
print(sheet.row_values(1))
print(sheet.col_values(2))



