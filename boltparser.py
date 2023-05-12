import boltdefs
import re
class ParserInstance:
    text=""
    vars=[]
    nonvars=[]
    def __init__(self):
        pass
        
        
        
    def parse(self, text):
        
        lines = text.splitlines()
        #print(f"PARSING STARTING ON {lines}")
        var_regex = '.*=.*'
        need_next_line = False

        for line in lines:
            #print(f"PARSING {line}")
            if re.match(var_regex, line):
                splitted = line.split("=")
                var = boltdefs.BoltVar(splitted[0], splitted[1])
                
                self.vars.append(var)
            else:
                self.nonvars.append(line)
                
            print(f"vars {self.vars} nonvars{self.nonvars}")


        

