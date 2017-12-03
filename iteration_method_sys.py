import math as m
import numpy as np

eps = 0.001

def main():
	'''a = np.array([[4, 2, -1, 0.5], 
		 [1, -5, 2, 1  ],
		 [2, 1, -4, -1.5],
		 [1, -0.4, 0.8, -3]])
''' 
	a = np.array([[4, 0.24, -0.08], 
		 [0.09, 3, -0.15],
		 [0.04, -0.08, 4]])
	free = [8, 9, 20]
	
	norm = round(getNorm(a), 4)
	iteration(3, a, free)

def getNorm(array):
	return sum(array[i][j]**2 for i in range(len(array)) 
							  for j in range(len(array)))**(0.5)

def start(n, array, free):
	b = np.zeros((n, 1))
	a = np.zeros((n, n))
	x = np.zeros((n, 1))

	for i in range(n):
		b[i] = round(free[i]/array[i][i], 4)
		for j in range(n):
			if i != j:
				a[i][j] = round(-array[i][j]/array[i][i], 4)
			else:
				a[i][j] = 0
			 
def iteration(n, a, b, x)

	

def epsilon(x, eps):
	for i in range(x):
		if m.fabs(x[i]) >= eps:
			return False
	return True



if __name__ == '__main__':
	main()