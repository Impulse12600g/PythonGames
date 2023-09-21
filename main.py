import flappy_bird_1



def mainScreen():
    print("WELCOME TO PYTHON GAMES")
    print()
    print("----press any button and enter-----")
    input()  # wait for user


def printMenu():
    print("Games")
    print("1. Flappy Bird")


def menu():
    mainScreen()
    while True:
        printMenu()
        choice = input("Enter Number")

        if choice == "1":
            flappy_bird_1.flappy()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu()
