import random
#導入函式庫 random 不成文規定要放最上面

upper = 100
under = 1

ans = random.randint(under,upper)
#隨機整數，並且設定範圍

#終極密碼可以輸入多次
for i in range(10):
    guess = int(input("請輸入數字："))

    if guess < ans:
        under = guess
        print(under , upper)
    elif guess > ans :
        upper = guess
        print(under , upper)
    else :
        print ("Congrats") 
        break
    #break跳出迴圈

