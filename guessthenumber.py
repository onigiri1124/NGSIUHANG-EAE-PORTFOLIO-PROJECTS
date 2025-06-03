import random
import time

number = random.randrange(0,1,1)

print("guess the number")
guess= int(input("guess: "))

if guess == number:
    print("congrats!")
else:
    print("aww shucks! Try again?")
    time.sleep(1)
    print(f"the number was actually {number}!")
