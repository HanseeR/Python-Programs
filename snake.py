import turtle
import time
import random

delay = 0.1
score = 0
highestscore = 0 

# Snake bodies
bodies = []

# Main screen
main_screen = turtle.Screen()
main_screen.title('Snake Game')
main_screen.bgcolor('green')
main_screen.setup(width=600, height=600)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('blue')
head.fillcolor('blue')
head.penup()
head.goto(0, 0)
head.direction = 'stop'

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape('square')
food.color('yellow')
food.fillcolor('red')
food.penup()
food.ht()
food.goto(0, 200)
food.st()

# Score board
sb = turtle.Turtle()
sb.shape('square')
sb.color('red')
sb.fillcolor('black')
sb.penup()
sb.ht()
sb.goto(-280, 250)
sb.write('Score: 0 | HighestScore: 0', font=('arial', 15, 'bold'))

# Function declarations
def moveup():
    if head.direction != 'down':
        head.direction = 'up'

def movedown():
    if head.direction != 'up':
        head.direction = 'down'

def moveleft():
    if head.direction != 'right':
        head.direction = 'left'
        
def moveright():
    if head.direction != 'left':
        head.direction = 'right'

def movestop():
    head.direction = 'stop'

def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)

def update_game():
    global score, highestscore, delay

    main_screen.update()

    # Check collision with borders
    if head.xcor() > 280:
        head.setx(-280)
    if head.xcor() < -280:
        head.setx(280)
    if head.ycor() > 280:
        head.sety(-280)
    if head.ycor() < -280:
        head.sety(280)

    # Check collision with food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Increase the length of snake
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape('square')
        body.color('red')
        body.fillcolor('darkred')
        bodies.append(body)

        # Increase score
        score += 10

        # Change delay
        delay -= 0.01

        # Update the highest score
        if score > highestscore:
            highestscore = score

        sb.clear()
        sb.write('Score: {} | Highest Score: {}'.format(score, highestscore), font=('arial', 15, 'bold'))

    # Move the snake body
    for i in range(len(bodies) - 1, 0, -1):
        x = bodies[i - 1].xcor()
        y = bodies[i - 1].ycor()
        bodies[i].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

    move()

    # Check collision with snake body
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'

            # Hide bodies
            for body in bodies:
                body.ht()
            bodies.clear()

            score = 0
            delay = 0.1

            sb.clear()
            sb.write('Score: {} | Highest Score: {}'.format(score, highestscore), font=('arial', 15, 'bold'))

    main_screen.ontimer(update_game, int(delay * 1000))  # Continue the loop after the delay

# Event handling
main_screen.listen()
main_screen.onkey(moveup, 'Up')
main_screen.onkey(movedown, 'Down')
main_screen.onkey(moveleft, 'Left')
main_screen.onkey(moveright, 'Right')
main_screen.onkey(movestop, 'space')

# Start the game
update_game()

# Start the main event loop
main_screen.mainloop()
