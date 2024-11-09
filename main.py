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

def main():
    racers = get_number_of_turtles()

if __name__ == "__main__":
    main()