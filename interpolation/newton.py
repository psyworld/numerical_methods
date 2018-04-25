import numpy as np 
import math as m

np.set_printoptions(suppress=True)
h = 0.005

def main():
	X = np.zeros((13,1))
	X = np.array([round((0.101+i*0.005),5) for i in range(len(X))])
	
	Y = np.array([
		1.26183,
		1.27644,
		1.29122,
		1.30617,
		1.32130, 
		1.33660, 
		1.35207, 
		1.36773, 
		1.38357, 
		1.39959,
		1.41579,
		1.42683, 
		1.43356
		])

	#print(X)

	#строим таблицу разностей

	delta = np.zeros((13, 14))
	
	for i in range(13):
		delta[i][0] = X[i]
		delta[i][1] = Y[i]

	#print(delta)

	k = 0
	for j in range(2, 14):
		for i in range(12-k):
			delta[i][j] = (delta[i+1][j-1]-delta[i][j-1])
		k += 1

	print(delta)
	Y_ = delta[0][1:4]
	print(Y_)

	x = [round(1.4161 + 0.001*i, 5) for i in range(1, 31)]
	
	#1 формула Ньютона

	for i in x:
		print(i, "--", P(Y_, i, X[0]), end="\n")


def P(array, x, x_0):
	q = lambda x: (x-x_0)/h
	res = array[0] + q(x)*array[1] + q(x)*(q(x)-1)*array[2]/2
	'''
	for i in range(2, len(array)):
		res += k(i, q(x))*array[i]
		#print(k(i,q(x)), "--------\n")
	'''

	return round(res, 5)

def k(j, q):
	p = 1
	for i in range(1, j-1):
		p *= (q - (i-1))

	return p/m.factorial(j)

if __name__ == '__main__':
	main()