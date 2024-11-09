import turtle
import time
import random

# Window dimensions
WIDTH, HEIGHT = 500, 500
# Possible colors for racers
COLORS = ["green", "red", "blue", "yellow", "black", "cyan", "pink", "purple", "brown", "orange"]

# Get # of racers
def get_number_of_turtles():
    while True:
        try:
            racers = int(input("Enter the number of racers (2-10): "))
            if 2 <= racers <= 10:
                return racers
            else:
                print("Pleaser enter a number within the range 2-10.\n")
        except ValueError:
            print("Enter a number (2-10).\n")
# Race function
def race(colors):
    turtles = create_turtles(colors)
    # Race
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)
            # Get y position to determine if winner
            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]

# Create turtles
def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color) # Get color
        racer.shape("turtle") # Get shape
        racer.left(90) # Make sure the turtle is racing upwards
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20) # Move turtle into right position
        racer.pendown()
        turtles.append(racer)
    return turtles

# Function to display window
def init_turtle():
    screen = turtle.Screen() # Initialize window into variable
    screen.setup(WIDTH, HEIGHT) # Set dimensions
    screen.title("Turtle Racing") # Change window title

def main():
    racers = get_number_of_turtles()
    init_turtle()
    # Get colors for racers
    random.shuffle(COLORS)
    colors = COLORS[:racers]
    winner = race(colors)
    print(f"The winner is: {winner.capitalize()}!")
    time.sleep(3)
    
if __name__ == "__main__":
    main()