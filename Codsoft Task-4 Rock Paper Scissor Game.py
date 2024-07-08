                                                #----GAME----

# THERE IS NO NEED OF TIME MODULE I JUST OPTIONALLY USED IT--
import time
import random

# ASSIGN VALUES TO THE VARIABLES--

user_score=0
comp_score=0
x,y,z,i=1,2,3,1

# CREATE A LIST--
option=['SCISSORS','ROCK','PAPER']

# DISPLAY GAME INSTRUCTIONS TO THE USER--

print(" ----------GAME-----------\n  **ROCK--PAPER--SCISSORS**\n\n")
time.sleep(1.01)
print("  --INSTRUCTIONS--\n PRESS KEY 1 FOR ROCK\n PRESS KEY 2 FOR PAPER\n PRESS KEY 3 FOR SCISSORS\n")

# ASK USER TO ENTER THE NUMBER OF ROUNDS THAT HE WANTS TO PLAY--
 
gp=int(input("HOW MANY ROUNDS YOU WANNA PLAY - "))
while i<=gp:
    ent=int(input("\nENTER KEY : "))
    i=i+1

# GAME LOGIC AND SCORE COUNTING --

    if ent==1:
        print("YOUR - ROCK")
        choicex=random.choice(option)
        print("COMP -" +choicex)
        if ent==1 and choicex=='SCISSORS':
            user_score=user_score+1
        elif ent==1 and choicex=='ROCK':
            comp_score=comp_score+0
            user_score=user_score+0
        elif ent==1 and choicex=='PAPER':
            comp_score=comp_score+1
        print("YOUR SCORE :",user_score) 
        print ("COMP SCORE :",comp_score,'\n') 

    if ent==2:
        print("YOUR - PAPER")
        choicex=random.choice(option)
        print("COMP -" +choicex)
        if ent==2 and choicex=='ROCK':
            user_score=user_score+1
        elif ent==2 and choicex=='PAPER':
            comp_score=comp_score+0
            user_score=user_score+0
        elif ent==2 and choicex=='SCISSORS':
            comp_score=comp_score+1
        print("YOUR SCORE :",user_score) 
        print ("COMP SCORE :",comp_score,'\n') 
        
    if ent==3:  
        print("YOUR - SCISSORS") 
        choicex=random.choice(option)     
        print("COMP -" +choicex)
        if ent==3 and choicex=='PAPER':
            user_score=user_score+1
        elif ent==3 and choicex=='SCISSORS':
            comp_score=comp_score+0
            user_score=user_score+0
        elif ent==3 and choicex=='ROCK':
            comp_score=comp_score+1
        print("YOUR SCORE :",user_score) 
        print ("COMP SCORE :",comp_score,'\n') 

# DISPLAY THE RESULT OF A GAME ACCORDING TO THE SCORE--

print("YOUR SCORE :",user_score) 
print ("COMP SCORE :",comp_score,'\n')      

if user_score>comp_score:
    print("YOU WIN!!!\n")
if user_score<comp_score:
    print("YOU LOSE!!!\n")
if user_score==comp_score:
    print("**GAME TIED**\n") 

    





































































































































