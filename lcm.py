# to find the least common multiple of two numbers using the linear search method

def lcm(x, y):
    # choose the greater number of the two numbers
    if x > y:
        greater = x
    else:
        greater = y
    # find the lcm starting from the greater number
    while True:
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

# test the lcm() method
print("please input two numbers m and n to calculate the least common multiple of them.")
m = int(input('input m: '))
n = int(input('input n: '))
number_lcm = lcm(m, n)
print("the least common multiple of two numbers m and n is %d" % number_lcm)

# check the result using the math.gcd() method
import math

# the least common multiple of two numbers is the product of the two numbers divided by their greatest common divisor
def lcm_using_gcd(x, y):
    lcm = (x * y) // math.gcd(x, y)
    return lcm

if number_lcm == lcm_using_gcd(m, n):
    print("Result:", number_lcm, "is the correct least common multiple of", m, "and", n)
else:
    print("Result:", number_lcm, "is not the correct least common multiple of", m, "and", n)
