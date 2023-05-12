import sys
import subprocess
import boltparser

def intrepter():
   parser=boltparser.ParserInstance()
   dontexit=True
   print("Bolt V1 by Gunnar Funderburk")
   while dontexit:
     line=input(">>>")
     if(line=="exit"):
       
       sys.exit(0)
    
     parser.parse(line)

if(sys.argv):
 if(sys.argv[1]=="interpreter"):
  #run interpreter

  
  intrepter()

  

   
   