import numpy as np

np.set_printoptions(suppress=True)
h = 0.05

def main():

	X = np.array([1.50 + 0.05*i for i in range(15)])

	Y = np.array([
		15.132,
		17.422,
		20.393,
		23.994,
		28.160,
		32.812,
		37.857,
		43.189,
		48.689,
		54.225,
		59.158,
		64.817,
		69.550,
		74.782,
		79.548
		])


	#Гаусс
	x1 = round(1.60+0.006*8, 4)
	#Стирлинг
	x2 = round(1.725+0.002*8, 4)
	#Бессель
	x3 = round(1.83+0.003*8, 4)

	delta = finite_deff(X, Y)

	#print(delta)

	y_ = delta[: : , 1:6]

	print("-----\n", y_, "-----\n", x1)

	print(X)

	j = 3 #x_0 index

	print(x1, "--", P_G(y_, x1, X[j], j),"<------- y1\n")

	j = 6 
	
	print(x2, "--", P_S(y_, x2, X[j], j),"<------- y2\n")

	j = 7

	print(x3, "--", P_B(y_, x3, X[j], j), "<------ y3\n")
	print(X[j-1], Y[j-1]) 
	print(X[j], Y[j])
	print(X[j+1], Y[j+1])

def finite_deff(X, Y):

	n = len(Y)
	delta = np.zeros((n, n+1))
	
	for i in range(n):
		delta[i][0] = X[i]
		delta[i][1] = Y[i]

	#print(delta)

	k = 0
	for j in range(2, n+1):
		for i in range(n - 1 -k):
			delta[i][j] = round((delta[i+1][j-1]-delta[i][j-1]), 3)
		k += 1

	return delta



def P_G(array, x, x_0, idx):
	q = lambda x: (x-x_0)/h
	#print(array[idx][0])
	res = array[idx][0]+q(x)*array[idx][2]
	res += q(x)*(q(x)-1)/2*array[idx-1][2]
	res += (q(x)+1)*(q(x)-1)/6*array[idx-1][3]
	res += (q(x)+1)*(q(x)-1)*(q(x)-2)/24*array[idx-2][4]

	return round(res, 5)

def P_S(ar, x, x_0, idx):
	q = lambda x: (x-x_0)/h
	res = ar[idx][0] + q(x)*(ar[idx-1][1]+ar[idx][1])/2
	res += (q(x))**2 * ar[idx-1][2]/2
	res += q(x)*((q(x))**2 - 1)*(ar[idx-2][3]+ar[idx-1][3]/2)

	return round(res,5)

def P_B(ar, x, x_0, idx):
	q = lambda x: (x-x_0)/h
	res = (ar[idx][0]+ar[idx+1][0])*0.5
	res += (q(x)-0.5)*ar[idx][1]
	res += q(x)*(q(x)-1)*0.5*(ar[idx-1][2]+ar[idx][2])*0.5
	res += (q(x)-0.5)*q(x)*(q(x)-1)*ar[idx-1][3]/6

	return round(res, 5)


if __name__ == '__main__':
	main()


