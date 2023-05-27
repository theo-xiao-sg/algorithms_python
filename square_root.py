# compare two methods to search square root of a number using binary search and linear search
import time

# calculate square root of a large number using binary search
def square_root_binary_search(n):
    start = 0
    end = n
    while start <= end:
        # find the middle number between start and end
        mid = (start + end) // 2
        # compare the middle number with the square root of n
        # if lucky, the square root of n is the middle number
        if mid * mid == n:
            return mid
        # if the square root of n is larger than the middle number, search the upper half
        elif mid * mid < n:
            start = mid + 1
        # if the square root of n is smaller than the middle number, search the lower half
        else:
            end = mid - 1

# calculate square root of a large number using linear search
def square_root_linear_search(n):
    # brute force search from 0 to n
    for i in range(n):
        if i * i == n:
            return i

# test the two methods to search square root of a large number
number_input = int(input("input a number to generate a large square number: "))
large_number = number_input ** 2
print("square of an input number {} is {}".format(number_input, large_number))

# test binary search method and time the time used
start = time.time()
sqrt_result_binary_search = square_root_binary_search(large_number)
end = time.time()
print("Time used for binary search:", format(round(end - start, 2), ".2f"), "seconds")
# check the result against the square root of the large number
if sqrt_result_binary_search == number_input:
    print("Result binary search:", sqrt_result_binary_search,
          "is the correct square root of", large_number)
else:
    print("Result binary search:", sqrt_result_binary_search,
          "is not the correct square root of", large_number)

# test linear search method and time the time used
start = time.time()
sqrt_result_linear_search = square_root_linear_search(large_number)
end = time.time()
print("Time used for linear search:", format(round(end - start, 2), ".2f"), "seconds")
# check the result against the square root of the large number
if sqrt_result_linear_search == number_input:
    print("Result linear search:", sqrt_result_linear_search,
          "is the correct square root of", large_number)
else:
    print("Result linear search:", sqrt_result_linear_search,
          "is not the correct square root of", large_number)






