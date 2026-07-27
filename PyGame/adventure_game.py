# This script runs a simple text-based adventure game.
print("Welcome to the adventure game!")


def start_game():
    print("You wake up in a mysterious land.")
    name = input("What is your name? ")
    print(f"Hello, {name}! You stand at a fork in the road.")

    choice = input("Do you want to explore the forest or enter the cave? ").strip().lower()
    if choice == "forest":
        forest_path()
    elif choice == "cave":
        cave_path()
    else:
        print("That choice is not recognized. Please try again.")


def forest_path():
    print("You step into the forest. The trees are tall and the air is cool.")

    choice = input("Do you want to follow the river or climb a tree? ").strip().lower()
    if choice == "river":
        print("You follow the river and find a hidden bridge.")
    elif choice == "tree":
        print("You climb the tree and spot a distant castle.")
    else:
        print("That choice is not recognized. Please try again.")


def cave_path():
    print("You step into the cave. The walls shimmer with ancient markings.")

    choice = input("Do you want to light a torch or proceed in the dark? ").strip().lower()
    if choice == "torch":
        print("The torch reveals a hidden treasure chamber.")
    elif choice == "dark":
        print("You stumble into a deep chamber and find an old map.")
    else:
        print("That choice is not recognized. Please try again.")


def main():
    while True:
        start_game()
        play_again = input("Do you want to play again? (yes/no) ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
