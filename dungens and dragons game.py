import random
import time

# Player initialization
player_name = input("Enter your character's name: ")
player_health = random.randint(50, 100)
player_attack = random.randint(10, 20)
player_defense = random.randint(5, 15)
player_level = 1
experience = 0
gold = 0
inventory = []

# Game variables
enemies_defeated = 0
locations_visited = 0

print(f"Welcome to the Dungeons and Dragons Adventure, {player_name}!\n")

# Main game loop
while player_health > 0:
    # Location initialization
    locations = ["Dark Forest", "Mystic Cavern", "Haunted Castle", "Enchanted Lake"]
    current_location = locations[locations_visited % len(locations)]
    locations_visited += 1

    print(f"\n{player_name}, you are now in the {current_location}!\n")

    # Random event
    if random.randint(1, 10) <= 3:
        print("You found a hidden chest!")
        loot = random.choice(["Health Potion", "Sword", "Shield", "Gold Coin"])
        print(f"You obtained: {loot}")
        inventory.append(loot)

    # Encounter initialization
    enemy_name = random.choice(["Orc", "Dragon", "Goblin", "Wizard"])
    enemy_health = random.randint(30 + player_level * 5, 70 + player_level * 5)
    enemy_attack = random.randint(8 + player_level, 15 + player_level)
    enemy_defense = random.randint(3 + player_level, 10 + player_level)

    print(f"A wild {enemy_name} appears!\n")

    # Battle loop
    while enemy_health > 0:
        # Display status
        print(f"\n{player_name}, Level {player_level}")
        print(f"Health: {player_health} | Attack: {player_attack} | Defense: {player_defense}")
        print(f"{enemy_name}'s Health: {enemy_health}\n")

        # Player's turn
        print("What will you do?")
        print("1. Attack")
        print("2. Use Item")
        print("3. Run away")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            # Player attacks enemy
            damage = max(0, player_attack - enemy_defense)
            enemy_health -= damage
            print(f"{player_name} attacks {enemy_name} for {damage} damage!")

        elif choice == "2":
            # Use item from inventory
            if not inventory:
                print("Your inventory is empty.")
            else:
                print("Inventory:")
                for item in inventory:
                    print(f"- {item}")
                use_item = input("Enter the item you want to use: ")
                if use_item in inventory:
                    if use_item == "Health Potion":
                        player_health += 20
                        print(f"{player_name} used a Health Potion and gained 20 health!")
                        inventory.remove("Health Potion")
                    elif use_item == "Sword":
                        player_attack += 5
                        print(f"{player_name} equipped a Sword and gained 5 attack!")
                        inventory.remove("Sword")
                    elif use_item == "Shield":
                        player_defense += 3
                        print(f"{player_name} equipped a Shield and gained 3 defense!")
                        inventory.remove("Shield")
                    elif use_item == "Gold Coin":
                        gold += 10
                        print(f"{player_name} found 10 gold coins!")
                        inventory.remove("Gold Coin")
                else:
                    print("Invalid item. Try again.")

        elif choice == "3":
            print("You run away from the battle. Coward!")
            break

        else:
            print("Invalid choice. Try again.")
            continue

        # Enemy's turn
        if enemy_health > 0:
            player_damage = max(0, enemy_attack - player_defense)
            player_health -= player_damage
            print(f"{enemy_name} attacks {player_name} for {player_damage} damage!")

        # Pause to make the game flow more naturally
        time.sleep(1)

    if player_health > 0:
        print(f"\nYou defeated the {enemy_name}!")
        enemies_defeated += 1
        experience += 20
        gold += random.randint(5, 15)
        print(f"{player_name} gained 20 experience points and found {gold} gold!\n")

        # Level up if enough experience points
        if experience >= player_level * 50:
            player_level += 1
            player_health += 10
            player_attack += 5
            player_defense += 3
            print(f"Congratulations! {player_name} leveled up to Level {player_level}!\n")

print(f"\nGame Over. {player_name} defeated {enemies_defeated} enemies, reached Level {player_level}, and collected {gold} gold.")
