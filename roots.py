from math import *

def main():
	#input polynomial coefficients from a_0 to a_n
	m 			= [int(i) for i in input().split()] 
	upper_bound = getBound(m)
	lower_bound = (-1)*getBound(PtoA(m))
	print(lower_bound, upper_bound)
	root_bounds	= separation(lower_bound, upper_bound)
	print(root_bounds)
	roots 		= getRoots(root_bounds)
	print(roots)

def f(x):
	return x**3+2*x+4

def dx(x):
	return 3*x*x + 2
	
def getRoots(array):
	roots = []
	for i in array:
		xi = (i[0]+i[1])*0.5
		if round(f(xi),3) == 0.000:
			roots.append(xi)
		elif f(xi)*f(i[0]) < 0:
			roots.append([i[0],xi])
		else:
			roots.append([xi, i[1]])
	return roots

def separation(low, up):
	epsilon = 0.001
	n 		= 3 
	roots   = []
	i = low + epsilon
	while i < up:
		if f(i)*f(i-epsilon) < 0 and dx(i)*dx(i-epsilon) > 0:
			roots.append([round(i,n), round(i-epsilon,n)])
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