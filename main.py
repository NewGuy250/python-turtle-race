import turtle

# Window dimensions
WIDTH, HEIGHT = 500, 500

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

# Function to display window
def init_turtle():
    screen = turtle.Screen() # Initialize window into variable
    screen.setup(WIDTH, HEIGHT) # Set dimensions
    screen.title("Turtle Racing") # Change window title

def main():
    racers = get_number_of_turtles()
    init_turtle()

if __name__ == "__main__":
    main()