from random import randint

# Players name
Player1_name = (input("Player One Name: "))
Player2_name = (input("Player Two Name: "))


# Round and Hp
Round = 0

Hp1 = 10
Hp2 = 10


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
    if Player1_attack > Player2_attack:
        print(f"{Player1_name} Hits!")
        Hp2 -= 1
        
    else: 
        print(f"{Player2_name} Hits!")
        Hp1 -= 1

    # Prints HP
    print(f"{Player1_name} : {Hp1}")
    print(f"{Player2_name} : {Hp2}")

    if Hp1 <= 0:
        print(f"{Player2_name} Wins!")
    elif Hp2 <= 0:
        print(f"{Player1_name} Wins!")
    Play = False

