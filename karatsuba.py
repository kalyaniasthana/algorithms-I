def add_zeros_left(big_num, small_num): #big_num and small_num are strings
	no_of_zeros = len(big_num) - len(small_num)
	small_num = '0'*no_of_zeros + small_num
	return small_num

def add_zeros_right(num, zeros):
	num = str(num)
	num = num + '0'*zeros
	return int(num)

def karatsuba_multiplication(x, y):
	x = str(x)
	y = str(y)

	if len(x) == len(y) == 1:
		p = int(x)*int(y)
		#print(p, 'x*y')
		return p

	if len(x) < len(y):
		x = add_zeros_left(y, x)
	elif len(x) > len(y):
		y = add_zeros_left(x, y)

	len_x = len(x)

	half_len = len_x//2

	if len(x)%2 != 0:
		half_len += 1

	zeros_q = len_x - half_len
	zeros_p = zeros_q*2
	a = int(x[ :half_len])
	c = int(y[ :half_len])
	b = int(x[half_len: ])
	d = int(y[half_len: ])
	#print(a, b, c, d, 'abcd')

	p = karatsuba_multiplication(a, c)
	q = karatsuba_multiplication(b, d)
	i = a+b
	j = c+d
	r = karatsuba_multiplication(i, j)
	r = r-p-q
	p = add_zeros_right(p, zeros_p)
	r = add_zeros_right(r, zeros_q)
	prod = p + r + q
	#print(prod, 'prod')
	return prod

#x = 5678910
#y = 1234567
x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627
prod = karatsuba_multiplication(x, y)
print(prod, 'final')


