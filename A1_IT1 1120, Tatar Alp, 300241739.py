
import math
import turtle
""" 
Family name: Tatar, Alp
Student number: 300241739
Course: IT1 1120 
Assignment Number 1
year 2021
"""

"""
Question 1
"""

def mh2kh(s):
    return s * 1.609344 #conversion factor for Miles per hour to kilometers per hour is 1.609344

"""
Question 2
"""

def pythagorean_pair(a,b) :
    x= (math.hypot(a,b))
    return x % 2 == 0

"""
Question 3
"""

def in_out(xs,ys,side):
    print("Enter a number for the x coordinate of a query point:")
    xQuery = float(input())
    print("Enter a number for the y coordinate of a query point:")
    yQuery = float(input())
    xAnswer = (xs <= xQuery <= (xs+ side))
    yAnswer = (ys <= yQuery <= (ys+side))
    return xAnswer == True and yAnswer == True


"""
Question 4 
"""

def safe(n):
    safenumber = (0<n<100 and ((n%9)==0 or int(n/10) == 9 or n%10 == 9 )) == False
    return safenumber

"""
Question 5
"""

def quote_maker(quote, name, year):
    return "In " + str(year) + " a person called " + str(name) +" said: " +'"' + str(quote) +'"'

"""
Question 6
"""

def quote_displayer():
      quote =input("Give me a quote: ")
      name = input("Who said that? ")
      year = input("What year did she/he say that? ")
      return print(quote_maker(quote,name,year))

"""
Question 7
"""

def rps_winner():
    player1choice = input("what choice did player 1 make \n Type one of the following options: rock, paper, scissors:")
    player2choice = input("what choice did player 2 make \n Type one of the following options: rock, paper, scissors:")
    winnerofgame = (player1choice == "rock" and player2choice == "scissors") or (player1choice == "paper" and player2choice == "rock") or (player1choice == "scissors" and player2choice == "paper")
    isitdraw = player2choice != player1choice
    return print("Player 1 wins. That is " + str(winnerofgame) + " \n It is a tie. That is not " + str(isitdraw))


"""
Question 8
"""

def fun(x):
    return (math.log10(x+3))/4

"""
Question 9
"""

def ascii_name_plaque(name):
    thePlaquetopandbot = "**"+ ("*" * (len(name)+4)) +"**"
    thePlaquespaceswith = "* " + ((" ")*(len(name)+4)) + " *"
    thePlaquemiddle ="* " + ("__" + name + "__") + " *"
    return print(thePlaquetopandbot  +"\n" + thePlaquespaceswith +"\n" + thePlaquemiddle +"\n" + thePlaquespaceswith + "\n"+ thePlaquetopandbot)

"""
Question 10 - not complete 

Backround - RGB = (224,237,219)

A - RGB (150,60,36)
B - RGB (213,133,62)
C - RGB (150,60,36) 
D - RGB (99,99,99)
E - RGB (182,205,199) interior & (66,64,65) exterior
F - RGB (208,210,205)
G - RGB (182,215,234) check image (darker), (222,240,252) check image (lighter)
H -  RGB (182,215,234) check image (darker), (222,240,252) check image (lighter)
I - RGB (182,215,234) check image (darker), (222,240,252) check image (lighter)
J - RGB (182,205,199) interior & (66,64,65) exterior
K - RGB (99,99,99)

MAX pixels is 350
Make sure to remove the time function while submitting
"""

def draw_train():
    turtle.penup()#start of location
    turtle.left(180)
    turtle.forward(175)
    turtle.speed(10)
#Block A
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor('#963c24')
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.end_fill()

#Block B
    turtle.begin_fill()
    turtle.fillcolor('#D5853E')
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.end_fill()
    turtle.penup()

#Block j
    turtle.right(90) #start of location
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(37.5)
    turtle.right(90)

    turtle.forward(40)#start of drawing
    turtle.left(90)
    turtle.forward(35)
    turtle.begin_fill()
    turtle.fillcolor('#424041')
    turtle.pendown()
    turtle.circle(55)
    turtle.end_fill()
    turtle.penup()

    turtle.left(90)# start of location
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(2)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor('#B6CDC7')
    turtle.circle(45)
    turtle.end_fill()
    turtle.penup()
    turtle.home()

# Block e
    turtle.left(180)
    turtle.forward(175)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)

"""
Question 11
"""

def alogical(n):
   return math.ceil(math.log2(n))

"""
Question 12
"""

def cad_cashier(price,payment):
    return round((payment - price) * 20.0) / 20.0 # simplification of the expression change round((payment - price) * 100/5)* 5/100

"""
Question 13
"""

def min_CAD_coins(price,payment):
    change = cad_cashier(price,payment)
    tooniesDue = int(change//2)
    change %= 2
    looniesDue = int(change//1)
    change %= 1
    quartersDue =int(change//0.25)
    change %= 0.25
    dimesDue = int(change//0.10)
    change %= 0.10
    nickelsDue=int(change//0.05)
    return "("+str(tooniesDue)+", "+str(looniesDue)+", "+str(quartersDue)+", "+str(dimesDue)+", "+str(nickelsDue)+")"

