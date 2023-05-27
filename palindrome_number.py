# to judge whether a number is a palindrome number
# a palindrome number is a number that reads the same backward as forward
# for example, both 1221 and 12321 are palindrome numbers, while 12345 is not

num = input('please input an integer number, and we will judge whether it is a palindrome number: ')
len_num = len(num)

if len_num % 2 != 0:
    # if len_num is an odd number, then the middle figure is not compared
    for j in range(int((len_num + 1) / 2)):
        if num[j] == num[len_num - j - 1]:
            if len_num == 2 * j + 1:
                print("{} is a palindrome number.".format(num))
        else:
            print("{} is not a palindrome number.".format(num))
            break
else:
    # if len_num is an even number, then all numbers are compared
    for j in range(int(len_num / 2)):
        if num[j] == num[len_num - j - 1]:
            if len_num == 2 * (j + 1):
                print("{} is a palindrome number.".format(num))
        else:
            print("{} is not a palindrome number.".format(num))
            break

