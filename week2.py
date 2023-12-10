import time
import random

def introduction():
    print("Welcome to the Mystical Forest Adventure!")
    print("You find yourself at the entrance of a mystical forest. Your goal is to find the hidden treasure.")

def choose_path():
    print("You stand at a crossroads. Choose your path:")
    print("1. Take the left path")
    print("2. Take the right path")
    return input("Enter your choice (1 or 2): ")

def encounter_monster():
    print("Oh no! A fierce monster appears!")
    print("You have to make a quick decision:")
    print("1. Fight the monster")
    print("2. Try to sneak past the monster")
    return input("Enter your choice (1 or 2): ")

def explore_clearing():
    print("You enter a peaceful clearing in the forest.")
    print("You notice a sparkling light beneath a tree.")
    print("It's the hidden treasure! Congratulations, you've won!")

def game_over():
    print("Game over! Better luck next time.")

def main():
    introduction()

    path_choice = choose_path()

    if path_choice == '1':
        print("You follow the left path...")
        time.sleep(1)  # Adding a delay for dramatic effect
        print("You encounter a mystical creature but it's friendly.")
        print("It guides you to a beautiful clearing.")

        explore_clearing()

    elif path_choice == '2':
        print("You follow the right path...")
        time.sleep(1)
        
        monster_choice = encounter_monster()

        if monster_choice == '1':
            print("You bravely fight the monster.")
            if random.choice([True, False]):
                print("Congratulations! You defeated the monster.")
                explore_clearing()
            else:
                print("Unfortunately, the monster was too strong. You lost the battle.")
                game_over()
        elif monster_choice == '2':
            print("You attempt to sneak past the monster.")
            print("It works! You successfully avoid the monster and reach a mysterious clearing.")

            explore_clearing()

        else:
            print("Invalid choice. The monster catches you off guard.")
            game_over()

    else:
        print("Invalid choice. You get lost in the forest.")
        game_over()

if __name__ == "__main__":
    main()
