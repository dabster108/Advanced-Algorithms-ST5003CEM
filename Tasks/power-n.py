def power(n, p):
    if p == 0:
        return 1

    half = power(n, p // 2)

    if p % 2 == 0: 
        return half * half
    else:         
        return n * half * half


print(power(2, 10))  
print(power(3, 4))   
print(power(5, 3))  
