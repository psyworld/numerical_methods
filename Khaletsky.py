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

	for i in range(n):
		for j in range(n):
			s = 0
			if i >= j > 0:
				for k in range(j-1):
					s += b[i][k]*c[k][j]
				b[i][j] = a[i][j]-s
			if 0 < i < j:
				s = 0
				for k in range(i-1):
					s += b[i][k]*c[k][j]
				c[i][j] = (1/b[i][i]).round(1)*(a[i][j]-s)
	print('b = ','\n', b, end='\n')
	print('c =','\n', c, end='\n')

	print(np.dot(b,c), end='\n')

	y = np.zeros(n)
	x = np.zeros(n)

	y[0] = a_free[0]/b[0][0]
	x[n-1] = y[n-1]

	for i in range(n):
		s = 0
		if i > 0: 
			for k in range(i-1):
				s += b[i][k]*y[k]
			y[i] = (1/b[i][i])*(a_free[i]-s)
		if i < (n-1):
			s = 0
			for k in range(i, n):
				s += c[i][k]*x[k]
			x[i] = y[i] - s

	print('y = ', y, '\n')
	print('x = ', x, '\n')
	print(np.dot(a,x),'\n')
	print(a_free)

if __name__ == "__main__":
	main()