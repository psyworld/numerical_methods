import numpy as np

def main():
	n = 4
	a = np.array([[4, 2, -1, 0.5], 
		 [1, -5, 2, 1  ],
		 [2, 1, -4, -1.5],
		 [1, -0.4, 0.8, -3]])
	print('a = b*c','\n', a, end='\n')
	a_free = np.array([30.5, -20, 6.5, 1.2] )

	b = np.zeros((n,n))
	c = np.eye(n)

	for i in range(n):
		b[i][0] = a[i][0]

	for j in range(n):
		c[0][j] = a[0][j]/b[0][0] 

	for i in range(1, n):
		for j in range(1, n):
			if i >= j:
				sum1 = sum([b[i][k]*c[k][j] for k in range(0, j)])
				b[i][j] = a[i][j]-sum1
			if i < j:
				sum2 = sum([b[i][k]*c[k][j] for k in range(0, i)])
				c[i][j] = (a[i][j]-sum2)/b[i][i]
	print('b = ','\n', b, end='\n')
	print('c =','\n', c, end='\n')

	print(np.dot(b,c), end='\n')

	y = np.zeros(n)
	x = np.zeros(n)

	y[0] = a_free[0]/b[0][0]

	for i in range(1, n):
		sum1 = sum([b[i][k]*y[k] for k in range(0, i)])
		y[i] = (a_free[i]-sum1)/b[i][i]

	x[n-1] = y[n-1]

	for i in range(n-1, -1, -1):
		sum1 = sum([c[i][k]*x[k] for k in range(i+1, n)])
		x[i] = y[i] - sum1

	print('y = ', y, '\n')
	print('x = ', x, '\n')
	print(np.dot(a,x),'\n')
	print(a_free)

if __name__ == "__main__":
	main()