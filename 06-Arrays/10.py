# 10.	An array contains numbers: -15, 8, -31, 47, -2, 19. Create a program that finds and displays the maximum and minimum number. Do not use available functions.

array = [-15, -8, -31, 47, -2, 19]
current_max = array[0]
current_min = -2

# # print(current_max)
# # print(current_min)
for i in range(len(array)):
    if i < current_max:
        continue
    else:
        current_max=array[i]

for i in range(len(array)):
    print
    if array[i] < current_min:
        current_min= array[i]
    else:
        continue

print(current_min, current_max)