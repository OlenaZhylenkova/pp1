# 11.	An array contains a list of Polish names: Genowefa, Onufry, Celestyna, Alojzy, Pankracy. Create a program that displays the longest name (consisting of the largest number of characters). Sample result:

array = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

max_len = 0 
longest_name = array[0]

res = max(array, key=len)

print(res)