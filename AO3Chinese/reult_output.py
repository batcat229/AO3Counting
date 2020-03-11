from one_page import counts
import xlsxwriter

workbook = xlsxwriter.Workbook('raw_result.xlsx')
worksheet=workbook.add_worksheet()
row=2
column=2
#rating code#
no_rated='9'
General='10'
Teen='11'
Mature='12'
Explicit='13'
rate_list=[no_rated, General, Teen, Mature, Explicit]

#language setting
zh='zh'
en=''

n=310 #begin date

#chinese loop
#while(n>0):
#    day=str(n)
#    date='%3E+'+day+'+days'
#    worksheet.write(row, column, day)
#    row+=1
#    for i in range(len(rate_list)):
#        result=counts(zh,date,rate_list[i])
#        worksheet.write(row, column, result)
#        row+=1
#        print(n)
#        
#    column=column+1
#    row=2
#    n=n-30

#all language loop
row=10
n=310
column=2
while(n>309):
    day=str(n)
    date='%3E+'+day+'+days'
    worksheet.write(row, column, day)
    row+=1
    for i in range(len(rate_list)):
        result=counts(en,date,rate_list[i])
        worksheet.write(row, column, result)
        row+=1
        print(n)
        
    column=column+1
    row=10
    n=n-30

workbook.close()

print("finish")