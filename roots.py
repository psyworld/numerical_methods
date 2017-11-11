from math import *

def main():
	#input polynomial coefficients from a_0 to a_n
	m 			= [int(i) for i in input().split()] 
	upper_bound = getBound(m)
	lower_bound = (-1)*getBound(PtoA(m))
	print(lower_bound, upper_bound)
	root_bounds	= separation(lower_bound, upper_bound)
	print(*root_bounds)
	roots 		= getRoots(root_bounds)
	print(*roots)

def f(x):
	return x**3+2*x+4

def df(x):
	return 3*x*x + 2

def getRoots(bounds): #use iteration method
	epsilon = 0.001
	roots = []
	n = 4
	for i in bounds:
		x0 = i[1]
		xn = x0 - f(x0)/df(x0)
		while (fabs(x0 -xn) > epsilon):
			x0 = xn
			xn = x0 - f(x0)/df(x0)
		roots.append(round(xn, n))
	return roots
	

def separation(low, up):
	epsilon = 0.1
	n 		= 3
	roots   = []
	i = low + epsilon
	while i < up:
		if f(i)*f(i-epsilon) < 0 and df(i)*df(i-epsilon) > 0:
			roots.append([round(i-epsilon,n),round(i,n)])
		i += epsilon
	return roots

def getBound(array):
	bound = 1	
	while not (is_bound(getHorner(array,bound))):
		bound += 1
	return bound

def getHorner(array, x):
	horner = []
	b      = array[0]
	horner.append(b)
	for i in range(1,len(array)):
		b = array[i] + b*x
		horner.append(b)
	return horner

def is_bound(array):
	#check horner's coefficients
	for i in array:
		if i < 0:
			return False
	return True

def PtoA(array):	
	#make P(-x)
	for i in range(len(array)):
		if (len(array)-i-1) % 2 != 0:
			array[i] *= -1
	#multiplied by (-1)^n
	if (len(array)-1) % 2 != 0:
		return list(map(lambda x: x*(-1),array))
	return array


if __name__ == "__main__":
	main()