import csv
from openpyxl import load_workbook


def complaintLodge(mno,akey,uid):
    # hello = [[mno,akey,uid]]
    #
    # print mno,akey,uid
    # with open('userdata.xlsx', 'a') as testfile:
    #     csv_writer = csv.writer(testfile)
    #     csv_writer.writerow(hello[0])

    wb = load_workbook('userdata.xlsx')
    sheet = wb.get_sheet_by_name('Sheet1')

    sheet.append([str(mno),akey,str(uid)])

    wb.save('userdata.xlsx')

complaintLodge(89515,"EAAJHwKVZCbFwBAPhBWBudp52uexyEZCksY5JRDWqz30TZCUX85NVOYcvZC6CP2bI57kAltfjBuDN2BCr0p6mhfEasPfKlORrAL4ZCXHf0C5DtOp1ZBMGKkryNa03lb95ZAZCsDhma0vp9mYdjZAD8r98lV0qUqZC7ZBhwClr9ZAHRZADZBwgZDZD",1272501602763539)