def fib(n):
	if (n / 1000) > 0:
		return n
	return fib(n-2) + fib(n-1)

result = fib(2)
print (result)
