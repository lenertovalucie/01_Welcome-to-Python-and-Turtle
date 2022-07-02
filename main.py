import turtle

print("Hello, world!")

george = turtle.Turtle('turtle') 

george.width(5)
george.color('blue')

for _ in range(4):
    george.forward(70)
    george.left(90)

george.penup()

george.goto(-150, 100)

george.color('green')

message = "Welcome to Python and Turtle!"
george.write(message, font=("Arial", 15, "normal"))
