# Purpose: binary search implementation using recursive algorithm

import random
random.seed(0)

# define the recursive binary search function
def search(lft, rgt, key):
	if lft > rgt:
		return -1
	mid = (lft + rgt) // 2
	if key == scores[mid]:
		return mid
	elif key < scores[mid]:
		return search(lft, mid - 1, key)
	else:
		return search(mid + 1, rgt, key)


# generate 50 random scores
scores = [random.randint(1, 500) for i in range(50)]
scores.sort()
print(scores)
key = int(input("input the score to search for:"))

# call the function to search the score
pos = search(0, len(scores), key)
print(pos)
