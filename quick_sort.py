# implement quick sort algorithm using recursion
import random

def partition(list_num):
	pivot = list_num[0]
	lower_half = [x for x in list_num[1:] if x < pivot]
	upper_half = [x for x in list_num[1:] if x >= pivot]
	return lower_half, pivot, upper_half

# quick sort
def quick_sort(list_num, order = 'ascending'):
	assert order == 'ascending' or order == 'descending', """Give 'ascending' or 'descending'."""
	n = len(list_num)
	if n <= 1:
		return list_num
	else:
		lower_half, pivot, upper_half = partition(list_num)
		if order == 'ascending':
			return quick_sort(lower_half, order) + [pivot] + quick_sort(upper_half, order)
		else:
			return quick_sort(upper_half, order) + [pivot] + quick_sort(lower_half, order)


if __name__ == '__main__':
	random.seed(0)
	list_to_sort = [random.randint(1, 100) for i in range(50)]
	n = len(list_to_sort)
	print(list_to_sort)
	list_sorted = quick_sort(list_to_sort, input('Give "ascending" or "descending":'))
	print(list_sorted)
