import openpyxl
titleList = []
wb = openpyxl.load_workbook('sampleInput.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
sheet.columns[1]
i = 0
for cellObj in sheet.columns[1]:
		if cellObj.value not in titleList:
			titleList.append(cellObj.value)
			i = i + 1
			wb.create_sheet(index=i, title=cellObj.value)
		else:
			print("hello World")
        
wb.save('sampleInput.xlsx')
print(titleList)