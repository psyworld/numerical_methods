import math as m

def main():
	a, b = float(input()), float(input())
	epsilon = 0.001
	x0 = b
	xn = x0 - f(x0)/df(x0)
	while (m.fabs(x0 - xn) > epsilon):
		x0 = xn
		xn = x0 - f(x0)/df(x0)
	print('	x = ', xn)

def f(x):
	return 3*x-m.exp(x)

def df(x):
	return 3 - m.exp(x)

if __name__ == "__main__":
	main()