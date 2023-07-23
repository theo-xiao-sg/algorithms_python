# implement selection sort algorithm
import random

def swap2(a,i,j):
	a[i], a[j] = a[j], a[i]
	return a

# selection sort
def select_sort(a, order = 'ascending'):
	assert order == 'ascending' or order == 'descending', """Give 'ascending' or 'descending'."""
	n = len(a)
	for i in range(n - 1):
		key = i
		for j in range(i + 1, n):
			if order == 'ascending':
				if a[j] < a[key]:
					key = j
			else:
				if a[j] > a[key]:
					key = j
		a = swap2(a, i, key)
	return a

if __name__ == '__main__':
	random.seed(0)
	list_to_sort = [random.randint(1, 100) for i in range(50)]
	n = len(list_to_sort)
	print(list_to_sort)
	list_sorted = select_sort(list_to_sort, input('Give "ascending" or "descending":'))
	print(list_sorted)
