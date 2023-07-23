# implements the recursive version of the Euclidean algorithm to find the greatest common divisor of two numbers
def gcd_recursive(m, n):
    if m % n == 0:
        return n
    else:
        return gcd_recursive(n, m % n)


m = int(input())
n = int(input())
number_gcd = gcd_recursive(m,n)

# check the result against the math.gcd() method
import math
if number_gcd == math.gcd(m, n):
    print("Result:", number_gcd, "is the correct greatest common divisor of", m, "and", n)
else:
    print("Result:", number_gcd, "is not the correct greatest common divisor of", m, "and", n)