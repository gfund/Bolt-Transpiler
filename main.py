import re
from boltdefs import BoltVar,isint
vars=[]
def boltparse(filename:str):
  varregex='.*=.*'
  neednextline=False
  if(filename[len(filename)-3:len(filename)]==".bv"): #file signature
   
   file=open(f"{filename}","r")
   lines=file.readlines()
   for line in lines:
     line=line.strip()
     if(isint(line[0]) and  vars[len(vars)-1]==):
       
   

     if(not neednextline):
      if(re.match(varregex,line)):
       splitted=line.split("=")
       var=BoltVar(splitted[0],splitted[1])
       
       if(splitted[1][0]=="'"):
          neednextline=True
        
        
       vars.append(var)
     else:
       
        newval=vars[len(vars)-1].value+line
        vars[len(vars)-1].value=newval.replace("'","")
        vars[len(vars)-1].pytranslation=newval
        
        neednextline=False
     
boltparse('main.bv')
for b in vars:
  print(f"TYPE {b.type} {b.name}={b.value} PY---> {b.pytranslation}")
  