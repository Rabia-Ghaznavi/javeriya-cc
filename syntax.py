count=0
def DEC():
    global count
    if(val[count][0]=='IDENTIFIER'):
        count+=1
        if(INIT()):
            return True
        
    return False

def INIT():
    global count
    return False    

def F_13():
    global count
    if(val[count][0]=='['):
        if(LIST()):
            count+=1
            if (val[count][0]==';'):
                return True
    elif(val[count][0]=='{'):
        if(DICTIONARY()):
            count+=1
            if (val[count][0]==';'):
                return True
    if(val[count][0]=='IDENTIFIER'):
        if(OBJECT_CREATE()):
            count+=1
            if (val[count][0]==';'):
                return True 

    return False

def MST():
    global count
    if(val[count][0]=='FOR') or (val[count][0]=='IF') or (val[count][0]=='TRY') or (val[count][0]=='DATA TYPE') or (val[count][0]=='IDENTIFIER'):
        if(SST()):
            #print('for true','mst')
            count+=1
            if(MST()):
                return True
    elif(val[count][0]=='}'):
        return True

    return False            

def OBJECT_CREATE():
    global count
    if(val[count][0]=='IDENTIFIER'):
            count+=1
            #print('inj')
            if(val[count][0]=='('):
                count+=1
                
                if(ARGUMENTS()):
                    if(val[count][0]==')'):
                        #print(val[count][0])
                        return True

    return False


def ARGUMENTS():
    global count
    if (val[count][0]=='IDENTIFIER') or (val[count][0]=='INT CONSTANT') or (val[count][0]=='STRING CONSTANT') or (val[count][0]=='FLOAT CONSTANT') or (val[count][0]=='BOOLEAN CONSTANT'):
        if(expression()):
            return True
    elif(val[count][0]==')'):
        return True
    
    return False   

def CLASS():
    global count
    if(val[count][0]=='CLASS'):
        count+=1
        if(val[count][0]=='IDENTIFIER'):
            count+=1
            #print('yes')
            if(F_4()):
            
                return True 

    return False

def F_4():
    global count
    if(val[count][0]=='{') :
        if(CLASS_DEF()):
            return True
    elif(val[count][0]=='('):
        count+=1
        if(BASE_CLASSES()):
            if(val[count][0]==')'):
                count+=1
                #print('d')
                if(CLASS_DEF()):
                    return True
    return False                       

def BASE_CLASSES():
    global count
    if(val[count][0]=='IDENTIFIER'):
        count+=1
        if(F_5()):
            return True
    
    return False 

def F_5():
    global count
    if(val[count][0]==','):
        count+=1
        if(val[count][0]=='IDENTIFIER'):
            count+=1
            if(F_5()):
                return True
    elif(val[count][0]==')'):#null remove
        return True

    return False 

def CLASS_DEF():
    global count
    if(val[count][0]=='{'):
        count+=1
        if (CLASS_BODY()):
            
            if(val[count][0]=='}'):
                count+=1
                return True

    return False

def CLASS_FUN():
    global count
    if (val[count][0]=='DEF'):
        count+=1
        if (val[count][0]=='IDENTIFIER'):
            count+=1
            if(val[count][0]=='('):
                count+=1
                if(val[count][0]=='SELF'):
                    count+=1
                    #print(val[count][0],'self')
                    if (PARA()):
                        if(val[count][0]==')'):
                            count+=1
                            #print(val[count][0],'self')
                            if(BODY()):
                                return True
    elif(val[count][0]=='@'):
        count+=1
        if(val[count][0]=='staticmethod'):
            count+=1
            if(FUNC_DEF()):
                return True
    return False

def PARA():
    global count
    if(val[count][0]==','):
        count+=1
        if(val[count][0]=='IDENTIFIER'):
            count+=1
            #print(val[count][0],'self1',val[count-1][1])
            if (PARA()):
                #print(val[count][0],'self1',val[count-1][1])
                return  True                         

    elif(val[count][0]==')'):#remove null 
        return True

    return False                                

def CONSTRUCTOR():
    global count
    if (val[count][0]=='DEF'):
        count+=1
        if(val[count][0]=='__init__'):
            count+=1
            if(val[count][0]=='('):
                count+=1
                if(val[count][0]=='SELF'):
                    count+=1
                    if (PARA()):
                        if(val[count][0]==')'):
                            count+=1
                            if(val[count][0]=='{'):
                                count+=1
                                if(CLASS_BODY()):
                                    
                                    if(val[count][0]=='}'):
                                        count+=1
                                        return True
                                    
    return False  


'''def CONSTRUCTOR_BODY():
    global count
    if(val[count][0]=='FOR') or (val[count][0]=='IF') or (val[count][0]=='TRY') or (val[count][0]=='DATA TYPE') or (val[count][0]=='IDENTIFIER') :
        count+=1
        if(CLASS_BODY()):
            return True
        
    elif(val[count][0]=='self') :#or(val[count][0]==''): null
        if(CONS_BD):
            return True

    return False'''

def CONS_BD():
    global count
    if(val[count][0]=='SELF'):
        count+=1
        if(val[count][0]=='.'):
            count+=1
            if(val[count][0]=='IDENTIFIER'):
                count+=1
                if(val[count][0]=='='):
                    count+=1
                    if(val[count][0]=='IDENTIFIER'):
                        count+=1
                        if(val[count][0]==';'):
                            count+=1
                            #print(val[count][0])
                            if(C_B()):
                                return True
                
                    
                
    return False

def C_B():
    global count
    if(val[count][0]=='SELF'):
        if(CONS_BD()):
            return True 
    elif(val[count][0]=='}'): #null remove 
        return True
    return False           

def STRUCTURE_LESS():
    global count
    if(val[count][0]=='FOR'):
        if(FOR_LOOP()):
            return True
    elif(val[count][0]=='IF'):
        if(if_else()):
            return True    
    elif(val[count][0]=='TRY'):
        if(EXCEPTIION_HANDLING()):
            return True
    elif(val[count][0]=='IDENTIFIER'):
        count+=1
        #print(val[count][0],'inc')
        if(F_23()):
            return True
    elif(val[count][0]=='DATA TYPE'):
        count+=1
        if(F_24()):
            return True  
    elif(val[count][0]=='CLASS'):
        if(CLASS()):
            #print(val[count][0],'f2',val[count-1][0],val[count-2][0],count)
            return True 

    print("error ",val[count][0],' at line ',val[count][2],count)                
    return False    
    

def F_23():
    global count
    if(val[count][0]=='+=') or (val[count][0]=='-=') or (val[count][0]=='*=') or (val[count][0]=='/='):
        if(INC_DEC()):
            count+=1
            if(val[count][0]==';'):
                return True
    elif(val[count][0]=='.') or (val[count][0]=='('):
        #print('func')
        if(FUNC_CALL()):
            #print(val[count][0],'23')
            return True
    elif(val[count][0]=='='):
        count+=1
        if(F_25()):
            return True
    return False

def F_25():
    global count
    if(val[count][0]=='['):
        if(LIST()):
            count+=1
            #print(val[count][0],';')
            if (val[count][0]==";"):
                return True       
    elif(val[count][0]=='{'):
        if(DICTIONARY()):
            count+=1
            if(val[count][0]==';'):  
                return True 
    elif(val[count][0]=='IDENTIFIER'):
        if(OBJECT_CREATE()):
            count+=1
            if(val[count][0]==';'):
                return True 

    return False

def F_24():
    global count
    if(val[count][0]=='IDENTIFIER'):
        if(DEC()):
            return True
    elif(val[count][0]=='DEF'):
        if(FUNC_DEF()):
            return True

    return False        

def CLASS_BODY():
    global count
    #print(val[count][0])
    if(val[count][0]=='FOR'):
        if(FOR_LOOP()):
            return True
    elif(val[count][0]=='IF'):
        if(if_else()):
            return True    
    elif(val[count][0]=='TRY'):
        if(EXCEPTIION_HANDLING()):
            return True
    elif(val[count][0]=='IDENTIFIER'):
        count+=1
        if(F_7()):
            return True
    elif(val[count][0]=='DATA TYPE'):
        count+=1
        if(F_6()):
            return True  
    elif(val[count][0]=='DEF'):
        if(CONSTRUCTOR()):
            #print(val[count][0],'con_body')
            return True
    elif(val[count][0]=='SELF'):
        #print('self')
        if(CONS_BD()):
            count-=1
            #print(val[count][0],'con')
            return True          
        
    return False

def F_6():
    global count
    #print(val[count][0])
    if(val[count][0]=='IDENTIFIER'):
        if(DEC()):
            #print('c')
            return True
    elif(val[count][0]=='DEF'):
        #print(val[count][0])    
        if(CLASS_FUN()):
            print(val[count][0])
            return True

    return False

def F_7():
    global count
    if val[count][0] in ['+=','-=','*=','/=']:
        if (INC_DEC()):
            return True
    elif (val[count][0]=='='):
        count+=1
        #print(val[count][0],'con')
        if(F_8()):
            return True  

    return False

def F_8():
    global count
    if(val[count][0]=='['):
        if(LIST()):
            count+=1
            if(val[count][0]==';'):
                return True
    elif(val[count][0]=='{'): 
        if(DICTIONARY()):
            count+=1
            if(val[count][0]==';'):
                return True

    return False        
count=0
a=True
val=[("VAR", "var", "1"),
("IDENTIFIER", "a", "1"),("SEMICOLON", ";", "1"),
("END_MARKER", "$", "1")]




while(count<len(val)) and (a==True):

    print(a,val[count][2])
    count+=1