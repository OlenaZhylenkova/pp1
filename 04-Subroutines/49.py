def f(n1, n2):
    n1 = set(str(n1))
    n2 = set(str(n2))
    
    for digit in n1:
        if digit in n2:
            return True
        else:
            return False
            
if __name__ == "__main__":
    print(f(12, 456))
    print(f(12,715))
    print(f(4455,90951))
    print(f(4455,777666555))