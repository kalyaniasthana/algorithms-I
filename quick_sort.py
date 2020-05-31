from split_inversions import text_file_to_list

def partition(arr, l, r):

	#when pivot is the first element

	'''

	p = arr[l]
	i = l + 1
	j = l + 1

	while j < r:
		#print(i, j)
		if arr[j] < p:
			temp = arr[i]
			arr[i] = arr[j]
			arr[j] = temp
			i += 1
		j += 1

	temp = arr[i - 1]
	arr[i-1] = arr[l]
	arr[l] = temp
	print(arr)
	return i-1, r-l-1

	'''

	#when pivot is the last element
	p = arr[r - 1]
	#print(p)
	i = l
	j = l

	while j < r - 1:

		if arr[j] < p:
			temp = arr[i]
			arr[i] = arr[j]
			arr[j] = temp
			i += 1
		j += 1

	temp = arr[i]
	arr[i] = arr[r - 1]
	arr[r - 1] = temp
	#print(arr)

	#print(i)

	return i, r - l - 1

def sort_quick(arr, l, r):
	count = 0
	if l >= r:
		return 0
	pivot_index, count = partition(arr, l, r)
	#print(pivot_index, l, r)
	count += sort_quick(arr, l, pivot_index)
	count += sort_quick(arr, pivot_index + 1, r)
	return count


#arr = [3, 8, 2, 5, 1, 4, 7, 6]
#print(arr)

#filename = 'QuickSort.txt'
#arr = text_file_to_list(filename)
#count = sort_quick(arr, 0, len(arr))
#print(count)
#print(arr)

