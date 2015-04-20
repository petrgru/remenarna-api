__author__ = 'petrg'
import openpyxl
def getdata_vskprofi(file):
    workbook = openpyxl.load_workbook(filename = file, use_iterators = True)
    worksheet = workbook.get_sheet_by_name('List1')
    d=[]
    for row in worksheet.iter_rows():
        if row[0].row > 4 :
            data = {
                'UID':  row[0].value, # Column A
                'order_number': row[1].value, # Column B
                'ShortName':  row[2].value, # Column C
                'groups':  row[3].value, # Column C
                'Prices':  row[4].value, # Column C
                'UnitType':  row[5].value, # Column C
                'Description':  row[6].value, # Column C
            }
            d.append(data)
            #print data['my_first_col'], '::', data['my_second_col'], '::', data['my_third_col']
    return d

#print getdata_vskprofi('../uploads/cenik-2015-04-kompletni-pc-czk.xlsx')