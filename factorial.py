# using the recursive method to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# test factorial method
number_input = int(input("input a number to calculate the factorial: "))
number_factorial = factorial(number_input)
print("factorial of an input number {} is {}".format(number_input, number_factorial))

# check the result against the math.factorial() method
import math
if number_factorial == math.factorial(number_input):
    print("Result:", number_factorial, "is the correct factorial of", number_input)
else:
    print("Result:", number_factorial, "is not the correct factorial of", number_input)


