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

# Round 
Round = 0


# Play Loop
Play = True

while Play:
    Round += 1
    print("\nRound", Round) 

    # Player 1's turn.
    print(f"{Player1_name} Turn!")
    action1 = (input("Choose an action: 1. Attack, 2. Heal, 3. shield bash, 4. Poison: "))

    # Input validations.
    while action1 not in ['1', '2', '3', '4']:
        print("Invalid action. Please choose 1, 2, 3 or 4")
        action1 = (input("Choose an action: 1. Attack, 2. Heal, 3. shield bash, 4. Poison: "))

    if action1 == '1':
      print(f"{Player1_name} Attacks!")
      time.sleep(.5) # Sleep delays the loop.
      Player1_attack = randint(1, 20) # Attacks for player 1 turn. As well as different scenarios depending on what number they roll.
    
      print(f"{Player1_name} Rolls: {Player1_attack}")
      if Player1_attack == 20:
        Hp2 -= 4
        time.sleep(.5) # Sleep delays the loop.
        print(f"{Player1_name} scores a critical hit!")
        time.sleep(.5) # Sleep delays the loop.
        print(f"{Player2_name} Hp: {Hp2}")
      elif Player1_attack >= 17:
        Hp2 -= 2
        time.sleep(.5) # Sleep delays the loop.
        print(f"{Player1_name} Hits {Player2_name} very hard!")
        time.sleep(.5) # Sleep delays the loop.
        print(f"{Player2_name} Hp: {Hp2}")
      elif Player1_attack >= 6:
        Hp2 -= 1
        time.sleep(.5) # Sleep delays the loop.
        print(f"{Player1_name} Hits {Player2_name}!")
        time.sleep(.5) # Sleep delays the loop.
        print(f"{Player2_name} Hp: {Hp2}")
      elif Player1_attack <= 6:
        Hp2 = Hp2
        time.sleep(.5) # Sleep delays the loop.
        print(f"{Player1_name} Swings and barely miss {Player2_name}! No one takes Damage.")
      elif Player1_attack <= 1:
        Hp1 -= 2
        time.sleep(.5) # Sleep delays the loop.
        print(f"{Player1_name} swings their sword backwards and accidentally cuts themselves! Critical Fail")
        time.sleep(.5) # Sleep delays the loop.
        print(f"{Player1_name} Hp: {Hp1}")
    elif action1 == '2':
       # Heal logic's (If you are healer)
       if Player1_Class_name == "Healer":
          time.sleep(.5)
          Heal = randint(1, 20)
          if Heal >= 20: 
            Hp1 += 4 # Heal 2 hp Might change! 
            time.sleep(.5)
            print(f"{Player1_name} heals themselves!")
            time.sleep(.5)
            print(f"{Player1_name} Hp: {Hp1}")
          elif Heal >= 17:
             Hp1 += 3
             time.sleep(.5)
             print(f"{Player1_name} heals themselves!")
             time.sleep(.5)
             print(f"{Player1_name} Hp: {Hp1}")
          elif Heal >= 12:
             Hp1 += 2
             time.sleep(.5)
             print(f"{Player1_name} heals themselves!")
             time.sleep(.5)
             print(f"{Player1_name} Hp: {Hp1}")
          elif Heal >= 8:
             Hp1 += 1
             time.sleep(.5)
             print(f"{Player1_name} heals themselves!")
             time.sleep(.5)
             print(f"{Player1_name} Hp: {Hp1}")
          elif Heal == 1:
             Hp2 += 2
             time.sleep(.5)
             print(f"{Player1_name} miss and accidentally heals {Player2_name}")
             time.sleep(.5)
             print(f"{Player2_name} Hp: {Hp2}")
       else: print(f"{Player1_name} cannot heal!")
    elif action1 == '3':
     if Player1_Class_name == "Warrior":
       print(f"{Player1_name} performs a shield bash!") # I'll fix so shield bash has a chance to stun. 
       time.sleep(.5)
       shield_bash_roll = randint(1, 20)
       if shield_bash_roll >= 15:
          Hp2 -= 2
       if Player2_Class_name == "Warrior":
          stun_chance = 0.5 # Aka 50% chance to stun warriors
       else:
          stun_chance = 0.8 # 80% chance to stun any other class.
       if randint(1, 10) <= int(stun_chance * 10):
          print(f"{Player2_name} is stunned!")
          Player2_stunned = True # Sets stun status to true.
      
          time.sleep(.5)
          print(f"{Player1_name} Hits {Player2_name}!")
          time.sleep(.5)
       else: print(f"{Player1_name}'s shield bash misses!")
     else: print("Only warriors can do that")
    elif action1 == '4':
       print(f"{Player1_name} uses poison!")
       time.sleep(.5)
       poison_roll = randint(1, 20)
       if poison_roll >= 12:
          time.sleep(.5)
          print(f"{Player1_name} successfully poisoned {Player2_name}!")
          time.sleep(.5)
       else: print(f"{Player1_name}'s poison was expired! nothing happens")

       print(f"{Player2_name}: {Hp2}")

    # Player 2's turn.
    print(f"{Player2_name} Turn!")
    action2 = (input("Choose an action: 1. Attack, 2. Heal, 3. shield bash, 4. Poison: "))

    # Input validations.
    while action2 not in ['1', '2', '3', '4']:
        print("Invalid action. Please choose 1, 2, 3 or 4")
        action2 = (input("Choose an action: 1. Attack, 2. Heal, 3. shield bash, 4. Poison: "))

    if action2 == '1':
      print(f"{Player2_name} Attacks!")
      time.sleep(.5) # Sleep delays the loop.
      Player2_attack = randint(1, 20) # Attacks for player 2 turn. As well as different scenarios depending on what number they roll.
    
      print(f"{Player2_name} Rolls: {Player2_attack}")
      if Player2_attack == 20:
        Hp1 -= 4
        time.sleep(.5) # Sleep delays the loop.
        print(f"{Player2_name} scores a critical hit!")
        time.sleep(.5) # Sleep delays the loop.
        print(f"{Player1_name} Hp: {Hp1}")
      elif Player2_attack >= 17:
        Hp1 -= 2
        time.sleep(.5) # Sleep delays the loop.
        print(f"{Player2_name} Hits {Player1_name} very hard!")
        time.sleep(.5) # Sleep delays the loop.
        print(f"{Player1_name} Hp: {Hp1}")
      elif Player2_attack >= 6:
        Hp1 -= 1
        time.sleep(.5) # Sleep delays the loop.
        print(f"{Player2_name} Hits {Player1_name}!")
        time.sleep(.5) # Sleep delays the loop.
        print(f"{Player1_name} Hp: {Hp1}")
      elif Player2_attack <= 6:
        Hp1 = Hp1
        time.sleep(.5) # Sleep delays the loop.
        print(f"{Player2_name} Swings and barely miss {Player1_name}! No one takes Damage.")
      elif Player2_attack <= 1:
        Hp2 -= 2
        time.sleep(.5) # Sleep delays the loop.
        print(f"{Player2_name} swings their sword backwards and accidentally cuts themselves! Critical Fail")
        time.sleep(.5) # Sleep delays the loop.
        print(f"{Player2_name} Hp: {Hp2}")
    elif action2 == '2':
       # Heal logic's (If you are healer)
       if Player2_Class_name == "Healer":
          time.sleep(.5)
          Heal = randint(1, 20)
          if Heal >= 20: 
            Hp1 += 4 # Heal 2 hp Might change! 
            time.sleep(.5)
            print(f"{Player2_name} heals themselves!")
            time.sleep(.5)
            print(f"{Player2_name} Hp: {Hp2}")
          elif Heal >= 17:
             Hp2 += 3
             time.sleep(.5)
             print(f"{Player2_name} heals themselves!")
             time.sleep(.5)
             print(f"{Player2_name} Hp: {Hp2}")
          elif Heal >= 12:
             Hp2 += 2
             time.sleep(.5)
             print(f"{Player2_name} heals themselves!")
             time.sleep(.5)
             print(f"{Player2_name} Hp: {Hp2}")
          elif Heal >= 8:
             Hp2 += 1
             time.sleep(.5)
             print(f"{Player2_name} heals themselves!")
             time.sleep(.5)
             print(f"{Player2_name} Hp: {Hp2}")
          elif Heal == 1:
             Hp1 += 2
             time.sleep(.5)
             print(f"{Player2_name} miss and accidentally heals {Player1_name}")
             time.sleep(.5)
             print(f"{Player1_name} Hp: {Hp1}")
       else: print(f"{Player2_name} cannot heal!")
    elif action2 == '3':
     if Player2_Class_name == "Warrior":
       print(f"{Player2_name} performs a shield bash!") # I'll fix so shield bash has a chance to stun. 
       time.sleep(.5)
       shield_bash_roll = randint(1, 20)
       if shield_bash_roll >= 15:
          Hp1 -= 1
          time.sleep(.5)
          print(f"{Player2_name} Hits {Player1_name}!")
          time.sleep(.5)
       else: print(f"{Player2_name}'s shield bash misses!")
     else: print("Only warriors can do that")
    elif action2 == '4':
       print(f"{Player2_name} uses poison!")
       time.sleep(.5)
       poison_roll = randint(1, 20)
       if poison_roll >= 12:
          time.sleep(.5)
          print(f"{Player2_name} successfully poisoned {Player1_name}!")
          time.sleep(.5)
       else: print(f"{Player2_name}'s poison was expired! nothing happens")


    # Prints HP at the end of each round.
    print(f"{Player1_name} Hp: {Hp1}")
    print(f"{Player2_name} Hp: {Hp2}")

    time.sleep(1) # Sleep delays the loop for 1 sec.

    if Hp1 <= 0:
        print(f"{Player2_name} Wins!") # Who wins and end of loop
        Play = False 
    elif Hp2 <= 0:
        print(f"{Player1_name} Wins!")
        Play = False
