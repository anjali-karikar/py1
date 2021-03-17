import random
comp = random.randint(1, 3) 

# print (comp)

player = int(input("Enter your input \n 1 for STONE \n 2 for PAPER \n 3 for SCISSOR  : \n\n"))
# print(player)

if (player==1 or player==2 or player==3):
    # print ("YOU : ",player)
    pass
else:
    print("INVALID INPUT ")

if(comp==1):
    computer="STONE"
elif(comp==2):
    computer="PAPER"
elif(comp==3):
    computer="SCSSIOR"

print("COMPUTER : ",computer)

if(comp==player):
    print("YOU : ",computer)
    print("HURREY !!! TIE BETWEEN YOU AND COMPUTER")
elif(comp==1):
    if(player==2):
        print("YOU : PAPER")
        print("YOU WON ! CONGRADULATIONS !!!")
    elif(player==3):
        print("YOU : SCISSOR")
        print("YOU LOST")

elif(comp==2):
    if(player==3):
        print("YOU : SCISSOR")
        print("YOU LOSTYOU WON ! CONGRADULATIONS !!!")
    elif(player==1):
        print("YOU : STONE")
        print("YOU LOST")

elif(comp==3):
    if(player==1):
        print("YOU : STONE")
        print("YOU LOSTYOU WON ! CONGRATULATIONS !!!")
    elif(player==2):
        print("YOU : PAPER")
        print("YOU LOST")


print("\n0(@..@)0")
print(" (----) ")
