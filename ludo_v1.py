"""
Samuel Nawar Lototo
Tracy Atieno Achieng
Calvin Mac-Philips
Kimberly Taj Mashanga
Obadiah Safi"""


import random
#initializations.........................................
yellow = 0
red = 0
#number of steps for a piece to move to complete the game
target = 57

# function for player one
def yellow_turn():
    #initialize global variable to accumulate steps.
    global yellow 
    if yellow == 0:
        #Ask yellow to type R1 to begin.
        player1 = input("Type R1 to begin:  ").upper()
        # if the user does not input R! ask again.
        while player1 != "R1" :
            player1 = str(input("Type R1 to begin: " ).upper())
        if player1 == "R1" :
            #toss the dice to get a number between 1 and 6
            Value1 = random.randint(1,6)
            #if player1 gets 6 piece comes out.
            if Value1 == 6:
                print("Congratulation your yellow piece is out!!!")
                print("you had",Value1,"you can now move")
                yellow = 1
            else:
                print("You had", Value1,"wait for your turn")
        # If the user does not type R1 ask again.
        else:
            player1 = input("Type R1 to begin: " ).upper() 
    if yellow != 0:
        player1 = input("Type R1 to continue: ").upper()
        while player1 != "R1" :
            player1 = str(input("Type R1 to begin: " ).upper())
        if player1 == "R1":
            Value1 = random.randint(1,6)
        #if player1 gets 6 play again.   
        while Value1 == 6:
            print("player1 had", Value1)
            yellow = yellow + Value1
            #check if player 1 has won the game.
            if yellow == target:
                print("Yellow player wins!")
                # remain at current position if number rolled from the dice exceeds target
            elif yellow > target:
                yellow = yellow - Value1
                print("exceeded number of steps, wait for your turn")
            print("player1 has moved a total of: ",yellow,"steps")
            print("Player 1 has", target - yellow,"steps remaining")
            player1 = input("Type R1 to continue playing: ")
            Value1 = random.randint(1,6)
            
     # show the number rolled when player1 does not get a 6
        print("player1 did not get a 6")
        print("player1 had a",Value1)
        yellow = yellow + Value1
        if yellow == target:
            print("Yellow player wins!")
        elif yellow > target:
            yellow = yellow - Value1
            print("exceeded number of steps, wait for your turn")
        print("player1 has moved a total of :", yellow,"steps")
        print("player1 has", target - yellow," steps remaining")
        

        
def red_turn():
    global red
    if red == 0:
        #Ask red to type R1 to begin.
        player2 = input("Type R2 to begin:  ").upper()
        while player2 != "R2" :
            player2 = str(input("Type R2 to begin: " ).upper())
        if player2 == "R2" :
            #toss the dice to get a number between 1 and 6
            Value2 = random.randint(1,6)
            #if player1 gets 6 piece comes out.
            if Value2 == 6:
                print("Congratulation your red piece is out!!!")
                print("you had",Value2,"you can now move")
                red = 1
            else:
                print("Sorry, you had", Value2,"wait for your turn")
        # If the user does not type R2 ask again.
        else:
            player2 = input("Type R2 to begin: " ).upper() 

    if red != 0:
        player2 = input("Type R2 to continue: ").upper()
        #Continue to ask player 2 to Type R2 to continue
        while player2 != "R2" :
            player2 = str(input("Type R2 to begin: " ).upper())
        if player2 == "R2":
            Value2 = random.randint(1,6)
        #if player2 gets 6 play again and accumulate numbers obtained from both rolls.
            while Value2 == 6 :
                print("player2 had", Value2)
                red = red + Value2
                # red is equal to target, player 1 wins
                if red == target:
                    print("Red player wins!")
                # if it exceeds , remain at the same place.
                elif red > target:
                    red = red - Value2
                    print("exceeded number of steps, wait for your turn")
                
                print("player2 has moved a total of: ",red,"steps")
                print("Player 2 has", target - red,"steps remaining")
                player2 = input("Type R2 to continue playing: ")
                Value2 = random.randint(1,6)
            
        print("player2 did not get a 6")
        print("player2 had a value of: ", Value2)
        red = red + Value2
        if red == target:
            print("Red player wins!")
        elif red > target:
            red = red - Value2
            print("exceeded number of steps, wait for your turn")
        print("player2 has moved a total of :", red,"steps")
        print("player2 still has", target - red," steps remaining")
        
        
# function for game flow
def ludo():
    while True:
        # end the game when player1 wins
        yellow_turn()
        if yellow == target:
               print("Yellow player wins!")
               break
               
           
# end the game when player2 wins
        red_turn()
        if red == target:
               print("Red player wins!")
               break
           
       
            
# function call
ludo()