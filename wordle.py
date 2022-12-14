import random

with open ("words.txt") as f:
    dictionary = f.read().splitlines()
answer = random.choice(dictionary)

print (answer)


count = 5
while count > 0 :

    guess = input(f"Type your guess : ")

    result = ""

    for i in range(5):
        # 是否相等
        if guess[i] == answer[i]:
            result = result + 'A'
        # 是否存在
        elif guess[i] in answer:
            result = result + 'B'
        # 都不存在
        else :
            result = result + 'X'

    if result == "AAAAA":
        print("Correct!")
        break

    print (result)

    count = count -1
