# Author: Håkan den store och extremt snygga.
# Description: Dre dåligt textbaserat spel
# Version: 2.0
# Date: 1655-12-31
# -----------------------------------------------

# IMPORTS
import time
import random
import os
from datetime import datetime

# VARIABLES
name = ""
keys = 0
money = 0
irritation = 0
items = []

# BACKPACK DICTIONARY
backpack = {
    "keys": keys, # Keys
    "money": money, # Money
    "name": name, # Player name
    "irritation": irritation, # Irritation level
    "items": [] # Others?
}

# sökning i dictionary behöver man ha

# if keys in backpack > 0:
#         print("He had a key in his pocket...")

# MENU FUNCTION
def menu(backpack):
    """
    Displays the main menu options to the user and waits for input.
    If the user chooses to start the game, the game() function is called.
    If the user chooses to choose a name, the choose_name() function is called.
    If the user chooses to save the game, the save() function is called.
    If the user chooses to exit the game, the program terminates.
    If the user chooses an invalid option, then the menu() function is called again.

    Returns:
    None
    """
    
    # Displays menu options
    print("=====================")
    print("1. START GAME")
    print("2. CHOOSE NAME")
    print("3. SAVE")
    print("4. EXIT")
    print("=====================")

    # Get user's choice
    choice = input("What do you want to do?: ")

    # If choice is 1 then call the function game.
    if choice == "1":
        print("You have chosen to start the game.")
        time.sleep(0.5)
        print("Loading.")
        time.sleep(0.2)
        print("Loading..")
        time.sleep(0.2)
        print("Loading...")
        game(backpack)
  
    # If choice is 2 then call the function choose_name.
    elif choice == "2":
        print("You have chosen to choose a name.")
        time.sleep(0.5)
        print("Loading.")
        time.sleep(0.2)
        print("Loading..")
        time.sleep(0.2)
        print("Loading...")
        choose_name(backpack)
    
    # If choice is 3 then call the function save.
    elif choice == "3":
        print("You have chosen to save the game.")
        save(backpack)
    
    # If choice is 4 then exit the program.
    elif choice == "4":
        print("You have chosen to exit the game.")
        exit()
    
    # Invalid input
    else:
        print("Invalid input. Try again.")
        menu()

# CHOOSE NAME
def choose_name(backpack):
    """
    Allows the user to choose their character's name.

    This function prompts the user for their name and asks if they want to save it.
    If the user chooses to save their name, the save function is called.

    Args:
        backpack (dict): The backpack dictionary that stores the user's items and progress.

    Returns:
        None
    """

    # Display options and get user input
    print("\nWhat is your name?")
    name = input("Name: ")

    # Prints the name
    print(f"Your name is {name}.")

    # Adds the name to the backpack
    backpack["name"] = name

    # Ask if user wants to save name
    while True:
        save_name = input("Do you want to save your name? (y/n): ").lower()

        # If user chooses to save their name, call the save function
        if save_name == "y":
            print("SAVING NAME")
            save(backpack)
            break

        # If user chooses not to save their name, go back to menu
        elif save_name == "n":
            print("Your name will not be saved.")
            print("Going back to the menu.")
            menu()
            break

        # Invalid input
        else:
            print("Invalid input. Try again.")

# SAVE FUNCTION 
def save(backpack, filename='save.txt'):
    """Saves the backpack to a file.

    This function attempts to save the backpack dictionary to a file. If the file
    does not exist, it is created.

    Args:
        backpack (dict): The backpack to be saved.
        filename (str, optional): The filename to save to. Defaults to 'save.txt'.
    """

    # Create a timestamp for the save data
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Construct the data to be saved
    save_data = {'timestamp': timestamp, 'backpack': backpack}

    try:
        # Check if the file already exists
        if os.path.isfile(filename):
            # Make a backup of the existing file
            backup_filename = f'{filename}.bak'
            os.rename(filename, backup_filename)
            print(f'Existing save file backed up to {backup_filename}.')

        # Write the save data to the file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(str(save_data))
            print(f'Backpack saved to {filename}.')
        
        # Return to menu
        print("Going back to the menu")
        menu()

    except Exception as e:
        print(f'Error saving backpack: {e}')
        return

    return save_data

# GAME FUNCTION
def game(backpack):
    """Start the game and prompt the user to make a choice between two doors.

    Args:
        backpack (dict): The backpack
    """

    # Dialogue
    print("A man finds himself in a dark room...")
    print("There are two doors, one on his left and one on his right...")

    # Prompt the user to choose a door
    choice = input("\nWhich door did the man take? (left or right): ")
    
    # If the user chooses the left door
    if choice.lower() in ["left", "l"]:
        print("The man went through the left door...")
        rLeft(backpack, choice)

    # If the user chooses the right door
    elif choice.lower() in ["right", "r"]:
        print("\nThe man went through the right door...")
        rRight(backpack, choice)

    # Invalid input
    else:
        print("Invalid input. Please try again.")
        game(backpack)

# ROOM 1 LEFT 
def rLeft(backpack, choice):
    """Room 1 Left Function

    This function is used to navigate through the left room in the game. It presents the user with 3 options, 
    and based on the user's input, performs the corresponding action. The function also updates the user's backpack 
    based on the outcome of their choice.

    Args:
        backpack (dict): A dictionary representing the user's backpack
        choice (int): An integer representing the user's choice of action in the left room

    Returns:
        None
    """

    # Display dialogue and get user input
    print("\nThe man found himself in a room with a table, a bed, and a carpet.")
    print("The man chose to look under the...")
    print("1. Table")
    print("2. Bed")
    print("3. Carpet")
    choice = int(input("Choice: ")) 

    # TABLE OPTION
    if choice == 1: 
        # Update backpack and display teh changes
        print("\nThe man chose to look under the table and found a key and money.")
        print("\nKeys + 1")
        print("Money + 1000")
        backpack["keys"] += 1
        backpack["money"] += 1000
        time.sleep(10)
        moment2left(backpack, choice)

    # BED OPTION
    elif choice == 2: 
        print("\nThe man chose to lie down on the bed and fell asleep.")
        time.sleep(1)
        print("The man slept for 1 hour.")
        time.sleep(1)
        print("The man slept for 2 hours..")
        time.sleep(1)
        print("The man slept for 3 hours...")
        time.sleep(1)
        print("The man slept for  4 hours....")
        time.sleep(1)
        print("And on the 5th hour he woke up.\nFeeling refreshed he started looking again.")
        # Return to the beginning of the function
        rLeft(backpack, choice)

    # CARPET OPTION
    elif choice == 3: 
        # Update backpack and display the changes
        print("\nThe man chose to look under the carpet and found a trapdoor.")
        print("Unfortunately, for the man, the trapdoor was locked.")
        print("\nThe man got irritated and started looking again.")
        print("Irritation + 1")
        backpack["irritation"] += 1
        time.sleep(10)
        # Return to the beginning of the function
        rLeft(backpack, choice)

    # Invalid input
    else: 
        print("Invalid input. Try again.")
        rLeft(backpack, choice)

# MOMENT 2 LEFT
def moment2left(backpack, choice):
    """Moment 2 left function.

    This function is used to handle the situation when the man tries to open the trapdoor
    found in the previous room using the key he just obtained.

    It has 2 options:
    1. Go back to the menu
    2. Proceed to the next room

    If the trapdoor opens, the function goes to moment3left() function.
    If the trapdoor does not open, the function gives the man a second chance.

    Args:
        backpack (dict): A dictionary representing the player's inventory.
            The keys and irritation fields will be updated.
        choice (int): The user's input for the previous room.

    """

    # Dialogue and input
    print("\nThe man used the key to open the trapped door which magically appeared.")
    print("The man tried to turn the key in the lock.")

    # Random number 1-10
    trapdoorOpen = random.randint(1, 10) 

    # If the number is higher than 5 then the trapdoor opens, goes to moment3left
    if trapdoorOpen > 5:
        print("\nThe key turned and the trapdoor opened.")
        print("Keys - 1")
        backpack["keys"] -= 1
        time.sleep(10)
        moment3left(backpack, choice)

    # If the number is lower than 5 then the trapdoor does not open
    else:
        # If the irritation is 3 then it's game over
        if backpack["irritation"] == 3:
            print("\nThe man was too irritated and died of a heart attack.")
            print("GAME OVER")
            menu()
        # If the irritation is less than 3, then give the man a second chance
        else:
            # Dialogue and display changes
            print("\nThe key did not turn.")
            print("\nThe man got really irritated.")
            print("Irritation + 1")
            print("Keys - 1")
           
            # Irritation + 1 and keys - 1
            backpack["irritation"] += 1
            backpack["keys"] -= 1

            # Second chance to open the trapdoor
            print("\nThe man got a second chance to open the trapdoor.")
            time.sleep(10)
            moment2left(backpack, choice)

# MOMENT 3 LEFT
def moment3left(backpack, choice):
    """Simulate the moment when the player goes through the trapdoor and enters a room with a locked door.

    Args:
        backpack (dict): A dictionary containing information about the player's inventory, such as the amount of money,
            keys, and irritation level.
        choice (str): The choice made by the player.

    The function has two options:

    1. If the player has 100 or more money, the door opens and the player advances to moment 4 left.
    2. If the player has less than 100 money, the door remains locked and the game ends.

    If the player successfully opens the door, 100 money is subtracted from the player's inventory.

    If the player does not have enough money to open the door, the game exits.
    """

    # Display Dialogue
    print("\nThe man went through the trapdoor and found himself in a room with a door.")
    print("And on that door it said \"You have to have at least 100 money to open the door\".")

    # If the player has 100 or more money, open the door and call moment 4 left function
    if backpack["money"] >= 100:
        print("Fortunately for the man, he had enough money to open the door.")
        print("Money - 100")
        backpack["money"] -= 100
        time.sleep(10)
        moment4left(backpack, choice)
    
    # If the player has less than 100 money, the game ends
    else:
        print("The man was too poor to open the door, and the room flooded with mustard gas, killing him.")
        print("GAME OVER")
        exit()


# MOMENT 4 LEFT
def moment4left(backpack, choice): # MOMENT 4 LEFT
    """Moment 4 left function
    
    This function is used to go to the moment 4 left.
    It has 2 options.
    1. Go back to menu
    2. Go to the next room
    
    1. Goes back to menu
    2. Goes to the next room
    
    Args: 
        backpack (dict): The backpack
        choice (int): The choice
    """

    # Dialog
    print("\nWhen he opened the door he was in a dimly lit room with a pedestal in the middle.")
    print("He approached the pedestal and saw a book on it.")
    print("And that book was")
    
    # Book list
    book_list = ["FORTNITE (Official): Battle Royale Survival Guide", "Ben 10 Ultimate Alien Storybooks Collection (10 Books in Box Set). RRP £39.99 (Ultimate Alien) Paperback", "Batman: Batmans sons magiska äventyr"]
    
    # Random book choice from the Book list 
    book_choice = random.choice(book_list)

    # FORTNITE. Prints the book name and calls the fortniteRoom function
    if book_choice == book_list[0]: 
        print("\"FORTNITE (Official): Battle Royale Survival Guide\"")
        time.sleep(10)
        fortniteRoom(backpack, choice)

    # BEN 10. Prints the book name and calls the ben10Room function
    elif book_choice == book_list[1]: 
        print("\"Ben 10 Ultimate Alien Storybooks Collection (10 Books in Box Set). RRP £39.99 (Ultimate Alien) Paperback\"")
        time.sleep(10)
        ben10Room(backpack, choice)
    
    # Batman. Prints the book name and calls the batmanRoom function
    elif book_choice == book_list[2]: 
        print("\"Batman: Batmans sons magiska äventyr\"")
        time.sleep(10)
        batmanRoom(backpack, choice)
    
    # veti fan om jag behöver den här... fixa/gör klart
    else:
        print("ERROR") 
        exit()

# Room for the fortnite book
def fortniteRoom(backpack, choice):
    """Fortnite room function

    This function is used to go to the fortnite room.
    It has 2 options.
    1. Yes
    2. No

    1. Buys the book
    2. Does not buy the book

    Args:
        backpack (dict): The backpack
        choice (str): The choice
    """

    # Dialog
    print("\nDo you want to buy the book?")

    # Input for buying the book
    choice = input("Y/N: ")

    # Say yes to buying the book, adds the book to the dictionary under "items", displays the new item and calls the moment5left function
    if choice in ["Y", "y"]:
        print("You bought the book.")
        print("Money - 100")
        print("Items + 1")
        backpack["money"] -= 100
        backpack["items"].append("FORTNITE (Official): Battle Royale Survival Guide")
        print("You got a new item: \"FORTNITE (Official): Battle Royale Survival Guide\"")
        print(backpack["items"]) 
    
    # Say no to buying the book
    elif choice in ["N", "n"]:
        print("You did not buy the book.")
        print("It would seem that you are not intelligent enough to press \"Y\".")
        print("try again.")
        time.sleep(10)
        fortniteRoom(backpack, choice)
    
    # Invalid input
    else:
        print("Invalid input. Try again.")
        time.sleep(10)
        fortniteRoom(backpack, choice)
    
    # If the player has the book in the backpack, he wins the game and the game exits
    if "FORTNITE (Official): Battle Royale Survival Guide" in backpack["items"]:
        print("You just bought the best book in the world and spent the rest of your life reading it.")
        print("You won the game.")
        exit()

# Room for the ben10 book
def ben10Room(backpack, choice):
    """Ben 10 room function.
    
    This function is used to go to the Ben 10 room.
    It has two options:
    1. Buy the book
    2. Do not buy the book
    
    Args:
        backpack (dict): A dictionary representing the player's backpack.
        choice (str): The player's choice.
    """

    # Dialog
    print("Do you want to buy the book?")

    # Input for buying the book
    choice = input("Y/N: ")

    # Buy the book and add it to the backpack
    if choice.lower() == "y":
        print("You bought the book.")
        print("Money - 100")
        backpack["money"] -= 100
        book_title = "Ben 10 Ultimate Alien Storybooks Collection (10 Books in Box Set). RRP £39.99 (Ultimate Alien) Paperback"
        backpack["items"].append(book_title)
        print(f"You got a new item: \"{book_title}\"")
        print("Items + 1")
        print(backpack["items"])

    # Do not buy the book and try again
    elif choice.lower() == "n":
        print("You did not buy the book.")
        print("It seems that you are not intelligent enough to press \"Y\".")
        print("Try again.")
        time.sleep(10)
        ben10Room(backpack, choice)
    
    # Invalid input
    else:
        print("Invalid input. Try again.")
        time.sleep(10)
        ben10Room(backpack, choice)
    
    # If the player has the book in the backpack, they lose the game and the game exits
    if "Ben 10 Ultimate Alien Storybooks Collection (10 Books in Box Set). RRP £39.99 (Ultimate Alien) Paperback" in backpack["items"]:
        print("After reading all of the 10 books in the collection, you convinced yourself that you are Ben 10 and jumped off a building trying to turn into an alien.")
        print("You died.")
        print("GAME OVER")
        exit()

# Room for the batman book
def batmanRoom(backpack, buy_choice):
    """Batman room function
    
    This function is used to go to the batman room.
    It has 2 options.
    1. Yes
    2. No
    
    1. Buys the book
    2. Does not buy the book
    
    Args:
        backpack (dict): The backpack
        buy_choice (str): The choice to buy the book
    """

    # Dialog
    print("Do you want to buy the book?")

    # Input for buying the book
    choice = input("Y/N: ")

    # Say yes to buying the book, adds the book to the dictionary under "items"
    if choice.lower() == "y":
        print("You bought the book.")
        print("Money - 100")
        backpack["money"] -= 100
        print('You got a new item: "A Signed Copy Of Mein Kampf"')
        backpack["items"].append("A Signed Copy Of Mein Kampf")
        print("Items + 1")
        print(backpack["items"])
    
    # Say no to buying the book and try again. 
    elif choice.lower() == "n":
        print("You did not buy the book.")
        print('It seems that you are not intelligent enough to press "Y".')
        print("Try again.")
        time.sleep(10)
        batmanRoom(backpack, buy_choice)
    
    # Invalid input
    else:
        print("Invalid input. Try again.")
        time.sleep(10)
        batmanRoom(backpack, buy_choice)
    
    # While the player has the book in the backpack, they can read it and get arrested for reading it and the game ends.
    while True:
        print("Do you want to read a book?")
        read_choice = input("Y/N: ").lower()

        # If yes to reading the book, the game ends
        if read_choice == "y":
            print("You read the book.")
            print("Irritation - 1")
            backpack["irritation"] -= 1
            print("Unfortunately, you were in Germany where owning or reading Mein Kampf is illegal.")
            print("You got arrested and sentenced to life in prison.")
            print("The END")
            exit()
            
        # If no to reading the book, the game still ends.
        elif read_choice == "n":
            print("You did not read the book.")
            print("Irritation + 1")
            backpack["irritation"] += 1
            print("Unfortunately, you were in Germany where owning or reading Mein Kampf is illegal.")
            print("You got arrested and sentenced to life in prison.")
            print("The END")
            exit()
        
        # Invalid input
        else:
            print("Invalid input. Try again.")
            batmanRoom(backpack, buy_choice)

# Room 1 Right
def rRight(backpack, choice):
    """Room 1 Right function
    
    This function is used to go to the room 1 right.
    It has 2 options.
    1. Yes
    2. No
    
    1. Goes to the room 2 right
    2. Goes to the room 2 left
    
    Args:
        backpack (dict): The backpack
        choice (str): The choice
    """

    # Dialog
    print("\nAs the man enters the room, he finds himself in a dark room with a wizard standing in the middle.")
    print("The wizard says: 'I will give you a riddle, if you answer it correctly you will get a reward.'")

    # Generates a random number between 1-3 to pick between riddles
    riddle = random.randint(1, 3)

    # Ask riddles and get answer
    if riddle == 1:
        print("\nWhat has hands but can not clap?")
        answer = input("\nAnswer: ")
        correct_answer = "clock"
    
    # If the random number is 2, ask the second riddle
    elif riddle == 2:
        print("\nWhat has a head and a tail but no body?")
        answer = input("\nAnswer: ")
        correct_answer = "coin"
    
    # If the random number is 3, ask the third riddle
    else:
        print("\nWhat has a neck but no head?")
        answer = input("\nAnswer: ")
        correct_answer = "bottle"

    # Check if answer is correct and give reward or punishment
    if answer.lower() == correct_answer:
        print("\nThe wizard was impressed by the man's answer and gave him a reward.")
        print("\nMoney + 100")
        backpack["money"] += 100
        time.sleep(2)
    
    # If the answer is wrong, the game ends
    else:
        print("\nThe wizard was not impressed by the man's answer and gave him a punishment.")
        print("The punishment of DEATH!!!!!")
        print("You died.")
        print("The END")
        exit()

    # Dialog
    print("\nThe man sees two doors.")
    print("One on the right and one on the left.")
    print("Which door does the man choose?")

    # Ask for door choice
    choice = input("R/L: ")

    # Go to the corresponding moment
    if choice.lower() == "r":
        moment2right(backpack, choice)

    # ???
    elif choice.lower() == "l":
        moment2left(backpack, choice)

    # Invalid input
    else:
        print("Invalid input. Try again.")
        rRight(backpack, choice)
  
# Moment 2 right
def moment2right(backpack):
    """Moment 2 right function
    
    This function is used to go to the moment 2 right.
    It has 2 options.
    1. Yes
    2. No
    
    1. Goes to the room 2 right
    2. Goes to the room 2 left
    
    Args:
        backpack (dict): The backpack
    """
    
    # Dialog
    print("There is nothing here, only a door.")
    
    # Handle invalid input with a while loop
    while True:
        choice = input("Do you want to go through the door? (Y/N)").lower()
        if choice in ['y', 'n']:
            break
        print("Invalid input. Try again.")
        time.sleep(1)

    # If the player chooses to go through the door, the game ends.
    if choice == "y": 
        print("You went through the door.")
        print("Unfortunately for you, you walked into a door full of spikes. You died.")
        print("The END")
        exit()
    
    # If the player chooses not to go through the door, the game ends.
    elif choice == "n":
        print("You chose not to go through the door.")
        print("Unfortunately for you, a Venezuelan secret agent was hiding in the corner and stabbed you in the back. You died.")
        print("The END")
        exit()

# 100% needed
if 5 + 5 == 10:
    print("5 + 5 is indeed 10")
else:
    print("You are wrong")
    

menu(backpack)
choose_name(backpack)
game(backpack)
        