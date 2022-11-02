my_name = "Teresa"
my_age = "1"
my_age = int(my_age)
#轉換型態
my_var = 10 
is_male = True



print("Hello,I'm " + my_name)
#print(type(my_age))看型態
print("->" + str(my_var))
#印出的時候轉換型態
print(10 + 6) #16
print(10 - 6) #4
print(10 * 6) #60
print(10 / 6) #1.666666
print(10 // 6) #1 取整數
print(10 % 6) #4 取餘數

a = 2
print(a < 5)
print(a > 5)
print(a == 5)
print(a <= 2)
print(a >= 5)
print(a >= 1 and a <= 10)
print(a >= 1 or a >= 10)
#不等式運算，回應是否成立 True / False

temperature  = 35

if temperature >= 30 :
    print("今天很熱！")
elif temperature < 20:
    print("今天很冷")
else :
    print("天氣很正常")
#if 判斷式
#如果你沒有縮排，就代表他不在判斷式裡面

my_List = [ 2 , 4 , 6 , 8]
my_List_a = ["A","B","C","D"]

print(my_List[2])
print(my_List_a[0])
#列表 從第0位開始

for item in my_List_a :
    print(item)
for item in my_List_a [2:]:
    print(item)
#從2開始列出來


my_List_b = [10 , 32 , 20, 50 , 70 , 10 , 80 ,100]

count = 0 
for item_b in my_List_b :
    if item_b >= 60 :
        count = count + 1
print(count)
#計算列表中有多少成績及格


for i in range(2,len(my_List_b),2 ):
    print(my_List_b[i])