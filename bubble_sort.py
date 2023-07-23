# implement Bubble sort algorithm
import random

def swap(a, j):
	a[j], a[j+1] = a[j+1], a[j]
	return a


# bubble sort
def bubble_sort(a, order = 'ascending'):
	assert order == 'ascending' or order == 'descending', """Give 'ascending' or 'descending'."""
	n = len(a)
	for i in range(n - 1):
		for j in range(n - 1 - i):
			if order == 'ascending':
				if a[j] > a[j + 1]:
					a = swap(a, j)
			else:
				if a[j] < a[j + 1]:
					a = swap(a, j)
	return a

if __name__ == '__main__':
	random.seed(0)
	list_to_sort = [random.randint(1, 100) for i in range(50)]
	n = len(list_to_sort)
	print(list_to_sort)
	list_sorted = bubble_sort(list_to_sort, input('Give "ascending" or "descending":'))
	print(list_sorted)
