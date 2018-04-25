import math as m
import numpy as np

n = 4

def main():
	a = np.array([[4, 2, -1, 0.5], 
		 [1, -5, 2, 1  ],
		 [2, 1, -4, -1.5],
		 [1, -0.4, 0.8, -3]])
    
	b = [30.5, -20, 6.5, 1.2]

	epsilon = 0.001

	c = np.zeros((n,n))
	for i in range(n):
		for j in range(n):
			if i != j:
				c[i][j] = a[i][j]/a[i][i]
	print("alpha = ", c, end='\n\n')

	x = iteration(a, b, epsilon)
	b_ = np.dot(a,x)
	print(x, end='\n\n')
	print(b_, end='\n\n')
	print(check(b_, b))

def check(a,b):
	return ['%f'%(m.fabs(a[i]-b[i])) for i in range((n))]

def eval(A, b, X):
	e = np.zeros(n)

	for i in range(n):
		e[i] = -b[i]
		for j in range(n):
			e[i] += A[i][j]*X[j]
	return e

def eps(A, b, epsilon):
	for i in range(n):
		if m.fabs(A[i] - b[i]) >= epsilon:
			return False
	return True

def iteration_pass(A, b, X_):
	x = np.zeros(n)

	for i in range(n):
		acc = 0
		for j in range(n):
			if j != i:
				acc += A[i][j]*X_[j]
		x[i] = (b[i]-acc)/A[i][i]

	return x

def iteration(A, b, epsilon):
	y = b
	x_ = b
	x = b
	x_ = x_
	x = iteration_pass(A, b, x_)
	while (not eps(x_, x, epsilon)):
		x_ = x
		x = iteration_pass(A, b, x_ )

	add_pass = True
	while (add_pass):
		add_pass = False

		e = eval(A, b, x)
		for i in e:
			if m.fabs(i) > epsilon:
				add_pass = True

		if add_pass:
			x = iteration_pass(A, b, x)

	return x

if __name__ == '__main__':
	main()