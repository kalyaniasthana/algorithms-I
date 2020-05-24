
def text_file_to_list(filename):

	A = []
	with open(filename) as f:
		for line in f:
			line = line.strip('\n')
			A.append(int(line))
	return A

def merge_and_count_splitInv(A, n1, B, n2):

	#A and B are sorted in increasing order
	#A is the first sorted array of length n1
	#B is the second sorted array of length n2

	C = [0 for i in range(n1+n2)] #output array of length n
	i = 0
	j = 0
	k = 0
	split_inv = 0

	while i < n1 and j < n2:

		if A[i] < B[j]:
			C[k] = A[i]
			i += 1
			k += 1

		elif A[i] > B[j]:
			C[k] = B[j]
			j += 1
			k += 1
			split_inv += (n1 - i)

	#for end cases (in case there are some uncompared elements because n1 != n2)
	while i < n1:

		C[k] = A[i]
		i += 1
		k += 1

	while j < n2:

		C[k] = B[j]
		j += 1
		k += 1

	return C, split_inv


def merge_sort_and_count(arr, n):

	if n == 1:
		return arr, 0

	mid = (n+1)//2

	#first half of arr
	arr_1 = arr[:mid]
	n1 = len(arr_1)
	A, x = merge_sort_and_count(arr_1, n1)
	#second half of arr
	arr_2 = arr[mid:]
	n2 = len(arr_2)
	B, y = merge_sort_and_count(arr_2, n2)
	#merge both lists
	C, z = merge_and_count_splitInv(A, n1, B, n2)
	return C, x+y+z

#arr = [1, 20, 6, 4, 5]

#A = [1, 3, 5, 7]
#B = [2, 4, 6, 8]
#print(merge_and_count_splitInv(A, 4, B, 4))

filename = 'integers.txt'
arr = text_file_to_list(filename)
print(merge_sort_and_count(arr, len(arr)))
