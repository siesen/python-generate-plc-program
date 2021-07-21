# -*- coding: utf-8 -*-

import pickle

temp='''FUNCTION "IO_Monitor" : Void
{ S7_Optimized_Access := 'FALSE' }
VERSION : 0.1
   VAR_TEMP 
      i : Int;
      Status : Byte;
      AdrNo : Int;
   END_VAR

   VAR CONSTANT 
      InMin : Int := %d;
      InMax : Int := %d;
      OutMin : Int := %d;
      OutMax : Int := %d;
   END_VAR


BEGIN
	//turn page
	IF "IO_Monitor_DB".Button.PageUp THEN
	    "IO_Monitor_DB".Page_Num := "IO_Monitor_DB".Page_Num + 1;
	END_IF;
	IF "IO_Monitor_DB".Button.PageDown THEN
	    "IO_Monitor_DB".Page_Num := "IO_Monitor_DB".Page_Num - 1;
	END_IF;
	IF "IO_Monitor_DB".Button.SkipUp THEN
	    "IO_Monitor_DB".Page_Num := "IO_Monitor_DB".Page_Num + 5;
	END_IF;
	IF "IO_Monitor_DB".Button.SkipDown THEN
	    "IO_Monitor_DB".Page_Num := "IO_Monitor_DB".Page_Num - 5;
	END_IF;
	//transfer data
	IF NOT "IO_Monitor_DB".Button.IO_Type THEN
	    IF "IO_Monitor_DB".Page_Num < #InMin THEN
	        "IO_Monitor_DB".Page_Num := #InMax;
	    END_IF;
	    IF "IO_Monitor_DB".Page_Num > #InMax THEN
	        "IO_Monitor_DB".Page_Num := #InMin;
	    END_IF;
	    
	    CASE "IO_Monitor_DB".Page_Num OF
	        %s:
	            #AdrNo := "IO_Monitor_DB".Page_Num;
	            "IO_Monitor_DB".Button.PageUp := false;
	            "IO_Monitor_DB".Button.PageDown := false;
	            "IO_Monitor_DB".Button.SkipUp := false;
	            "IO_Monitor_DB".Button.SkipDown := false;
	    END_CASE;
	    FOR #i := 1 TO 8 BY 1 DO
	        "IO_Monitor_DB".Text[#i] := #i + 8 * #AdrNo;
	    END_FOR;
	    "IO_Monitor_DB".#Status := "IB".In[#AdrNo];
	ELSE
	    IF "IO_Monitor_DB".Page_Num < #OutMin THEN
	        "IO_Monitor_DB".Page_Num := #OutMax;
	    END_IF;
	    IF "IO_Monitor_DB".Page_Num > #OutMax THEN
	        "IO_Monitor_DB".Page_Num := #OutMin;
	    END_IF;
	    
	    CASE "IO_Monitor_DB".Page_Num OF
	        %s:
	            #AdrNo := "IO_Monitor_DB".Page_Num;
	            "IO_Monitor_DB".Button.PageUp := false;
	            "IO_Monitor_DB".Button.PageDown := false;
	            "IO_Monitor_DB".Button.SkipUp := false;
	            "IO_Monitor_DB".Button.SkipDown := false;
	    END_CASE;
	    FOR #i := 1 TO 8 BY 1 DO
	        "IO_Monitor_DB".Text[#i] := #i + 8 * #AdrNo + 5000;
	    END_FOR;
	    "IO_Monitor_DB".#Status := "QB".Out[#AdrNo];
	END_IF;
	
	    
	    
END_FUNCTION'''
fo=open('IO_Monitor.pkl','wb')
pickle.dump(temp,fo)
fo.close()


#fo=open('IO_Monitor_DB.pkl','rb')
#temp=pickle.load(fo)
#fo.close()

#fo=open('IO_Monitor_DB.db','w')
#fo.write(temp)
#fo.close()
"""
b=a=1
row=[1,1,'aaa','bbb','','Q1.0','','','T']
print([str(a),'Discrete_alarm_'+str(a),row[2]+'缩回报警'+row[6],'','Warnings','Cylinder_Error',str(b+8),'<No value>','0','<No value>','0','<No value>','False','<No value>'])
"""