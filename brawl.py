from random import randint # Imports randint for random attacks
import time # Imports time so i can use time.sleep to make a delay after each round

# Players name
Player1_name = (input("Player One Name: "))
Player2_name = (input("Player Two Name: "))

# Classes And their Hp
class_hp = {
    "Peasant": 10,
    "Warrior": 15,
    "Healer": 10,
    "Thief": 8,
    "American": 20
}
# Player Hp
Hp1 = 0
Hp2 = 0


print(f"{Player1_name} choose your class: 1. Peasant, 2. Warrior, 3. healer, 4. Thief, 5. American")

# Assign class base on input
Player1_Class = int(input("Class: ")) # Converts to integer.
if Player1_Class == 1: 
    Player1_Class_name = "Peasant"
elif Player1_Class == 2:
    Player1_Class_name = "Warrior"
elif Player1_Class == 3:
    Player1_Class_name = "Healer"
elif Player1_Class == 4:
    Player1_Class_name = "Thief"
elif Player1_Class == 5:
    Player1_Class_name = "American"
print(f"{Player1_name} chose {Player1_Class_name}!")

Hp1 = class_hp[Player1_Class_name] # Assigns Hp from Class_hp according to class name. Table to Player1_Class_name

print(f"Now {Player2_name} Choose your class: 1. Peasant, 2. Warrior, 3. healer, 4. Thief, 5. American")

Player2_Class = int(input("Class: ")) # Converts to integer.
if Player2_Class == 1: # assign Class and Hp accordingly.
    Player2_Class_name = "Peasant"
elif Player2_Class == 2:
    Player2_Class_name = "Warrior"
elif Player2_Class == 3:
    Player2_Class_name = "Healer"
elif Player2_Class == 4:
    Player2_Class_name = "Thief"
elif Player1_Class == 5:
    Player1_Class_name = "American"
print(f"{Player2_name} chose {Player2_Class_name}!")

Hp2 = class_hp[Player2_Class_name]

# Round and Hp
Round = 0


# Play Loop
Play = True

while Play:
    Round += 1
    print("\nRound", Round) 

    # Random Attacks
    Player1_attack = randint(1, 20)
    Player2_attack = randint(1, 20)
    print(f"{Player1_name}: {Player1_attack}")
    print(f"{Player2_name}: {Player2_attack}")

    # Who Hits And Dmg
    if Player1_attack == Player2_attack:
        Hp =+-1 
        print("Attacks where parried no one takes Dmg!")
    elif Player1_attack > Player2_attack:
        print(f"{Player1_name} Hits!")
        Hp2 -= 1
        
    else: 
        print(f"{Player2_name} Hits!")
        Hp1 -= 1

    # Prints HP
    print(f"{Player1_name} Hp: {Hp1}")
    print(f"{Player2_name} Hp: {Hp2}")

    time.sleep(1) # Sleep delays the loop for 1 sec.

    if Hp1 <= 0:
        print(f"{Player2_name} Wins!")
        Play = False 
    elif Hp2 <= 0:
        print(f"{Player1_name} Wins!")
        Play = False
