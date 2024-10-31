import re
tokenization=[]
class Token:
    def __init__(self, token_type, lexeme,check,line):
        self.token_type = token_type
        self.value_part = lexeme
        self.check=check
        self.line=line
        

class KeywordToken(Token):
    def __init__(self, token_type,lexeme,line):
        super().__init__(token_type, lexeme,True,line)
class ObjectCallToken(Token):
    def __init__(self, lexeme,line):
        super().__init__("OBJECT CALL", lexeme,True,line)
class IdentifierToken(Token):
    def __init__(self, lexeme,line):
        super().__init__("IDENTIFIER", lexeme,True,line)
class LexicalToken(Token):
    def __init__(self, lexeme,line):
        super().__init__("LEXICAL ERROR", lexeme,False,line)        
class IntConstantToken(Token):
    def __init__(self, lexeme,line):
        super().__init__("INT CONSTANT", lexeme,True,line) 
class FloatConstantToken(Token):
    def __init__(self, lexeme,line):
        super().__init__("FLOAT CONSTANT", lexeme,True,line) 
class StringConstantToken(Token):
    def __init__(self, lexeme,line):
        super().__init__("STRING CONSTANT", lexeme,True,line) 
class BooleanToken(Token):
    def __init__(self, lexeme,line):
        super().__init__("BOOLEAN CONSTANT", lexeme,True,line) 
'''class PunctureToken(Token):
    def __init__(self, token_type,lexeme):
        super().__init__(token_type, lexeme,True) '''
class PunctureToken(Token):
    def __init__(self, token_type,lexeme,line):
        super().__init__(token_type, lexeme,True,line)
class OperatorToken(Token):
    def __init__(self, token_type,lexeme,line):
        super().__init__(token_type, lexeme,True,line)
class DataTypeToken(Token):
    def __init__(self, lexeme,line):
        super().__init__("DATA TYPE", lexeme,True,line)                 

class checker:
    def __init__(self):
        pass
    def isDataType(self,word,line):
        DT=['int','float','string','bool'] 
        if word in DT:
            return(DataTypeToken(word,line))
        else:
            return(LexicalToken(word,line))
    def isOB_CALL(self, word,line):
        match = re.match(r'[_A-Za-z]+[_0-9A-Za-z]*(\.[_A-Za-z]+[_0-9A-Za-z]*)*$', word)
        if match:
            iden=match.group()
            return(ObjectCallToken(iden,line))
        else:
            return(LexicalToken(word,line))       
    def isID(self, word,line):
        match = re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', word)
        if match:
            iden=match.group()
            return(IdentifierToken(iden,line))
        else:
            return(LexicalToken(word,line))
    def isINT(self,word,line):
        match=re.match(r'^[+|-]?[0-9]+$',word)
        if match:
            iden=match.group()
            return(IntConstantToken(iden,line))
        else:
            return(LexicalToken(word,line))
    def isFLOAT(self,word,line):
        match=re.match(r'^[+|-]?([0-9]+\.([0-9]*)?|(\.[0-9]+))$',word)
        if match:
            iden=match.group()
            return(FloatConstantToken(iden,line))
        else:
            return(LexicalToken(word,line))   
    def isSTRING(self,word,line):
        match=re.match(r"^(['\"])(.*?)(?<!\\)\1$",word)
        if match:
            iden=match.group()
            return(StringConstantToken(iden,line))
        else:
            return(LexicalToken(word,line))
    def isBOOLEAN(self,word,line):
        match=re.match(r"^(True|False)$" ,word)
        if match:
            iden=match.group()
            return(BooleanToken(iden,line))
        else:
            return(LexicalToken(word,line))  
    def isKEYWORD(self,word,line):
        key=['self','staticmethod','and','or','class','len','def','if','elif','else','break','continue','pass','for','not','return','is','in','while','import','from','try','exception','as','range','except','finally','print',] 
        if word in key:
            return(KeywordToken(word.upper(),word,line))
        else:
            return(LexicalToken(word,line))   
    def isPUNCT(self,word,line):
        punct=['(',')','{','}','[',']',',',';',':','.'] 
        if word in punct:
            return(PunctureToken(word,word,line))
        else:
            return(LexicalToken(word,line))
    def isOPER(self,word,line):
        oper=['++','--','&','|','**','*','/','+','-','<','>','<=','>=','!=','==','=','+=','-=','*=','/=']
        if word in oper:
            if (word=='++') or (word=='--'):
                return(OperatorToken(word,word,line))
            if(word=='+=') or (word=='-=') or (word=='*=') or (word=='/='):
                return(OperatorToken(word,word,line))
            if(word=='&') or (word=='|') :
                return(OperatorToken(word,word,line))
            if (word=='**'):
                return(OperatorToken(word,word,line)) 
            if (word=='='):
                return(OperatorToken(word,word,line))
            if (word=='*') or (word=='/'):
                return(OperatorToken(word,word,line))
            if (word=='+') or (word=='-'):
                return(OperatorToken(word,word,line)) 
            if (word=='<') or (word=='>') or (word=='<=') or (word=='>=') or (word=='!=') or (word=='=='):
                return(OperatorToken(word,word,line))
        else:
            return(LexicalToken(word,line))      

'''c=checker()
res=c.isID('2xyz')
res1=c.isINT('-788')
res2=c.isFLOAT('-.5')
res3=c.isSTRING('"ehfwfwfwhf/.wfe/\wfef''%32737$"')
res4=c.isBOOLEAN('True')
res5=c.isKEYWORD('for')
res6=c.isPUNCT('}')
res7=c.isOPER('>=')
print(res.token_type,res.value_part,res1.token_type,res1.value_part,res2.token_type,res2.value_part,res3.token_type,res3.value_part,res4.token_type,res4.value_part,res5.token_type,res5.value_part,res6.token_type,res6.value_part,res7.token_type,res7.value_part)'''
class Lexer:
    def __init__(self, input_text):
        self.input_text = input_text
        self.position = 0
        self.tokens = []
        self.temp=''
        self.quote=[]
        self.punct=['(',')','{','}','[',']',',',';',':']
        self.line_number = 1  # Initialize line number
        self.line_check=False
        self.comments=[]

    def scan(self):
        self.line_check=False
        while self.position < len(self.input_text):
            self.line_check=False
            if (self.input_text[self.position] !='"') and len(self.quote)<=0:
                if (self.input_text[self.position] != ' ') and (self.input_text[self.position] != '\n'):
                    if(self.input_text[self.position] in self.punct):
                        if self.temp:  # Check if temp is not empty before appending
                            self.tokens.append(self.temp)
                            self.tokens.append(self.line_number)
                            self.temp = ''
                            #print('pun',self.line_number,self.input_text[self.position])
                            if (self.position+1==len(self.input_text)):
                                break
                            #if (self.input_text[self.position+1] == '\n'):
                                #print('pun',self.line_number,self.input_text[self.position-1])
                             #   self.line_number=self.line_number+1
                              #  self.line_check=True
                            
                    if(self.input_text[self.position] =='='):
                        if self.temp:  # Check if temp is not empty before appending
                            self.tokens.append(self.temp)
                            self.tokens.append(self.line_number)
                            self.temp = ''
                    if(self.input_text[self.position] =='+'):
                        if self.temp:  # Check if temp is not empty before appending
                            self.tokens.append(self.temp)
                            self.tokens.append(self.line_number)
                            self.temp = ''
                    if(self.input_text[self.position] =='-'):
                        if self.temp:  # Check if temp is not empty before appending
                            self.tokens.append(self.temp)
                            self.tokens.append(self.line_number)
                            self.temp = '' 
                    if(self.input_text[self.position] =='*'):
                        if self.temp:  # Check if temp is not empty before appending
                            self.tokens.append(self.temp)
                            self.tokens.append(self.line_number)
                            self.temp = ''
                    if(self.input_text[self.position] =='/'):
                        if self.temp:  # Check if temp is not empty before appending
                            self.tokens.append(self.temp)
                            self.tokens.append(self.line_number)
                            self.temp = ''        
                    if(self.input_text[self.position] =='<'):
                        if self.temp:  # Check if temp is not empty before appending
                            self.tokens.append(self.temp)
                            self.tokens.append(self.line_number)
                            self.temp = ''
                    if(self.input_text[self.position] =='>'):
                        if self.temp:  # Check if temp is not empty before appending
                            self.tokens.append(self.temp)
                            self.tokens.append(self.line_number)
                            self.temp = ''
                    if(self.input_text[self.position] =='!'):
                        if self.temp:  # Check if temp is not empty before appending
                            self.tokens.append(self.temp)
                            self.tokens.append(self.line_number)
                            self.temp = ''
                    if(self.input_text[self.position] =='&'):
                        if self.temp:  # Check if temp is not empty before appending
                            self.tokens.append(self.temp)
                            self.tokens.append(self.line_number)
                            self.temp = '' 
                    if(self.input_text[self.position] =='|'):
                        if self.temp:  # Check if temp is not empty before appending
                            self.tokens.append(self.temp)
                            self.tokens.append(self.line_number)
                            self.temp = ''                                

                    self.temp = self.temp + self.input_text[self.position]
                    self.position = self.position + 1
                    if(self.position==len(self.input_text)):
                        break
                    if(self.input_text[self.position]=='.'):
                        match=re.match(r'[0-9]*',self.temp)
                        if match==True:
                            self.temp=self.temp+self.input_text[self.position]
                            self.position=self.position+1
                            while(re.match(r'[0-9]',self.input_text[self.position])):
                                #print('while self position',self.position,self.input_text[self.position],len(self.input_text))
                                self.temp=self.temp+self.input_text[self.position]
                                self.position=self.position+1
                                if (self.position==len(self.input_text)):
                                    break
                            else:
                                if self.temp:  # Check if temp is not empty before appending
                                    self.tokens.append(self.temp)
                                    self.tokens.append(self.line_number)
                                    self.temp = '' 
                        else:
                            if self.temp=='':
                                if self.temp:  # Check if temp is not empty before appending
                                    self.tokens.append(self.temp)
                                    self.tokens.append(self.line_number)
                                    self.temp = ''
                                self.temp=self.temp+self.input_text[self.position]
                                self.position=self.position+1
                                while(re.match(r'[0-9]',self.input_text[self.position])):
                                    #print('while self position',self.position,self.input_text[self.position],len(self.input_text))
                                    self.temp=self.temp+self.input_text[self.position]
                                    self.position=self.position+1
                                    if (self.position==len(self.input_text)):
                                        break              
                    '''if(self.input_text[self.position]=='.'):
                        match=re.match(r'[_A-Za-z]+[_0-9A-Za-z]*(\.[_A-Za-z]+[_0-9A-Za-z]*)$',self.temp)
                        print(self.input_text[self.position],self.temp)
                        if match is not None:
                            self.temp=self.temp+self.input_text[self.position]
                            self.position=self.position+1
                            #print(self.input_text[self.position])
                            while(re.match(r'[_A-Za-z0-9]',self.input_text[self.position])):
                                print('while self position',self.position,self.input_text[self.position],len(self.input_text))
                                if(self.input_text[self.position-1]=='.'):
                                    if(re.match(r'[0-9]',self.input_text[self.position])):
                                        if self.temp:  # Check if temp is not empty before appending
                                            self.tokens.append(self.temp)
                                            self.tokens.append(self.line_number)
                                            self.temp = ''
                                    else:
                                        print(self.temp[-1],' .')
                                        self.temp=self.temp+self.input_text[self.position]
                                        self.position=self.position+1
                                        if (self.position==len(self.input_text)):
                                            break       
                                else:
                                    print(self.temp[-1])
                                    self.temp=self.temp+self.input_text[self.position]
                                    self.position=self.position+1
                                    if (self.position==len(self.input_text)):
                                        break  
                            else:
                                if self.temp:  # Check if temp is not empty before appending
                                    self.tokens.append(self.temp)
                                    self.tokens.append(self.line_number)
                                    self.temp = '''
                    if(self.temp in self.punct):
                        if self.temp:  # Check if temp is not empty before appending
                            self.tokens.append(self.temp)
                            #print('down punc',self.line_number,self.input_text[self.position])    
                            self.temp = ''
                            if (self.input_text[self.position+1] == '\n'):
                                #print('down punc 1',self.line_number,self.input_text[self.position+1])
                                self.line_number=self.line_number+1
                                self.line_check=True
                                #print('temp',self.temp)
                            if (self.input_text[self.position] == '\n'):
                                #print('down punc 1',self.line_number,self.input_text[self.position+1])
                                self.line_number=self.line_number+1
                                self.line_check=True
                                #print('temp',self.temp)    
                            #self.tokens.append(self.line_number-1)    
                            if self.line_check:
                                self.tokens.append(self.line_number-1)
                            else:
                                self.tokens.append(self.line_number)   
                            
                    if(self.temp=='='):
                        if(self.input_text[self.position] =='='):
                            self.temp = self.temp + self.input_text[self.position]
                            self.position = self.position + 1
                            if self.temp:  # Check if temp is not empty before appending
                                self.tokens.append(self.temp)
                                self.tokens.append(self.line_number)
                                self.temp = ''
                                if (self.input_text[self.position] == '\n'):
                                    self.line_number =self.line_number+ 1
                        else:
                            if self.temp:  # Check if temp is not empty before appending
                                self.tokens.append(self.temp)
                                self.tokens.append(self.line_number)
                                self.temp = ''
                                if (self.input_text[self.position] == '\n'):
                                    self.line_number =self.line_number+ 1
                    if(self.temp=='/'):
                        if(self.input_text[self.position] =='='):
                            self.temp = self.temp + self.input_text[self.position]
                            self.position = self.position + 1
                            if self.temp:  # Check if temp is not empty before appending
                                self.tokens.append(self.temp)
                                self.tokens.append(self.line_number)
                                self.temp = ''
                                if (self.input_text[self.position] == '\n'):
                                    self.line_number =self.line_number+ 1
                        else:
                            if self.temp:  # Check if temp is not empty before appending
                                self.tokens.append(self.temp)
                                self.tokens.append(self.line_number)
                                self.temp = ''
                                if (self.input_text[self.position] == '\n'):
                                    self.line_number =self.line_number+ 1            
                    if(self.temp=='+'):
                        if(self.input_text[self.position] =='+') or (self.input_text[self.position]=='='):
                            self.temp = self.temp + self.input_text[self.position]
                            self.position = self.position + 1
                            if self.temp:  # Check if temp is not empty before appending
                                self.tokens.append(self.temp)
                                self.tokens.append(self.line_number)
                                self.temp = ''
                                if (self.input_text[self.position] == '\n'):
                                    self.line_number =self.line_number+ 1
                        else:
                            if self.temp:  # Check if temp is not empty before appending
                                self.tokens.append(self.temp)
                                self.tokens.append(self.line_number)
                                self.temp = ''
                                if (self.input_text[self.position] == '\n'):
                                    self.line_number =self.line_number+ 1 
        
                    if(self.temp=='-'):
                        if(self.input_text[self.position] =='-') or (self.input_text[self.position]=='='):
                            self.temp = self.temp + self.input_text[self.position]
                            self.position = self.position + 1
                            if self.temp:  # Check if temp is not empty before appending``
                                self.tokens.append(self.temp)
                                self.tokens.append(self.line_number)
                                self.temp = ''
                                if (self.input_text[self.position] == '\n'):
                                    self.line_number =self.line_number+ 1
                        else:
                            if self.temp:  # Check if temp is not empty before appending
                                self.tokens.append(self.temp)
                                self.tokens.append(self.line_number)
                                self.temp = ''
                                if (self.input_text[self.position] == '\n'):
                                    self.line_number =self.line_number+ 1
                    if(self.temp=='*'):
                        if(self.input_text[self.position] =='*') or (self.input_text[self.position]=='='):
                            self.temp = self.temp + self.input_text[self.position]
                            self.position = self.position + 1
                            if self.temp:  # Check if temp is not empty before appending
                                self.tokens.append(self.temp)
                                self.tokens.append(self.line_number)
                                self.temp = ''
                                if (self.input_text[self.position] == '\n'):
                                    self.line_number =self.line_number+ 1
                        else:
                            if self.temp:  # Check if temp is not empty before appending
                                self.tokens.append(self.temp)
                                self.tokens.append(self.line_number)
                                self.temp = ''
                                if (self.input_text[self.position] == '\n'):
                                    self.line_number =self.line_number+ 1  
                    if(self.temp=='<'):
                        if(self.input_text[self.position]=='='):
                            self.temp = self.temp + self.input_text[self.position]
                            self.position = self.position + 1
                            if self.temp:  # Check if temp is not empty before appending
                                self.tokens.append(self.temp)
                                self.tokens.append(self.line_number)
                                self.temp = ''
                                if (self.input_text[self.position] == '\n'):
                                    self.line_number =self.line_number+ 1
                        else:
                            if self.temp:  # Check if temp is not empty before appending
                                self.tokens.append(self.temp)
                                self.tokens.append(self.line_number)
                                self.temp = ''
                                if (self.input_text[self.position] == '\n'):
                                    self.line_number =self.line_number+ 1
                    if(self.temp=='>'):
                        if(self.input_text[self.position]=='='):
                            self.temp = self.temp + self.input_text[self.position]
                            self.position = self.position + 1
                            if self.temp:  # Check if temp is not empty before appending
                                self.tokens.append(self.temp)
                                self.tokens.append(self.line_number)
                                self.temp = ''
                                if (self.input_text[self.position] == '\n'):
                                    self.line_number =self.line_number+ 1
                        else:
                            if self.temp:  # Check if temp is not empty before appending
                                self.tokens.append(self.temp)
                                self.tokens.append(self.line_number)
                                self.temp = ''
                                if (self.input_text[self.position] == '\n'):
                                    self.line_number =self.line_number+ 1  
                    if(self.temp=='!'):
                        if(self.input_text[self.position] =='='):
                            self.temp = self.temp + self.input_text[self.position]
                            self.position = self.position + 1
                            if self.temp:  # Check if temp is not empty before appending
                                self.tokens.append(self.temp)
                                self.tokens.append(self.line_number)
                                self.temp = ''
                                if (self.input_text[self.position] == '\n'):
                                    self.line_number =self.line_number+ 1
                    if(self.temp=='&'):
                        if self.temp:
                            self.tokens.append(self.temp)
                            self.tokens.append(self.line_number)
                            self.temp=''
                            if (self.input_text[self.position] == '\n'):
                                self.line_number =self.line_number+ 1
                    if(self.temp=='|'):
                        if self.temp:
                            self.tokens.append(self.temp)
                            self.tokens.append(self.line_number)
                            self.temp=''
                            if (self.input_text[self.position] == '\n'):
                                self.line_number =self.line_number+ 1                                                                  
                                                                      
                else:
                    if self.temp:  # Check if temp is not empty before appending
                        self.tokens.append(self.temp)
                        self.tokens.append(self.line_number)
                        self.temp = ''
                        if (self.input_text[self.position] == '\n'):
                            #print(self.line_number,self.input_text[self.position-1])
                            self.line_number =self.line_number+ 1
                            
                    self.position = self.position + 1        
                # print(self.position,self.input_text[self.position])
            else:
                #  print('else ',self.position)
                if (self.input_text[self.position] !='"'):
                    if(self.input_text[self.position] == "\\"):
                        self.temp = self.temp + self.input_text[self.position]
                        self.position = self.position + 1
                        self.temp = self.temp + self.input_text[self.position]
                        self.position = self.position + 1
                    else:    
                        self.temp = self.temp + self.input_text[self.position]
                        self.position = self.position + 1
                else:                                
                    self.temp = self.temp + self.input_text[self.position]
                
                    if(len(self.quote)>0):
                        self.quote.pop()
                        if self.temp:
                            self.tokens.append(self.temp)
                            self.tokens.append(self.line_number)
                            self.temp = ''
                        if (self.input_text[self.position+1] == '\n'):
                            #print(self.line_number,self.input_text[self.position-1])
                            self.line_number =self.line_number+ 1
                    else:
                        self.quote.append(self.input_text[self.position])
                    self.position=self.position+1
             
            
                 

        # Append the last word after the loop
        if self.temp:
            self.tokens.append(self.temp)
            self.tokens.append(self.line_number)
            self.temp = ''

        #print(self.tokens, self.position, self.input_text)

        return self.tokens


def switch_case(case,line):
    check=checker()
    toke=[]
    if (re.match(r'_|[a-zA-Z]',case[0])) :
        dt=check.isDataType(case,line)
        id=check.isID(case,line)
        ky=check.isKEYWORD(case,line)
        ob=check.isOB_CALL(case,line)
        if(id.check==True)and(ky.check==True):
            toke.append(ky.token_type)
            toke.append(ky.value_part)
            toke.append(ky.line)
            return toke
        
        elif(id.check==True)and(dt.check==True):
            toke.append(dt.token_type)
            toke.append(dt.value_part)
            toke.append(dt.line)
            return toke
        
        else:
            bol=check.isBOOLEAN(case,line)
            if(bol.check==True):
                toke.append(bol.token_type)
                toke.append(bol.value_part)
                toke.append(bol.line)
                return toke
            elif(id.check==True):
                toke.append(id.token_type)
                toke.append(id.value_part)
                toke.append(id.line)
                return toke
            else:
                toke.append(ob.token_type)
                toke.append(ob.value_part)
                toke.append(ob.line)
                return toke
            
    elif case[0]=='"' or case[0]=="'":
        string=check.isSTRING(case,line)
        toke.append(string.token_type)
        toke.append(string.value_part)
        toke.append(string.line)
        return toke
    elif (case[0] == '+') or (case[0]=='-') or (case[0]=='&') or (case[0]=='|') or (case[0]=='*') or (case[0]=='/') or (case[0]=='<') or (case[0]=='>') or (case[0]=='!') or (case[0]=='='):
        oper=check.isOPER(case,line)
        toke.append(oper.token_type)
        toke.append(oper.value_part)
        toke.append(oper.line)
        return toke
    elif (case[0] == '(') or (case[0]==')') or (case[0]=='{') or (case[0]=='}') or (case[0]=='[') or (case[0]==']') or (case[0]==':') or (case[0]==';') or (case[0]==',') :
        punct=check.isPUNCT(case,line)
        toke.append(punct.token_type)
        toke.append(punct.value_part)
        toke.append(punct.line)
        return toke
    elif (re.match(r'.|[0-9]',case[0])):
        integ=check.isINT(case,line)
        flt=check.isFLOAT(case,line)
        if(integ.check==True) or (flt.check==True):
            if(integ.check==True):
                toke.append(integ.token_type)
                toke.append(integ.value_part)
                toke.append(integ.line)
                return toke
            else:
                toke.append(flt.token_type)
                toke.append(flt.value_part)
                toke.append(flt.line)
                return toke
        else:
            toke.append(integ.token_type)
            toke.append(integ.value_part)
            toke.append(integ.line)
            return toke
     
    else:
        return (LexicalToken(case,line))



input_code = open(r'C:\Users\hpint\OneDrive\Desktop\javeriya CC\lexicalread.py','r')
lexer = Lexer(input_code.read())
tokens = lexer.scan()
#print(tokens)
for i in range(0,len(tokens),2): 
    #print(tokens[i+1],tokens[i],len(tokens))
    val=switch_case(tokens[i],tokens[i+1])
    #val[1]=val[1]+"#"
    #print(val)
    tokenization.append(val)
    
print(tokenization,type (tokenization))   
with open("list.txt", "w") as my_file:
    for item in tokenization:
        line = " ".join(map(str, item)) + "\n"
        my_file.write(line)
