# MAKE A CONTACT BOOK WITH THE FOLLOWING FEATURES (ADD,DELETE,UPDATE,FIND,VIEW)
#ERRORLESS CONTACTBOOK!!
#######################################################################################

# CREATE A EMPTY LIST WHICH CONTAIN ALL THE DATA IN THE FORM OF DICTONARIES--
G_Data=[]

# CREATE A CLASS NAME CONTACTS------
class Contacts:
    def __init__(self):
        self.Data={}     #--> ''INSTANCE VARIABLE WHICH HOLD THE DATA''
#---------------------------------------------------------------------------------------

# ASK USER WHAT ACTION HE/SHE WANTS TO PERFORM?
    def menu_func(self):
        print('''HOW WOULD YOU LIKE TO PROCEED?
              1. ENTER 1 FOR ADD CONTACT
              2. ENTER 2 FOR DELETE CONTACT
              3. ENTER 3 FOR UPDATE CONTACT
              4. ENTER 4 FOR FIND CONTACT
              5. ENTER 5 FOR SEE CONTACTS ''')
    
        User_choice = input('\nENTER CHOICE HERE - ')
        if User_choice.isnumeric():
            User_choice = int(User_choice)
            def check():
                if User_choice==1:
                    self.add_func()
                elif User_choice==2:
                    self.flush_func() 
                elif User_choice==3:
                    self.update_func()
                elif User_choice==4:
                    self.find_func() 
                elif User_choice==5:
                    self.view_func() 
                else:
                    print('\n INVALID CHOICE!!! \n') 
                    self.menu_func()  
        else:
            print('\n ---PLEASE ENTER CHOICE IN NUMBER--- \n') 
            self.menu_func()
        check()
#-------------------------------------------------------------------------------------- 

#1 THIS METHOD WILL ADD THE CONTACTS IN THE LIST-----
    def add_func(self):
    
    # CHECKING CITY NAME--
        def Check_city():
            global city
            city=input('ENTER CITY - ')
            if city.isalpha():
                if city.lower():
                    city = city.upper()

            # ADD DATA IN THE LIST OF DICTIONARY--
                    self.Data={
                        'NAME' : name,
                        'PHONE' : phone,
                        'CITY' : city
                        }
                    G_Data.append(self.Data)
                    print('\n%s IS ADDED SUCCESSFULLY---\n'%(name))
                    self.ask_func()
                else: pass 

            else:
                print('\n --PLEASE ENTER VALID DETAIL-- \n')
                Check_city() 

    # CHECKING PHONE NUMBER--
        def Check_Phone():
            global phone
            phone=input('ENTER NUMBER - ')
            if phone.isnumeric() and len(phone)==10:
                flag = False
                for x in G_Data:
                    if x['PHONE'] == phone:
                        print('\n**THIS PHONE NUMBER IS ALREADY EXIST**\nTRY ANOTHER NUMBER\n')
                        flag = True
                        Check_Phone()
                    else:
                        continue 
                if flag is False:
                    Check_city()
            else:
                print('\n --PLEASE ENTER VALID PHONE NUMBER-- \n')
                Check_Phone()        

    # CHECKING NAME--
        def Check_name():
            global name
            name=input('\nENTER NAME - ')
            if name.isalpha():
                if name.lower():
                    name = name.upper() 
                    Check_Phone()
                else: pass

            else:
                print('\n --PLEASE ENTER CORRECT NAME-- \n')
                Check_name() 
                  
    # FUNCTION CALLING--
        Check_name()

    # METHOD CALLING--
        self.add_func()
#---------------------------------------------------------------------------------------

#2 THIS METHOD WILL SHOW THE CONTACTS NAME FROM THE LIST---
    def view_func(self):
        print('\nCONTACT LIST-->\n')
        if len(G_Data)==0:
            print('\n---EMPTY---')
            self.ask_func()
        else:
            for x in G_Data:
                print(x)    
            self.ask_func()
#-------------------------------------------------------------------------------------- 

#3 THIS METHOD WILL DELETE THE SELECTED CONTACT FROM THE LIST---
    def flush_func(self):

    # CHECK AND PROVIDE THE RELAVENT DATA TO THE USER---    
        def checker():
                print('PLEASE ENTER THE NAME OF CONTACT THAT YOU WANT TO DELETE--\n')
                con_name=input('ENTER NAME - ')
                if con_name.isalpha():
                    if con_name.lower():
                        con_name = con_name.upper()    
                        flag = False
                        store = []  
                        for item in G_Data:
                            if item['NAME'] == con_name:
                                flag = True
                                store.append(item)
                                continue
                            else: continue 

                        if len(store)>1:
                            for store_item in store:
                                print(store_item) 
                            take = input('\nTHERE ARE MULTIPLE SAME NAMES IN CONTACT\n >>>>>>>>\nENTER THE CITY OF %s TO DELETE  - '%(con_name))
                            for x in G_Data:
                                if x['CITY'] == take and x['NAME'] == con_name: 
                                    G_Data.remove(x)
                                    print('\n%s FROM %s IS DELETED SUCCESSFULLY!!'%(con_name,take)) 
                                    self.ask_func()
                                else: continue

                            if x['CITY'] != take:
                                print("\n SORRY:( CAN'T FOUND %s FROM %s"%(con_name,take))
                                self.ask_func()          
                        else: 
                            for y in G_Data:
                                if y['NAME'] == con_name:
                                    G_Data.remove(y)
                                    print('\n%s IS DELETED SUCCESSFULLY!!'%(con_name)) 
                                    self.ask_func()  
                                else: continue

                        if flag is False:
                            print('\nSORRY,THIS CONTACT IS NOT FOUND:(')
                            self.ask_func()    

                    else: pass                   

                else:
                    print('\n--PLEASE ENTER VALID NAME--\n')
                    checker()

    # FUNCTION CALLING
        checker()
#-------------------------------------------------------------------------------------- 

#4 THIS METHOD WILL SEARCH THE CONTACT NAME IN THE LIST---
    def find_func(self):
        def ask():
            src=input('\n---SEARCH BY NAME---\nENTER NAME - ')
            if src.isalpha():
                if src.lower():
                    src = src.upper()
                    flag = False
                    store2 = []
                    for x in G_Data:
                        if x['NAME'] == src:
                            flag = True
                            store2.append(x)
                            continue   
                        else: continue

                    if len(store2)>1:
                        print('\nCONTACT LIST>>>')
                        for x in store2:
                            print(x)
                        self.ask_func()

                    else:
                        print('\nCONTACT LIST>>>')
                        for val in G_Data:
                            if val['NAME'] == src:
                                print(val) 
                                self.ask_func()
                            else: continue      

                    if flag is False:
                        print('\nSORRY,%s IS NOT FOUND!!'%(src))
                        self.ask_func()
                else: pass

            else:
                print('\n--PLEASE ENTER NAME FOR SEARCHING--\n')   
                ask() 

    # FUNCTION CALLING--
        ask()  
#---------------------------------------------------------------------------------------

#5 THIS METHOD WILL UPDATE THE EXISTING CONTACT---
    def update_func(self):

    # CHECKING CITY----    
        def change_city():
            global new_city
            new_city=input('ENTER CITY - ')
            if new_city.isalpha():
                if new_city.lower():
                    new_city = new_city.upper()
                    for x in G_Data:
                        if x['NAME'] == con_input:
                            x['NAME'] = new_name
                            x['PHONE'] = new_phone
                            x['CITY'] = new_city
                            print('\n---CONTACT IS UPDATED SUCCESSFULLY---\n')
                            self.ask_func()
                        else: continue 
                else: pass

            else:
                print('\n --PLEASE ENTER VALID DETAIL-- \n')
                change_city() 

    # CHECKING NEW PHONE----    
        def change_phn():
            global new_phone
            new_phone = input('ENTER NUMBER - ')  
            if new_phone.isnumeric() and len(new_phone)==10:
                change_city()
            else:
                print('\n --PLEASE ENTER VALID PHONE NUMBER-- \n')
                change_phn()

    # CHECKING NEW NAME----
        def change_name():
                global new_name
                new_name=input('\nENTER NEW NAME - ')
                if new_name.isalpha():
                    if new_name.lower():
                        new_name = new_name.upper()
                        change_phn()
                    else: pass 
                else:
                    print('\n--PLEASE ENTER CORRECT NAME--\n')  
                    change_name() 

    # CHECKING DATA IS PRESENT IN LIST OR NOT----
        def change():
            global con_input
            con_input = input('ENTER THE NAME THAT YOU WANT TO EDIT - ')
            if con_input.isalpha():
                if con_input.lower():
                    con_input = con_input.upper()
                    flag = False
                    global change_stored_data
                    change_stored_data = []
                    for value in G_Data:
                        if value['NAME'] == con_input:
                            flag = True
                            change_stored_data.append(value)
                            continue
                        else: continue

                    if len(change_stored_data)>1:
                        for stored_item in change_stored_data:
                                print(stored_item) 
                        global take_input
                        take_input = input('\nTHERE ARE MULTIPLE SAME NAMES IN CONTACT>>>>>>>>\n \nENTER THE CITY OF %s THAT YOU WANT TO EDIT  - '%(con_input))

                        for x in G_Data:
                            if x['CITY'] == take_input and x['NAME'] == con_input: 
                                change_name()
                            else: continue

                        if x['CITY'] != take_input and x['NAME'] == con_input:
                            print("\n SORRY:( CAN'T FOUND %s FROM %s"%(con_input,take_input))
                            self.ask_func()    
                    else:
                        for y in G_Data:
                            if y['NAME'] == con_input:
                                change_name()
                            else:
                                continue
                            
                    if flag is False:
                        print('SORRY,%s IS NOT FOUND IN CONTACT'%(con_input))  
                        self.ask_func()
                else: pass 

            else:
                print('\n--PLEASE ENTER NAME IN WORDS--\n') 
                change() 

    # FUNCTION CALLING--
        change()                                     
#-------------------------------------------------------------------------------------- 
         
# ---ADDITIONAL METHOD ADDED BY USER---
#6 THIS METHOD WILL ASK THE USER TO SHOW THE MENU OPTIONS---
    def ask_func(self):
        def chooser():
            inner_choice=input('\nENTER "0" FOR MENU - ')
            if inner_choice.isnumeric():
                inner_choice = int(inner_choice)
                if inner_choice==0:
                    self.menu_func() 
                else:
                    print('\n--PLEASE ENTER 0 FOR MENU--\n')   
                    chooser()  
            else:
                print('\n--PLEASE ENTER 0 FOR MENU--\n') 
                chooser() 
        chooser() 
#---------------------------------------------------------------------------------------                 
# CREATING A OBJECT NAME 'USER' AND CALLING MENU FUNCTION TO DISPLAY ALL THE MENU---
user=Contacts().menu_func()