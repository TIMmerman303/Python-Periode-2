print("Hello Periode 2!")

player_name = input("What is your name? ")
player_gold = 100
inventory = []

print(f"Welcome {player_name}! You have {player_gold} gold.")

shop_items = ["1. Buy Sword (50 gold)", "2. Buy Shield (40 gold)", "3. Buy Potion (20 gold)", "4. Buy Bow (60 gold)"]

while True:
    print("\n=== Fantasy Item Shop ===")

    for item in shop_items:
        print(item)

    print("5. View Inventory")
    print("6. Exit Shop")

    keuze = input("\nWhat would you like to do? ")

    match keuze:
        case "1":
            if player_gold >= 50:
                player_gold -= 50
                inventory.append("Sword")
                print(f"You bought a Sword! Gold left: {player_gold}")
            else:
                print("Not enough gold!")

        case "2":
            if player_gold >= 40:
                player_gold -= 40
                inventory.append("Shield")
                print(f"You bought a Shield! Gold left: {player_gold}")
            else:
                print("Not enough gold!")

        case "3":
            if player_gold >= 20:
                player_gold -= 20
                inventory.append("Potion")
                print(f"You bought a Potion! Gold left: {player_gold}")
            else:
                print("Not enough gold!")

        case "4":
            if player_gold >= 60:
                player_gold -= 60
                inventory.append("Bow")
                print(f"You bought a Bow! Gold left: {player_gold}")
            else:
                print("Not enough gold!")

        case "5":
            if len(inventory) == 0:
                print("Your inventory is empty!")
            else:
                print("Your inventory:")
                for item in inventory:
                    print(f"- {item}")

        case "6":
            print(f"Thanks for visiting the shop, {player_name}! Gold left: {playergold}")
            break

        case :
            print("Invalid option! Please choose 1 to 6.")