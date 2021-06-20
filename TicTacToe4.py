# go to base and correct writing TicTacToe part
#


from turtle import *
from time import sleep
from sys import exit
List = []
cross = []
os = []
win_places = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 5, 9],
    [3, 5, 7],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]


def one():
    up()
    goto(-100, 135)
    down()
    forward(20)


def two():
    up()
    goto(0, 135)
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
    goto(100, 135)
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
    goto(-110, 30)
    down()
    forward(10)
    right(90)
    up()
    forward(10)
    right(90)
    down()
    forward(20)
    up()
    goto(-110, 30)
    left(90)
    down()
    forward(10)


def five():
    up()
    goto(0, 30)
    down()
    forward(10)
    right(90)
    forward(10)
    right(90)
    forward(10)
    right(90)
    up()
    goto(0, 30)
    down()
    forward(10)
    right(90)
    forward(10)
    right(90)


def six():
    up()
    goto(100, 40)
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
    goto(-100, -80)
    down()
    forward(20)
    left(90)
    forward(10)


def eight():
    up()
    goto(0, -60)
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
    goto(100, -70)
    down()
    left(90)
    forward(10)
    right(90)
    forward(10)
    right(90)
    forward(20)
    up()
    goto(100, -70)
    left(90)
    down()
    forward(10)
    left(180)

# declaring an other turtlke pointor so that it can be erased when i need to


def erasableWrite(name, font, align, reuse=None):
    eraser = Turtle() if reuse is None else reuse
    eraser.hideturtle()
    eraser.up()
    eraser.setposition(position())
    eraser.write(name, font=font, align=align)
    return eraser


def base():
    setup(width=350, height=450)
    ht()
    speed(0)

    # Writing TicTacToe
    up()
    goto(-125, 220)
    down()
    color('black')
    write("TicTacToe", True, align='center')

    # horizontal
    up()
    goto(-150, -50)
    down()
    forward(300)
    up()
    left(90)
    forward(100)
    left(90)
    down()
    forward(300)
    # vertical
    up()
    goto(-50, -150)
    right(90)
    down()
    forward(300)
    up()
    right(90)
    forward(100)
    right(90)
    down()
    forward(300)
    # numbers
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
        goto(-150, 85)
        down()
        left(180)
        forward(300)
        sleep(1)
        exit()

    elif a == win_places[1]:
        up()
        goto(-150, -15)
        down()
        left(180)
        forward(300)
        sleep(1)
        exit()

    elif a == win_places[2]:
        up()
        goto(-150, -115)
        down()
        left(180)
        forward(300)
        sleep(1)
        exit()

    elif a == win_places[3]:
        up()
        goto(-150, 150)
        down()
        left(135)
        forward(425)
        sleep(1)
        exit()

    elif a == win_places[4]:
        up()
        goto(150, 150)
        down()
        left(45)
        forward(425)
        sleep(1)
        exit()

    elif a == win_places[5]:
        up()
        goto(-100, 150)
        down()
        left(90)
        forward(300)
        sleep(1)
        exit()

    elif a == win_places[6]:
        up()
        goto(0, 150)
        down()
        left(90)
        forward(300)
        sleep(1)
        exit()

    elif a == win_places[7]:
        up()
        goto(100, 150)
        down()
        left(90)
        forward(300)
        sleep(1)
        exit()


def win():

    for l in win_places:

        if all(a in cross for a in l):
            print("Cross wins")
            cut(l)

        if all(i in os for i in l):
            print("Zero wins")
            cut(l)

    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if l1 == sorted(List):
        print("The match is draw")
        sleep(1)
        exit()


def turn():
    if len(List) % 2 == 0:  # zero
        color('red')
        up()
        backward(3)
        down()
        for i in range(72):
            forward(1)
            right(5)
        up()

    elif len(List) % 2 == 1:  # cross
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


def touch(x, y):

    if x > -160 and x < -50:
        if y > -160 and y < -50:  # place 7
            up()
            goto(-100, -125)
            down()
            if 7 not in List:
                turn()
                if len(List) % 2 == 0:
                    os.append(7)
                else:
                    cross.append(7)
                List.append(7)
            else:
                print("This place is already taken")
        elif y < 50:  # place 4
            up()
            goto(-100, -25)
            down()
            if 4 not in List:

                turn()
                if len(List) % 2 == 0:
                    os.append(4)
                else:
                    cross.append(4)
                List.append(4)
            else:
                print("This place is already taken")
        elif y < 160:  # place 1
            up()
            goto(-100, 75)
            down()
            if 1 not in List:

                turn()

                if len(List) % 2 == 0:
                    os.append(1)
                else:
                    cross.append(1)
                List.append(1)
            else:
                print("This place is already taken")

    elif x < 50:
        if y > -160 and y < -50:  # place 8
            up()
            goto(0, -125)
            down()
            if 8 not in List:

                turn()

                if len(List) % 2 == 0:
                    os.append(8)
                else:
                    cross.append(8)
                List.append(8)
            else:
                print("This place is already taken")
        elif y < 50:  # place 5
            up()
            goto(0, -25)
            down()
            if 5 not in List:

                turn()

                if len(List) % 2 == 0:
                    os.append(5)
                else:
                    cross.append(5)
                List.append(5)
            else:
                print("This place is already taken")
        elif y < 160:  # place 2
            up()
            goto(0, 75)
            down()
            if 2 not in List:

                turn()

                if len(List) % 2 == 0:
                    os.append(2)
                else:
                    cross.append(2)
                List.append(2)
            else:
                print("This place is already taken")

    elif x < 160:
        if y > -160 and y < -50:  # place 9
            up()
            goto(100, -125)
            down()
            if 9 not in List:

                turn()

                if len(List) % 2 == 0:
                    os.append(9)
                else:
                    cross.append(9)
                List.append(9)
            else:
                print("This place is already taken")
        elif y < 50:  # place 6
            up()
            goto(100, -25)
            down()
            if 6 not in List:

                turn()

                if len(List) % 2 == 0:
                    os.append(6)
                else:
                    cross.append(6)
                List.append(6)
            else:
                print("This place is already taken")
        elif y < 160:  # place 3
            up()
            goto(100, 75)
            down()
            if 3 not in List:

                turn()
                if len(List) % 2 == 0:
                    os.append(3)
                else:
                    cross.append(3)
                List.append(3)
            else:
                print("This place is already taken")
    win()
    loop()


def loop():
    if len(List) % 2 == 0:

        print("Its Zero's turn ")
    elif len(List) % 2 == 1:

        print("Its Cross' turn ")

    onscreenclick(touch, btn=1, add=True)
    mainloop()


if __name__ == '__main__':
    t = Turtle()
    base()
    print("This is a game of Tic Tac Toe")
    while True:

        loop()
