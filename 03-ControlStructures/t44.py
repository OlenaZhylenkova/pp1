num = int(input("num1: "))
numbers=[]
while num != 0:
    numbers.append(num)
    num=int(input("num:"))
 
sum=0
quantity = 0

for number in numbers: 
    sum+=number
    length=len(numbers)
    mean = sum/length

print(sum)
print(length)
print(mean)