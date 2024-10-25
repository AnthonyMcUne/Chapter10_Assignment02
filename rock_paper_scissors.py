import turtle
import random
wn = turtle.Screen()
#I preferred the game to utilized mouse clicks for ther users choice
#The code for the key presses, however, is is also scripted in, and the keys for each respective choice
#correspond with their first letters.
rock = "Rock.gif"
paper = "Paper.gif"
scissors = "Scissors.gif"

user_choice = 0
user_score = 0
computer_score= 0
wn.addshape(rock)
wn.addshape(paper)
wn.addshape(scissors)

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
score_keeper = turtle.Turtle()
announcer = turtle.Turtle()

def computer_rock_paper_scissors():
    com_num = random.randint(0, 2)
    return com_num
def rock_paper_scissors():
    global user_score
    global computer_score
    global user_choice
    computer_choice = computer_rock_paper_scissors()
    if computer_choice == 0 and user_choice == 0:
        announcer.write("Computer chose rock! You tied!")
    elif computer_choice == 0 and user_choice == 1:
        announcer.write("Computer chose rock! You won!")
        user_score += 1
    elif computer_choice == 0 and user_choice == 2:
        announcer.write("Computer chose rock! You lost!")
        computer_score += 1 
    elif computer_choice == 1 and user_choice == 0:
        announcer.write("Computer chose paper! You lost!")
        computer_score += 1
    elif computer_choice == 1 and user_choice == 1:
        announcer.write("Computer chose paper! You tied!")
    elif computer_choice == 1 and user_choice == 2:
        announcer.write("Computer chose paper! You won!")
        user_score += 1
    elif computer_choice == 2 and user_choice == 0:
        announcer.write("Computer chose scissors! You won!")
        user_score += 1
    elif computer_choice == 2 and user_choice == 1:
        announcer.write("Computer chose scisssors! You lost!")
        computer_score += 1
    elif computer_choice == 2 and user_choice == 2:
        announcer.write("Computer chose scisssors! You tied!")
    score_keeper.clear()
    score_keeper.write("Computer: ")
    score_keeper.forward(50)
    score_keeper.write(computer_score)
    score_keeper.forward(60)
    score_keeper.write("You: ")
    score_keeper.forward(30)
    score_keeper.write(user_score)
    wn.ontimer(reset, 3000)
def user_rock(x,y):
    global user
    t2.hideturtle()
    t3.hideturtle()
    user_choice = 0
    wn.ontimer(rock_paper_scissors, 2000)
def user_paper(x,y):
    global user_choice
    t1.hideturtle()
    t3.hideturtle()
    user_choice = 1
    wn.ontimer(rock_paper_scissors, 2000)
def user_scissors(x,y):
    global user_choice
    t1.hideturtle()
    t2.hideturtle()
    user_choice = 2
    wn.ontimer(rock_paper_scissors, 2000)
def user_rock_key():
    global user
    t2.hideturtle()
    t3.hideturtle()
    user_choice = 0
    wn.ontimer(rock_paper_scissors, 2000)
def user_paper_key():
    global user_choice
    t1.hideturtle()
    t3.hideturtle()
    user_choice = 1
    wn.ontimer(rock_paper_scissors, 2000)
def user_scissors_key():
    global user_choice
    t1.hideturtle()
    t2.hideturtle()
    user_choice = 2
    wn.ontimer(rock_paper_scissors, 2000)
def reset():
    t1.showturtle()
    t2.showturtle()
    t3.showturtle()
    announcer.clear()
    score_keeper.left(180)
    score_keeper.forward(140)
    score_keeper.left(180)


score_keeper.penup()
score_keeper.hideturtle()
announcer.penup()
announcer.hideturtle()
t1.penup()
t2.penup()
t3.penup()

t1.shape(rock)
t2.shape(paper)
t3.shape(scissors)

score_keeper.right(90)
score_keeper.forward(150)
score_keeper.right(90)
score_keeper.forward(75)
score_keeper.left(180)
announcer.left(90)
announcer.forward(150)
announcer.left(90)
announcer.forward(75)
announcer.right(180)
t1.forward(-200)
t3.forward(200)



t1.onclick(user_rock)
t2.onclick(user_paper)
t3.onclick(user_scissors)
wn.onkey(user_rock_key, "r")
wn.onkey(user_paper_key, "p")
wn.onkey(user_scissors_key, "s")
wn.bgcolor("lightblue")

wn.listen()
wn.mainloop() # Wait for user to close window
