import random
def game():
    coins=int(input('enter how many coins\n'))
    t=1#turns counter
    y=0
    while coins <=0:
        coins=int(input('enter a positive number'))
    while coins>0:
        if t%2==1:
            x=int(input('player 1 :\n'))
            while (x>=coins and coins>1) or x<1 or (x>2*y and t>1):
                    x=int(input('try again'))
            coins-=x
        else :
            if mode==1:
                print('computer :')
                y=random.randint(1,2*x)
            else: 
                y=int(input('player 2 :\n'))
            while (y>=coins and coins>1) or y<1 or y>2*x:
                if mode==1:
                   y=random.randint(1,2*x)
                else:
                    y=int(input('try again'))
            if mode==1:
                print(y)
            coins-=y
        print('reminder = ',coins,'\n\n')
        if coins>0:
            t+=1
    if t%2==1:
        print('player 1 won')
    elif t%2==0 and mode==1:
        print('computer won')
    else:
        print('player 2 won')
while True:
    mode=int(input('enter 1-play against computer 2-multiplayer mode\n'))
    while mode!=1 and mode!=2:
        mode=int(input('please enter 1 or 2\n'))
    game()
    print('\nnew game\n')
            
