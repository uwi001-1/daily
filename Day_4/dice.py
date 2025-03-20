#two players with one dice
#rolls turn by turn
#total score 50 wins 
#6 reroll    3 times then 18 becomes 0     3 after remove power

import random

def roll():     #Generate random number between 1 and 6
    num = random.randint(1,6)
    return num

def game():         #Rolls the dice and return the score 
    take1 = roll()      #First Roll
    print(f"GOT:  {take1}")

    #if not 6 then return roll1
    if take1 !=6:    
        return take1 
    else:
        take2 = roll()    #Second Roll
        print("Rolled again.")
        print(f"GOT:  {take2}")

        #if not 6 then return roll1 + roll2
        if take2 !=6:  
            return take1 + take2
        else:
            take3 = roll()   #Third Roll
            print("Rolled again.")
            print(f"GOT:  {take3}")

            #if not 6 then return roll1 + roll2 + roll3
            if take3 !=6:    
                return take1 + take2 + take3
            else:    #if 3 consecutive 6 then return 0
                return 0

def score():
    s1 = 0
    s2 = 0
    while True:   #Choose who will start the game
        try:
            turn = int(input("Enter who wants to play first (1 or 2): "))
            if turn in [1, 2]:
                break
            else:
                print("Invalid input. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")

    #Loop till the someone wins
    while s1<50 or s2<50:
        if turn ==1:
            print(f"{player1}'s turn. ")
            output = game()
            s1 += output
            if s1 >= 50:
                break
            turn = 2    #next turn
        else:
            print(f"{player2}'s turn. ")
            output = game()
            s2 += output
            if s2 >= 50:
                break
            turn = 1     #next turn
    
    if s1 >= 50:
        print(f"{player1} won the game with score: {s1}")
        print(f"While {player2}'s score was {s2}")
    else:
        print(f"{player2} won the game with score: {s2}")
        print(f"While {player1}'s score was {s1}")


player1 = input("Enter the first player:  ").strip()
player2 = input("Enter the second player:  ").strip()
score()