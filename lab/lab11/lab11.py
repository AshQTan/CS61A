def countdown(n):
	"""
	>>> for number in countdown(5):
	...     print(number)
	...
	5
	4
	3
	2
	1
	0
	"""
	while n >= 0:
		yield n
		n -= 1

def trap(s, k):
	"""Return a generator that yields the first K values in iterable S,
	but raises a ValueError exception if any more values are requested.

	>>> t = trap([3, 2, 1], 2)
	>>> next(t)
	3
	>>> next(t)
	2
	>>> next(t)
	ValueError
	>>> list(trap(range(5), 5))
	ValueError
	"""
	g=iter(s)
	assert len(s) >= k
	while k > 0:
		x = next(g)
		if x is None:
			raise ValueError
		else:
			yield x
		k -= 1
	if k==0:
		raise ValueError('uh oh')


def repeated(t, k):
	"""Return the first value in iterable T that appears K times in a row.

	>>> s = [3, 2, 1, 2, 1, 4, 4, 5, 5, 5]
	>>> repeated(trap(s, 7), 2)
	4
	>>> repeated(trap(s, 10), 3)
	5
	>>> print(repeated([4, None, None, None], 3))
	None
	"""
	# assert k > 1
	# def cont(lst):
	# 	for c in lst:
	# 		if c != k:
	# 			return False
	# 	return True

	# for x in range(t):
	# 	if cont(lst[x, x+k]):
	# 		return t(x)
	# return None
	assert k>1
	count = 0
	first = True
	for v in t: 
		if first:
			first, previous = False, v
		elif v==previous:
			count+=1
			if k ==count:
				return v
		else: 
			count =1
			previous = v

def hailstone(n):
	"""
	>>> for num in hailstone(10):
	...     print(num)
	...
	10
	5
	16
	8
	4
	2
	1
	"""
	yield n 
	if n>1:
		if n%2==0:
			yield from hailstone(n//2)
		else:
			yield from hailstone(n*3+1)
