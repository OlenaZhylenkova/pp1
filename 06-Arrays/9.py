# 9.	An array contains values: 1, 2, 3, 4, 5. Create a program that modifies the array values. Display the array after each change.
# a.	subtract one from the first element of the array
# b.	increase the last array element by 4
# c.	multiple the middle array element by 2
# d.	adds 3 to each value of the array (use a loop statement)



array = [1,2,3,4,5]

array[0] = array[0] - 1
print(array)

array[4] = array[-1] +4
print(array)

array[2] = array[2]*2
print(array)

for x in range(len(array)):
    array[x] = array[x] + 3
print(array)
