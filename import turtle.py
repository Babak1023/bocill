import turtle
import time
import random

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Bucin Animation")

# Function to draw a heart
def draw_heart(color):
    turtle.color(color)
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(180)
    turtle.circle(-90, 200)
    turtle.left(120)
    turtle.circle(-90, 200)
    turtle.forward(180)
    turtle.end_fill()

def display_text(text, color, y_offset, size):
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.color(color)
    pen.penup()
    pen.goto(0, y_offset)
    pen.pendown()
    pen.write(text, align="center", font=("Comic Sans MS", size, "bold"))
    
# Function to show animated texts
def animated_text():
    phrases = ["Sayang banget sama kamu!", "Kamu tuh candu!", "My love, my world!", "Selamanya kamu di hati!"]
    colors = ["red", "pink", "white", "purple"]
    y_positions = [100, 50, 0, -50]
    
    for i in range(4):
        display_text(phrases[i], colors[i], y_positions[i], 20)
        time.sleep(1)
        screen.update()

def falling_hearts():
    heart = turtle.Turtle()
    heart.hideturtle()
    heart.speed(0)
    
    for _ in range(10):
        x = random.randint(-200, 200)
        y = random.randint(100, 300)
        heart.penup()
        heart.goto(x, y)
        heart.pendown()
        draw_heart(random.choice(["red", "pink", "purple"]))
        time.sleep(0.3)
        screen.update()

# Main animation
turtle.speed(3)
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
draw_heart("red")
animated_text()
falling_hearts()

time.sleep(5)
screen.bye()
