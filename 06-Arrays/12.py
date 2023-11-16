# 12.	An array contains integer numbers. Create a program that calculates and displays the number of even and odd values in the array. Use the “while” loop statement.

array=[1,2,3,4,5,6,7,8,9]

index = 0
even_count = 0
odd_count = 0

while index < len(array):
    if array[index]%2==0:
        even_count+=1
    else:
        odd_count +=1 
    index+=1

print(odd_count, even_count)