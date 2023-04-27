def isint(i):
  try:
    return (True,int(i))
  except:
    return (False,0)
class BoltVar:
  name = ""

  value = ""
  pytranslation = ""

  def __init__(self, name, value):
    self.name = name
    self.value = value
    intcheck=isint(self.value)
    if (intcheck[0]):
      self.type = "int"
      self.pytranslation = f'{name} = {intcheck[1]}'
   
    elif (self.value[0] == '{' and self.value[len(self.value) - 1] == '}'):
      self.type = "lst"
      self.pytranslation = f'{name} = {"".join(value).replace("{","").replace("}","").split(" ")}'
    else:
      self.type = "str"
      self.pytranslation=f'{name} = {value}'
 