from random import randint # Imports randint for random attacks
import time # Imports time so i can use time.sleep to make a delay after each round

# Players name
Player1_name = (input("Player One Name: "))
Player2_name = (input("Player Two Name: "))

WarriorClass = (4)
HealerClass = (3)
ThiefClass = (2)
PeasantClass = (1)

print(f"{Player1_name} choose your class: 1. Peasant, 2. Warrior, 3. healer, 4. Thief")

Player1_Class = (input("Class: "))
if Player1_Class == 1:
    print(f"{Player1_Class} Great choice!")
print(f"Now {Player2_name} Choose your class: 1. Peasant, 2. Warrior, 3. healer, 4. Thief")
print(f"{Player2_name} Great choice!")
Player2_Class = (input("Class: "))

#Classes Hp
WarriorHp = 15
HealerHp = 10
ThiefHp = 8

# Round and Hp
Round = 0

# Peasant class
PeasantHp1 = 10
PeasantHp2 = 10

Hp1 = Player1_Class
Hp2 = Player2_Class

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

    time.sleep(1) # Sleep delays the code for 1 sec.

    if Hp1 <= 0:
        print(f"{Player2_name} Wins!")
        Play = False 
    elif Hp2 <= 0:
        print(f"{Player1_name} Wins!")
        Play = False
