import random
import string
from colorama import Back, Fore, Style
#colorama for the aesthetics, optional

num_letters = 3
para = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
random_letters = random.choices(para, k=num_letters)
random_string = "".join(random_letters)
print(random_string)

correctanswer = random_string
guess = random.choices(para, k=num_letters)
if guess != correctanswer:
    while guess != correctanswer:
        print(Fore.GREEN + "".join(guess))
        guess = ''.join(random.choices(para, k=num_letters))
        if guess == correctanswer:
            print(f"Correct answer: {guess}")