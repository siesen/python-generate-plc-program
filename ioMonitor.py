# -*- coding: utf-8 -*-
import pickle
import openpyxl
#create IO monitor
def ioMonitor(ws3,plcpath):
    try:
        inMax=inMin=int(float(ws3['A2'].value[1:]))
        outMax=outMin=int(float(ws3['E2'].value[1:]))
    except:
        return 0
    #get max min inputByte
    for row in ws3.values:
        if row[0]:
            if row[0].startswith('I'):
                temp=int(float(row[0][1:]))
                if inMax<temp:
                    inMax=temp
                if inMin>temp:
                    inMin=temp                
    #get max min outputByte
    for row in ws3.values:
        if row[4]:
            if row[4].startswith('Q'):
                temp=int(float(row[4][1:]))
                if outMax<temp:
                    outMax=temp
                if outMin>temp:
                    outMin=temp
    #get inByte
    inByte=''
    for row in ws3.values:
        if row[0]:
            if row[0].startswith('I'):
                temp=str(int(float(row[0][1:])))
                if inByte.find(temp)==-1:
                    inByte=inByte+temp+','
    #get outByte
    outByte=''
    for row in ws3.values:
        if row[4]:
            if row[4].startswith('Q'):
                temp=str(int(float(row[4][1:])))
                if outByte.find(temp)==-1:
                    outByte=outByte+temp+','
    
    #create InUdt-----------------------------------------------------------
    fo=open('In_IB.pkl','rb')
    tempstr=pickle.load(fo)
    fo.close()
    
    fo = open(plcpath+"\\In_IB.udt", "w")
    fo.write( tempstr %inMax)
    fo.close()
    
    #create OutUdt----------------------------------------------------------
    fo=open('Out_QB.pkl','rb')
    tempstr=pickle.load(fo)
    fo.close()
    
    fo = open(plcpath+"\\Out_QB.udt", "w")
    fo.write( tempstr %outMax)
    fo.close()
    
    #create IO Monitor FC---------------------------------------------------
    fo=open('IO_Monitor.pkl','rb')
    tempstr=pickle.load(fo)
    fo.close()
    
    fo = open(plcpath+"\\IO_Monitor.scl", "w")
    fo.write(tempstr %(inMin,inMax,outMin,outMax,inByte[:-1],outByte[:-1]))
    fo.close()
    
    #create IO Monitor DB--------------------------------------------------
    fo=open('IO_Monitor_DB.pkl','rb')
    tempstr=pickle.load(fo)
    fo.close()
    
    fo = open(plcpath+"\\IO_Monitor_DB.db", "w")
    fo.write(tempstr)
    fo.close()
    
    #create PLC tag---------------------------------------------------------
    wb2=openpyxl.Workbook()
    ws4=wb2.active
    ws4.title='PLC Tags'
    ws4.append(['Name','Path','Data Type','Logical Address','Comment','Hmi Visible','Hmi Accessible'])
    for row in ws3.values:
        if row[0]:
            if row[0].startswith('I'):
                ws4.append([row[1],'IO表','Bool','%'+row[0],'','True','True'])
    for row in ws3.values:
        if row[4]:
            if row[4].startswith('Q'):
                ws4.append([row[5],'IO表','Bool','%'+row[4],'','True','True'])
    ws4.append(['IB','IO表','\"In_IB\"','%I0.0','','True','True'])
    ws4.append(['QB','IO表','\"Out_QB\"','%Q0.0','','True','True'])
    wb2.save(plcpath+"\\PLCTags.xlsx")
    wb2.close()
    return 1