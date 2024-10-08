#
#       project: HundredLinesOfCode.py
#        author: Christian Rios <crios2703019@woonsocketschools.com>
#  date written: 09/4/2024
#
#   description: learning python day 17")

counter1 = 0
counter2 = 0
round = 1
isPlaying = True
print("=== ROCK PAPER SCISSORS ===")
while isPlaying:
    print ("Players can either choose R, P, S. FIRST TO 3, begin")
    print("ROUND",round)
    player1 = input("Player 1 : ")
    player2 = input("Player 2 : ")
    #print("DEBUG",counter1,counter2)

    if player1 == "R" and player2 == "S" or player1 == "S" and player2 == "P" or player1 == "P" and player2 == "R":
        print("PLAYER 1 WINS THIS ROUND")
        counter1 += 1
        round += 1

    elif player2 == "R" and player1 == "S" or player2 == "S" and player1 == "P" or player2 == "P" and player1 == "R":
        print("PLAYER 2 WINS THIS ROUND")
        counter2 += 1
        round += 1

    elif (player2 == "R") and (player1 == "R") or (player2 == "S") and (player1 == "S") or (player2 == "P") and (player1 == "P"):
        print("TIE RESTART THE ROUND")

    else:
        print("Im not sure I understand try again.")


    if counter1 == 3:
        print("player 1 WINS the score was",counter1,"-",counter2)
        leave = input("If you want to close game press Y otherwise game will continue : ")
        if leave == "Y":
            print("Come Back Soon!")
            break
        else:
            round = 1
            counter1 = 0
            counter2 = 0


    if counter2 == 3:
        print("player 2 WINS the score was", counter1, "-", counter2)
        leave = input("If you want to close game press Y otherwise game will continue : ")
        if leave == "Y":
            print("Come Back Soon!")
            isPlaying = False
        else:
            round = 1
            counter1 = 0
            counter2 = 0
