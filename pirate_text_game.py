import random

# Function to display the opening message
def game_intro():
    print("\nWelcome to the Pirate's Treasure Hunt!")
    print("-----------------------------------")
    print("You find yourself on a mysterious island with a map in hand.")
    print("The map reveals 5 hidden islands, each with a treasure chest or danger.")
    print("Be cautious! There are rumors of ambushes set by the East India Company and Scavengers.")
    print("Your mission is to find the treasures and escape without falling into a trap.")
    print("You can input commands like: 'walk', 'search', 'go to <island>', and 'map'.")
    print("If you land on an ambush island, you must roll a dice. Roll 4 or higher to survive!")
    print("Let's begin your adventure!\n")
    return

# Dictionary to store island names and their treasures
islands_treasures = {
    "Treasure Island": "Gold Coin",
    "Mystical Island": "Enchanted Pearl",
    "Cursed Island": "Ruby of Riches",
    "Whispering Island": "Silver Crown",
    "Forgotten Island": "Diamond Skull",
}

# Randomly assign two ambush islands
island_names = list(islands_treasures.keys())
ambush_islands = random.sample(island_names, 2)
east_india_ambush = ambush_islands[0]
scavenger_ambush = ambush_islands[1]

# Variable to track the current island
current_island = "Nassau"  # The game starts from 'Nassau' the capital of pirates

# Function to display the map with hints
def display_map():
    print("\nMap of the Islands:")
    print("-------------------")
    for island in islands_treasures.keys():
        if island == east_india_ambush:
            print(f"- {island} (You notice suspiciously organized camps nearby...)")
        elif island == scavenger_ambush:
            print(f"- {island} (Signs of chaotic looting and abandoned rafts are seen here...)")
        else:
            print(f"- {island}")
    print("- Nassau (you are here)\n")
    return

# Dice roll function for ambush islands
def roll_dice():
    roll = random.randint(1, 6)  # Roll a 6-sided dice
    print(f"\nYou rolled a {roll}.")
    return roll

# Game loop function
def game_loop():
    global current_island
    treasures_collected = 0

    while True:
        user_input = input(f"{current_island}:> ").lower().strip()

        # Command to quit game
        if user_input == "quit":
            print("\nThanks for playing! Come back soon for more adventure!")
            break

        # Command to display the map
        elif user_input == "map":
            display_map()

        # Command to walk around
        elif user_input == "walk":
            print("You walk around the island. Nothing exciting happens.")

        # Command to search for treasure
        elif user_input == "search":
            if current_island == east_india_ambush:
                print("You are ambushed by the East India Company! Time to roll the dice to see if you survive!")
                roll = roll_dice()
                if roll < 4:
                    print("You rolled less than 4! The East India Company catches you, and you lose everything!")
                    print("Game Over!")
                    break
                else:
                    print("You rolled 4 or higher! You survive the ambush and can continue your adventure!")
                    current_island = "Nassau"  # Return to Start Island after surviving
            elif current_island == scavenger_ambush:
                print("You fall into a Scavenger ambush! Time to roll the dice to see if you survive!")
                roll = roll_dice()
                if roll < 4:
                    print("You rolled less than 4! The Scavengers overwhelm you and steal all your treasure!")
                    print("Game Over!")
                    break
                else:
                    print("You rolled 4 or higher! You escape the Scavengers and can continue your adventure!")
                    current_island = "Nassau"  # Return to Start Island after surviving
            elif current_island in islands_treasures:
                print(f"You found the {islands_treasures[current_island]}!")
                del islands_treasures[current_island]
                treasures_collected += 1

                # Check if all treasures have been collected
                if treasures_collected == 5:
                    print("Congratulations! You've collected all the treasures and can now sail off to live a life of luxury!")
                    break
            else:
                print("You search everywhere but couldn't find any treasure.")

        # Command to go to an island
        elif user_input.startswith("go to "):
            destination = user_input[6:].title()  # Capitalize to match island names
            if destination in islands_treasures.keys() or destination == "Start Island":
                current_island = destination
                print(f"You set sail to {current_island}.")
            else:
                print(f"There is no island called '{destination}'. Check your map!")

        # Invalid command
        else:
            print("Invalid command. Please try again.")

# Start the Game
game_intro()
game_loop()
