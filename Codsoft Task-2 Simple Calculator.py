                                       #----SIMPLE CALCULATOR-----

#CREATING A FUNCTION 'OPT' THAT WILL PERFORM ALL MATHEMATICAL OPERATIONS!!!
def opt():
    choice=str(input("CHOOSE OPERATION - \n1-'+'\n2-'-'\n3-'*'\n4-'/'\n5- '**'\nENTER OPERATION : "))
    if choice=='+':
        print('-->',num1,choice,num2,"=",num1+num2)
    elif choice=='-':
        print('-->',num1,choice,num2,"=",num1-num2)
    elif choice=='*':
        print('-->',num1,choice,num2,"=",num1*num2) 
    elif choice=='**':
        print('-->',num1,choice,num2,'=',num1**num2)   
    elif choice=='/':
        if num1%num2==0:
            print('-->',num1,choice,num2,"=",int(num1/num2))
        else:
            print('-->',num1,choice,num2,"=",num1/num2) 
    else:
        print("PLEASE CHOOSE RIGHT OPEARTION FROM THE GIVEN!!!\n")
        opt()
               
# TAKE TWO NUMBER AS A INPUT FROM USER & ALSO CHECK WHETHER USER VALUES ARE INT OR STR--
def user_input():
    global num1
    num1=input("ENTER FIRST NUMBER : ")
    if num1.isalpha() or num1.isspace() or num1=='':
        print('\n---PLEASE ENTER VALUE IN DIGITS---\n')
        user_input()
    else:
       num1=int(num1)
       global num2 
       num2=input("ENTER SECOND NUMBER : ")
       if num2.isalpha() or num2.isspace() or num2=='':
        print('PLEASE ENTER VALUE IN DIGITS---')
        user_input()
       else:
           num2=int(num2)
           opt() 
print('\n-----CALCULATOR-----\n')            
user_input()              

