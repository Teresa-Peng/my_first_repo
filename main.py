#print("Hello NTUE!!")

my_var = 4 
if my_var > 5 : 
    print ("Ture")
else :
    print("False") 

my_list = [1,3,5,7,8]
print(my_list[0])
#取出矩陣的數值
for item  in my_list:
    print(item)
#印出矩陣的所有項目

#[0,1,2,3,4,5,6,7,8,9]
for i in range(10):
    print(i)
#range會直接給我所有資料(0-9),執行10次

my_sum = 0
for i in range(10):
    my_sum = my_sum + i
print(my_sum)
#累加

#開檔案(input.txt)方式
# f只是一個變數
# splitlines把每一筆資料切開來，過濾掉換行符號
with open ("input.txt") as f :
    content = f.read().splitlines()
print(content)

my_sum_input = 0
for item in content:
    my_sum_input = my_sum_input + int(item)
print(my_sum_input)
#將檔案資料轉換成int，才能相加

#for index , item in enumerate(content):
#    content[index] = int item
#for i in range(len(content)) :
#    content[i] = int(content[i])