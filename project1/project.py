import random

def victory(comp,you):
    
    if comp == you:
        return None

    elif comp == "w":
        if you == "g":
            return False
        elif you == "s":
            return True

    elif comp == "s":
        if you == "w":
            return False
        elif you == "g":
            return True

    elif comp == "g":
        if you == "s":
            return False
        elif you == "w":
            return True





print("Computers turn: snake(s),water(w) or gun(g)")
random_no = random.randint(1,3)

if random_no == 1:
    comp = "s"

elif random_no == 2:
    comp = "w"

elif random_no == 3:
    comp = "g"


you = input("Your's turn: snake(1) , water(2) or gun(3):  ")


a = victory(comp,you)
print(f"Computer choose {comp}")
print(f"You choose {you}")


if a == None:
    print("Tie")

elif a:
    print("You win")

else:
    print("You lost!")
