# -*- coding: utf-8 -*-

import openpyxl

def hmiFile(ws3,hmipath):
    #create HMITextLists-----------------------------------------------------
    #sheet1 textlist
    wb3=openpyxl.Workbook()
    ws5=wb3.active
    ws5.title='TextList'
    row=['Name','ListRange','Comment [zh-CN]','Comment [en-US]']
    ws5.append(row)
    row =['IO_Type','IO_Num','IO_Text']
    for a in range(3):
        ws5.append([row[a],'Decimal','<No value>','<No value>'])
        
    #sheet2 TextListEntry
    ws6=wb3.create_sheet('TextListEntry')
    row=['Name','Parent','DefaultEntry','Value','Text [zh-CN]','Text [en-US]','FieldInfos']
    ws6.append(row)

    #IO Monitor-------------------------------------------------------------
    ws6.append(['Text_list_entry_1','IO_Type','',str(0),'输入','Input'])
    ws6.append(['Text_list_entry_2','IO_Type','',str(1),'输出','Output'])
    #IO Number-------------------------------------------------------------------
    a=1
    #Input
    for row in ws3.values:
        if row[0]:
            if row[0].startswith('I'):
                b=int(float(row[0][1:]))*8+int(row[0][-1])+1
                ws6.append(['Text_list_entry_'+str(a),'IO_Num','',str(b),row[0],row[0]])
                a+=1
    #Output
    for row in ws3.values:
        if row[4]:
            if row[4].startswith('Q'):
                b=int(float(row[4][1:]))*8+int(row[4][-1])+5001
                ws6.append(['Text_list_entry_'+str(a),'IO_Num','',str(b),row[4],row[4]])
                a+=1
    #IO Text----------------------------------------------------------------
    a=1
    #Input
    for row in ws3.values:
        if row[0]:
            if row[0].startswith('I'):
                b=int(float(row[0][1:]))*8+int(row[0][-1])+1
                ws6.append(['Text_list_entry_'+str(a),'IO_Text','',str(b),row[1],row[2]])
                a+=1
    #Output
    for row in ws3.values:
        if row[4]:
            if row[4].startswith('Q'):
                b=int(float(row[4][1:]))*8+int(row[4][-1])+5001
                ws6.append(['Text_list_entry_'+str(a),'IO_Text','',str(b),row[5],row[6]])
                a+=1
                
    wb3.save(hmipath+"\\HMITextLists.xlsx")
    wb3.close()
