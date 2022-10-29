import random
def game(comp ,b):
    if comp==b:
        return None
    elif comp=='s':
        if b=='w':
            return False
        elif b=='g':
            return True    
    elif comp=='w':
        if b=='g':
            return False
        elif b=='s':
            return True  
    elif comp=='g':
        if b=='s':
            return False
        elif b=='w':
            return True 
print("computer turn: snake(s), gun(g), water(w) ?")
randNO = random.randint(1,3)
if randNO==1:
    comp ='s'
    
elif randNO==2:
    comp = "g"
   
elif randNO==3: 
    comp='w'




b= input("You'r turn:snake(s), gun(g), water(w) ?")
a= game(comp,b)
print(f"computer chose {comp}")
print(f'you chose {b}')
if a== None:
    print("The game is tie!")
elif a:
    print("You win!")
else :
    print("you lose!")

