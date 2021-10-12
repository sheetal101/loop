secret=4
chances=5
while chances>0:
    guess=int(input("guess a number: "))
    if secret==guess:
        print("your guess is correct")
        break
    elif secret!=guess and chances==1:
        print("You Loss the game")
    elif secret<guess:
        print("jo apne guess kiya vo bada hai Try again!")
    else:
        print("jo apne guess kiya vo chhota hai Try again!")
    chances-=1
print("game over")