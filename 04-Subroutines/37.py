# 37.	Define the function f(n), which returns the n-th value of the Fibonacci sequence. The sequence is defined as follows: the first value of the sequence is 0, the second value is 1. Each subsequent value is the sum of the previous two. Sample result:
# f(5) returns 3
# f(9) returns 21


def f(n):
    n1=0
    n2=1
    count = 0
    next_num = n2
    seq = []
    for i in range(n):
        count += 1 
        n1, n2 = n2, next_num
        next_num = n1+n2    
        seq.append(next_num)
    return print(seq[n-4])

f(9)