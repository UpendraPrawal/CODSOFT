                                #-----GENRATING RANDOM PASSWORD------

import random

small_char='abcdefghijklmnopqrstuvwxyz'
capital_char='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols='!@#$%*[,]{.}'
num_values='1234567890'

# --COMPLEXITY--
easy,moderate,hard='low','mid','high'

#--MAKING COMBINATION OF VALUES AS PER COMPLEXITY LEVEL--
Low_level=capital_char + num_values
Mod_level=small_char + capital_char + num_values
Hard_level=small_char + capital_char + symbols + num_values

# ASK USER FOR A LENGTH OF A PASSWORD AND COMPLEXITY LEVEL--

user_input=int(input("ENTER LENGTH OF YOUR PASSWORD : "))
complexity=str(input("DIFFICULTY--\n-LOW\n-MID\n-HIGH\nENTER LEVEL OF DIFFICULTY - "))

for i in range(user_input):
        if complexity=='high' or complexity=='HIGH':
            h_pwd=random.choice(Hard_level)
            print(h_pwd,end='') 
        elif complexity=='mid' or complexity=='MID':
            m_pwd=random.choice(Mod_level)
            print(m_pwd,end='')
        elif complexity=='low' or complexity=='LOW':
            e_pwd=random.choice(Low_level) 
            print(e_pwd,end='')     
        else:
             print("YOU'VE ENTERED WRONG OPTOIN!")
             
           
        
















"""
for i in range(user_input):
    if complexity=='low':
        password=random.choice(char)
        print(password,end='')
    elif complexity=='mid':
        password=random.choice(sym)
        print(password,end='')
    elif complexity=='high':
        password=random.choice(tchar)  
        print(password,end='') 
"""