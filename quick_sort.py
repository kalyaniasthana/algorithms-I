from split_inversions import text_file_to_list

#form stack overflow 
def median_of_three(arr, l, r):
    mid = (l + r - 1)//2
    a = arr[l]
    b = arr[mid]
    c = arr[r - 1]

    if a <= b <= c:
        return b, mid

    if c <= b <= a:
        return b, mid

    if a <= c <= b:
        return c, r - 1

    if b <= c <= a:
        return c, r - 1

    return a, l

def partition(arr, l, r):

	'''
	if (r - l) % 2 == 0:
		x = (r - l)//2
		mid = x - 1
	else:
		mid = (r - l)//2
	'''

	#print(r - l, mid)

	#find_median_list = [arr[l], arr[mid], arr[r - 1]]

	#med = median(find_median_list)

	#print(find_median_list, med, arr[mid])

	#if med == arr[mid]:

	#	arr[l], arr[mid] = arr[mid], arr[l]

	#elif med == arr[r - 1]:

	#	arr[l], arr[r - 1] = arr[r - 1], arr[l]

	pivot, pivot_index = median_of_three(arr, l, r)
	arr[l], arr[pivot_index] = arr[pivot_index], arr[l]

	p = arr[l]
	i = l + 1
	j = l + 1

	while j < r:
		if arr[j] < p:
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
		j += 1

	arr[i - 1], arr[l] = arr[l], arr[i - 1]

	return i - 1, r - l - 1

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

filename = 'QuickSort.txt'
arr = text_file_to_list(filename)
count = sort_quick(arr, 0, len(arr))
print(count)
#print(arr)

