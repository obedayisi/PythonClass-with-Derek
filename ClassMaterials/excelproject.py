import openpyxl
path = "C:/Users/ayitobed/Desktop/PythonClass-with-Derek/ClassMaterials/gfg.xlsx"
wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active
cell_obj = sheet_obj.cell(row = 1, column = 1)
print(cell_obj.value)