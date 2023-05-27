# to find the greatest common divisor of two numbers using the linear search method

def gcd(x, y):
    # choose the smaller number of the two numbers
    if x > y:
        smaller = y
    else:
        smaller = x
    # find the gcd which is equal or smaller than the smaller number
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            gcd = i
    return gcd

# test the gcd() method
print("please input two numbers m and n to calculate the greatest common divisor of them.")
m = int(input('input m: '))
n = int(input('input n: '))
number_gcd = gcd(m, n)
print("the greatest common divisor of two numbers m and n is %d" % number_gcd)

# check the result against the math.gcd() method
import math
if number_gcd == math.gcd(m, n):
    print("Result:", number_gcd, "is the correct greatest common divisor of", m, "and", n)
else:
    print("Result:", number_gcd, "is not the correct greatest common divisor of", m, "and", n)
