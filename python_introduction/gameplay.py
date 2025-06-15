import random

secret_number = random.randint(1,15) 

while True :
    try:
        guess = int(input("enter  a number between 1 and 15: "))

        if guess < 1 or guess > 15:
            
            print ("enter a valid number")

        else:

            break
    except ValueError:
        print("❗ That's not a number. Try again.")

match guess:
       case number if number == secret_number:
        print("yay, you guessed right!")


       case _:
            print("better luck next time. ")
