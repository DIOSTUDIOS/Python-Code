from openpyxl import Workbook
from datetime import datetime
from openpyxl.utils import FORMULAE


wb = Workbook()
# print(wb.active)

# wb["Sheet"]["E3"] = "python"

for col in range(1, 10):
	for row in range(1, 10):
		wb["Sheet"].cell(column=col, row=row, value=(col + row))

# print(wb["Sheet"]["A9"].value)
# print(wb["Sheet"]["A9"].column)
# print(wb["Sheet"]["A9"].row)

# wb.copy_worksheet(wb["Sheet"])
# 
# for cell in wb["Sheet"]["A1:A9"]:
# print(wb["Sheet"]["A1:C9"])
	# print(cell)
	# print(cell[0].value)
# print("SUM" in FORMULAE)
wb["Sheet"]["A1"].value = datetime.now()
print(wb["Sheet"]["A1"].number_format)
wb["Sheet"]["A9"].value = "python"
print(wb["Sheet"]["A9"].number_format)
# wb["Sheet"]["J1"].value = "=SAM(A1:A)"

wb.save(filename="example.xlsx")