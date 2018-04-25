from iteration_method_sys import *
from Khaletsky import * 
from time import time

def main():
	n = 4
	a = np.array([[4, 2, -1, 0.5], 
		[1, -5, 2, 1  ],
		[2, 1, -4, -1.5],
		[1, -0.4, 0.8, -3]])
    
	b = [30.5, -20, 6.5, 1.2]

	epsilon = 0.001
	tic = time()
	x = iteration(a, b, epsilon)
	toc = time()

	print('Метод итераций занимает ', (toc - tic)*1000,'ms', end="\n")
	print(x, end='\n\n')

	tic = time()
	x = khaletsky(n, a, b)
	toc = time()

	print('Метод Халецкого занимает', (toc - tic)*1000, 'ms', end='\n')
	print(x)

if __name__ == '__main__':
	main()
