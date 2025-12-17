#Write an algorithm to multiply two numbers n × n using Divide and Conquer

'''
Algorithm Multiply(x, y):

1. If x < 10 AND y < 10 then
       return x * y      // base case

2. Let n = max(number of digits of x, number of digits of y)
3. Let m = n / 2

4. Split x into:
       x = a * 10^m + b
   Split y into:
       y = c * 10^m + d

5. Recursively compute:
       ac = Multiply(a, c)
       ad = Multiply(a, d)
       bc = Multiply(b, c)
       bd = Multiply(b, d)

6. Combine the results:
       return ac * 10^(2*m) + (ad + bc) * 10^m + bd


'''

def multiply(x, y):
    if y == 0:
        return 0
    if y == 1:
        return x

    half = multiply(x, y // 2)

    if y % 2 == 0:
        return half + half  
    else:
        return half + half + x  



print(multiply(7, 5))  
print(multiply(12, 10)) 
