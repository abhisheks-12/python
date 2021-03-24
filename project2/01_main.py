import random
randoNum = random.randint(1,100)
user_guess = None
guess_no = 0
print(randoNum)

while (user_guess != randoNum):

    user_guess = int(input("Enter the number: "))
    guess_no = guess_no + 1

    if user_guess == randoNum:
        print("You are right!")
    
    else:
        if user_guess > randoNum:
            print("You are wrong! guess smaller number.")
        else:
            print("you are wrong ! guess larger number.")

print(f"You guessed in {guess_no} guesses.")


with open("highscore.txt","r") as f:
    hiscore = int(f.read())


if (user_guess < hiscore):
     print("You just broke highscore.")
     with open("highscore.txt","r") as f:
         f.write(str(user_guess))






