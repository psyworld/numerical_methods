import numpy as np

np.set_printoptions(suppress=True)

def main():
	X = np.array([
		0.593,
		0.598,
		0.605,
		0.613,
		0.619,
		0.627,
		0.632,
		0.640,
		0.650
		])

	Y = np.array([
		0.532050,
		0.535625,
		0.540598,
		0.546235,
		0.550431,
		0.555983,
		0.559428,
		0.568738,
		0.575298
		])
	N = 8
	x = [0.704 + 0.001*i  for i in range(7, 2*N+1)]
	print(Y.size)
	for i in x:
		print(L(i, X, Y))

def L(x, X, Y):
	res = 0.0 
	for i in range(Y.size):
		a = 1
		b = 1
		for j in range(X.size):
			if i != j:
				a *= (x-X[j])
				b *= (X[i] - X[j])
		res += Y[i]*a/b

	return round(res, 4)

if __name__ == '__main__':
	main()