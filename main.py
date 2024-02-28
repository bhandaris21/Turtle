
import turtle
import tkinter as tk

import turtle
import random

# Function to move the turtle in a random direction and update its position
def take_step(turtle_object):
    # Generate a random angle between 0 and 360 degrees
    random_angle = random.randint(0, 360)

    # Turn the turtle to the random angle
    turtle_object.setheading(random_angle)

    # Move the turtle forward a certain distance
    turtle_object.forward(50)

# Create the turtle object
t = turtle.Turtle()

# Set the turtle's appearance (optional)
# You can customize the turtle's color, pen size, and speed here

# Set the maximum number of steps
max_steps = 100

# Start the random walk
for _ in range(max_steps):
    take_step(t)

# Keep the turtle window open (optional)
turtle.done()
