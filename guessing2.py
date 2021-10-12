scret=5
chance=5
print("you have 5 chances right ")
while chance>0:
    guess=int(input("enter a guessing num: "))
    if scret==guess:
        print("you won")
        break
    elif scret!=guess and chance==1:
        print("YOU loss game")
    else:
        print("try again")
    chance-=1
    print("you have left with " +str(chance)+" chances")
print("game over")