from turtle import *
from time import sleep
from sys import exit

List=[]
cross=[]
os=[]
win_places=[
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [1,5,9],
        [3,5,7],
        [1,4,7],
        [2,5,8],
        [3,6,9]
        ]

def one():
    up()
    goto(-100,135)
    down()
    forward(20)

def two():
    up()
    goto(0,135)
    down()
    left(90)
    forward(10)
    right(90)
    forward(10)
    right(90)
    forward(10)
    left(90)
    forward(10)
    left(90)
    forward(10)

def three():
    up()
    goto(100,135)
    down()
    forward(10)
    right(90)
    forward(10)
    right(90)
    forward(10)
    left(180)
    forward(10)
    right(90)
    forward(10)
    right(90)
    forward(10)
    right(90)

def four():
    up()
    goto(-110,30)
    down()
    forward(10)
    right(90)
    up()
    forward(10)
    right(90)
    down()
    forward(20)
    up()
    goto(-110,30)
    left(90)
    down()
    forward(10)

def five():
    up()
    goto(0,30)
    down()
    forward(10)
    right(90)
    forward(10)
    right(90)
    forward(10)
    right(90)
    up()
    goto(0,30)
    down()
    forward(10)
    right(90)
    forward(10)
    right(90)

def six():
    up()
    goto(100,40)
    down()
    forward(20)
    left(90)
    forward(10)
    left(90)
    forward(10)
    left(90)
    forward(10)
    right(90)

def seven():
    up()
    goto(-100,-80)
    down()
    forward(20)
    left(90)
    forward(10)

def eight():
    up()
    goto(0,-60)
    down()
    left(90)
    forward(20)
    left(90)
    forward(10)
    left(90)
    forward(20)
    left(90)
    forward(10)
    left(90)
    forward(10)
    left(90)
    forward(10)

def nine():
    up()
    goto(100,-70)
    down()
    left(90)
    forward(10)
    right(90)
    forward(10)
    right(90)
    forward(20)
    up()
    goto(100,-70)
    left(90)
    down()
    forward(10)
    left(180)


def base():
    setup(width=350,height=350)
    ht()
    speed(0)

    #horizontal
    up()
    goto(-150,-50)
    down()
    forward(300)
    up()
    left(90)
    forward(100)
    left(90)
    down()
    forward(300)

    #vertical
    up()
    goto(-50,-150)
    right(90)
    down()
    forward(300)
    up()
    right(90)
    forward(100)
    right(90)
    down()
    forward(300)

    #numbers
    one()
    two()
    three()
    four()
    five()
    six()
    seven()
    eight()
    nine()

def cut(a):
    color('blue')
    if a == win_places[0]:
        up()
        goto(-150,85)
        down()
        left(180)
        forward(300)

    elif a == win_places[1]:
        up()
        goto(-150,-15)
        down()
        left(180)
        forward(300)

    elif a == win_places[2]:
        up()
        goto(-150,-115)
        down()
        left(180)
        forward(300)

    elif a == win_places[3]:
        up()
        goto(-150,150)
        down()
        left(135)
        forward(425)

    elif a == win_places[4]:
        up()
        goto(150,150)
        down()
        left(45)
        forward(425)

    elif a == win_places[5]:
        up()
        goto(-100,150)
        down()
        left(90)
        forward(300)

    elif a == win_places[6]:
        up()
        goto(0,150)
        down()
        left(90)
        forward(300)

    elif a == win_places[7]:
        up()
        goto(100,150)
        down()
        left(90)
        forward(300)
        
    FileWrite()

def win():
    global winner
    global t1, t2
    global P1, P2

    for l in win_places:

        if all(a in cross for a in l):
            print("{} wins".format(t2))
            winner = t2

            t1, t2 = t2, t1
            cut(l)

        if all(i in os for i in l):
            print("{} wins".format(t1))
            winner = t1
            cut(l)

    l1=[1,2,3,4,5,6,7,8,9]

    if l1 == sorted(List):

        print("The match is draw")
        t1,t2 = t2,t1

        FileRead()

def turn():
    if len(List)%2==0:  #zero
        color('red')
        up()
        backward(3)
        down()
        for i in range(72):
            forward(1)
            right(5)
        up()

    elif len(List)%2==1:  #cross
        color('orange')
        up()
        forward(8)
        down()
        right(135)
        forward(30)
        up()
        left(135)
        forward(20)
        left(135)
        down()
        forward(30)
        right(135)
        up()

def touch(x,y):


    if x>-160 and x<-50:
        if y>-160 and y<-50:  #place 7
            up()
            goto(-100,-125)
            down()

            if 7 not in List:
                turn()

                if len(List)%2==0:
                    os.append(7)

                else:
                    cross.append(7)

                List.append(7)
            else:
                print("This place is already taken")

        elif y<50:  #place 4
            up()
            goto(-100,-25)
            down()

            if 4 not in List:

                turn()
                if len(List)%2==0:
                    os.append(4)

                else:
                    cross.append(4)

                List.append(4)
            else:
                print("This place is already taken")

        elif y<160:  #place 1
            up()
            goto(-100,75)
            down()

            if 1 not in List:

                turn()

                if len(List)%2==0:
                    os.append(1)

                else:
                    cross.append(1)

                List.append(1)
            else:
                print("This place is already taken")

    elif x<50:
        if y>-160 and y<-50:  #place 8
            up()
            goto(0,-125)
            down()

            if 8 not in List:

                turn()

                if len(List)%2==0:
                    os.append(8)

                else:
                    cross.append(8)

                List.append(8)
            else:
                print("This place is already taken")

        elif y<50:  #place 5
            up()
            goto(0,-25)
            down()

            if 5 not in List:

                turn()

                if len(List)%2==0:
                    os.append(5)

                else:
                    cross.append(5)

                List.append(5)
            else:
                print("This place is already taken")

        elif y<160:  #place 2
            up()
            goto(0,75)
            down()

            if 2 not in List:

                turn()

                if len(List)%2==0:
                    os.append(2)

                else:
                    cross.append(2)

                List.append(2)
            else:
                print("This place is already taken")

    elif x<160:
        if y>-160 and y<-50:  #place 9
            up()
            goto(100,-125)
            down()

            if 9 not in List:

                turn()

                if len(List)%2==0:
                    os.append(9)

                else:
                    cross.append(9)

                List.append(9)
            else:
                print("This place is already taken")

        elif y<50:  #place 6
            up()
            goto(100,-25)
            down()
            if 6 not in List:

                turn()

                if len(List)%2==0:
                    os.append(6)
                else:
                    cross.append(6)
                List.append(6)
            else:
                print("This place is already taken")

        elif y<160:  #place 3
            up()
            goto(100,75)
            down()
            if 3 not in List:

                turn()
                if len(List)%2==0:
                    os.append(3)
                else:
                    cross.append(3)
                List.append(3)
            else:
                print("This place is already taken")

    win()
    loop()
    
def FileWrite():
    global winner
    global w1, w2
        
    player = open("tictactoe.txt",'a')
    player.write("{}\n".format(winner))
    
    player.close()
    
    if winner == P1:
    	w1 += 1
    elif winner == P2:
    	w2 += 1

    FileRead()
    
def FileRead():

    global t1, t2
    global P1, P2
    global participants
    
    
    player = open("tictactoe.txt",'r')
    
    a = player.readlines()
    
    participants = dict()
    
    for i in a:
        if i.strip() in participants.keys():
            participants[i.strip()]+=1
            
        elif i.strip() not in participants.keys():
            participants[i.strip()]=1
    
    player.close()
    Options()
    
def Options():

    global participants
    global P1, P2
    global t1, t2
    global w1, w2
    
    print("\n")
    print("PRESS 1 if you want to know this score ")
    print("PRESS 2 if you want to see the leaderboard ")
    print("PRESS 3 if you want to change player ")
    print("PRESS 4 to see score of a person ")
    print("PRESS 5 to play again ")
    print("PRESS 6 to quit ")
    
    LeadBoard = int(input())
    
    if LeadBoard == 1:
        print("{}'s won".format(P1),w1,'times')
        print("{}'s won".format(P2),w2,'times')

        Options()
        
    elif LeadBoard == 2:
        itm = participants.items()
        itmL = []
        
        for i in itm:
            itmL.append(i)
            
        #bubble sorting of itmL list to show leaderboard
        for i in range(len(itmL)):
            for j in range (0,len(itmL)-i-1):
                if itmL[j][1] < itmL[j+1][1]:
                    itmL[j],itmL[j+1]=itmL[j+1],itmL[j]
                    
        try:
            for i in range(10):
                print("The score of {} is :".format(itmL[i][0]), itmL[i][1])
        except IndexError:
            pass

        Options()
            
    elif LeadBoard == 3:
    	
        if w1 > w2:
            print("{} wins".format(P1))
            
        elif w1 < w2:
            print("{} wins".format(P2))
            
        elif w1 == w2:
            print("The match was draw")
        
        print("\n")
        
        w1 = w2 = 0
        
        P1 = input("Enter the name of player 1 ")
        P2 = input("Enter the name of player 2 ")
        
        t1,t2 = P1,P2
        
        LeadBoard = 5
        
    elif LeadBoard == 4:
    	nam = input("Enter the name of the person whose score you want to know ")
    	try :
    		print(nam, 'has won', participants[nam], 'times')
    	except KeyError:
    		print("Player not found")
    	
    	Options()
    	
    	
    elif LeadBoard == 6:
    	#chanf=ge it to w1 and w2
        if w1 > w2:
            print("{} wins".format(P1))
            
        elif w1 < w2:
            print("{} wins".format(P2))
            
        elif w1 == w2:
            print("The match was draw")

        
        sleep(1)
        exit()
        
    if LeadBoard == 5:
            
            print("\n")
            
            clearscreen()
            
            base()
            
            List.clear()
            os.clear()
            cross.clear()

def loop():
    if len(List)%2==0:

        print("Its {}'s turn ".format(t1))
        
    elif len(List)%2==1:

        print("Its {}'s turn ".format(t2))

    onscreenclick(touch,btn=1,add=True)
    mainloop()


if __name__=='__main__':

    print("This is a game of Tic Tac Toe")
    
    global P1, P2
    global t1, t2
    global w1, w2
    
    w1 = w2 = 0
    
    P1 = input("Enter the name of player 1 ")
    P2 = input("ENter the name of player 2 ")
    
    t1,t2 = P1,P2

    base()
    
    while True:

        loop()
        