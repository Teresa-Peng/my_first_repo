import random

low_bound = 1
up_bound = 100


answer = random.randint(low_bound,up_bound)

count = 5
while count > 0 :
    guess = int (input(f"Type your guess ({low_bound}~{up_bound}): "))

    if guess < answer:
        low_bound = guess
    elif guess > answer :
        up_bound = guess
    else :
        print ("You're correct!") 
        break

    count = count -1

