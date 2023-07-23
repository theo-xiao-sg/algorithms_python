# implement insert sort algorithm
import random

def swap(a, j):
	a[j], a[j+1] = a[j+1], a[j]
	return a

# insert sort
def insert_sort(a, order = 'ascending'):
	assert order == 'ascending' or order == 'descending', """Give 'ascending' or 'descending'."""
	n = len(a)
	# i is the number which needed to be inserted
	for i in range(1,n):
		key = a[i]
		j = i - 1
		# j is the number which is in front of the number needs to be inserted
		if order == 'ascending':
			while j >= 0 and key < a[j]:
				a = swap(a,j)
				j -= 1
		else:
			while j >= 0 and key > a[j]:
				a = swap(a,j)
				j -= 1
	return a

if __name__ == '__main__':
	random.seed(0)
	list_to_sort = [random.randint(1, 100) for i in range(50)]
	n = len(list_to_sort)
	print(list_to_sort)
	list_sorted = insert_sort(list_to_sort, input('Give "ascending" or "descending":'))
	print(list_sorted)
