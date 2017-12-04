import math as m
import numpy as np

eps = 0.001

def main():
	a = np.array([[4, 2, -1, 0.5], 
		 [1, -5, 2, 1  ],
		 [2, 1, -4, -1.5],
		 [1, -0.4, 0.8, -3]])
    
	free = [11.5, 1, 0.5, 7.2]
	n = 4
	norm = round(getNorm(a), 4)
	alpha, beta = start(n, a, free)
	print(alpha, beta)
	x = iteration(n, alpha, beta)
	print(x)
	print(np.dot(a, x))

def getNorm(array):
	return sum(array[i][j]**2 for i in range(len(array)) 
							  for j in range(len(array)))**(0.5)

def start(n, array, free):
	b = np.zeros((n, 1))
	a = np.zeros((n, n))

	for i in range(n):
		b[i] = round(free[i]/array[i][i], 4)
		for j in range(n):
			if i != j:
				a[i][j] = round(-array[i][j]/array[i][i], 4)
			else:
				a[i][j] = 0
	return a, b
 
def iteration(n, a, b):
	x = np.zeros((n,1))
	for i in range(n):
			x[i] = b[i] + sum(a[i][j]*x[j] for j in range(n))
	i = 1
	x_ = np.zeros((n,1))
	while True:
		for i in range(n):
			x[i] = b[i] + sum(a[i][j]*x[j] for j in range(n))
		if not epsilon(x, x_, eps):
			break
		x_ = x
	return x	

def epsilon(x, x_, eps):
	for i in range(len(x)):
		if m.fabs(x[i] - x_[i]) >= eps:
			return True
	return False

if __name__ == '__main__':
	main()