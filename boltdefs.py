def isint(i):
  try:
    return (True,int(i))
  except:
    return (False,0)
class BoltLangWord:
  name=""
  
#Basic Class to hold Var Types 
class BoltVar:
  name = ""
  value = ""
  type=""
  pytranslation = ""

  def __init__(self, name, value):
    self.name = name
    self.value = value
  #given a value, determine the variable's type 
  #multiline variables are accounted for already
  def det_type(self,name,value):
    var=None
    intcheck=isint(self.value)#safe type check and translation 
    if(intcheck[0]): 
      self.type="int"
      self.pytranslation = f'{name} = {intcheck[1]}'
      var=BoltInt(name,value)
    elif(self.value[0]=='{' and self.value[-1]=='}'):
      self.type="list"
      self.pytranslation = f'{name} = {"".join(value).replace("{","").replace("}","").split(" ")}'
      var=BoltLst(name,value)
    else:
      #probably a string
      self.type="str"
      self.pytranslation=f'{name} = {value}'
    if(var==None):
      print(f"Cannot find a var type for the provided data: {name} {value}")
      return
    return var
    
      
      
      
       
    

class BoltInt(BoltVar):
   
   def __init__(self,name,value):
       super().__init__(name, value)
class BoltStr(BoltVar):
   def __init__(self,name,value):
       super().__init__(name, value)
class BoltLst(BoltVar):
   def __init__(self,name,value):
       super().__init__(name, value)
class BoltFunc(BoltVar):
    def __init__(self,name,value):
       super().__init__(name, value)

  
  
      
     

 