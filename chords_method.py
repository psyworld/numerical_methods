import math as m

def main():
	a = -3.34159
	b = 2.94159

	bounds = separation(a,b)
	print(bounds)

	roots = getRoots(bounds)
	print(*roots)
	

def f(x):
	return m.tan(0.5*x + 0.1) - x*x 

def df(x):
	return 0.5/((m.cos(0.5*x+0.1)) ** 2) - 2*x

def d2f(x):
	return 0.5*m.tan(0.5*x+0.1)/((m.cos(0.5*x+0.1))**2) - 2

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

def getRoots(bounds): #use chords method
	roots = []
	epsilon = 0.001
	for i in bounds:
		a = i[0]
		b = i[1]
		if f(a)<0 and f(b)>0 and d2f(b) > 0 or f(a)>0 and f(b)<0 and d2f(b) < 0:   
		#i.e. f'(x) * f''(x) > 0
		    x0 = a
		    xn = x0 - f(a)*(b-a)/(f(b)-f(a))
		    while m.fabs(xn-x0) > epsilon:
		    	x0 = xn
		    	xn = x0 - f(x0)*(b-x0)/(f(b)-f(x0))
		    roots.append(round(xn,4))
		else:
		#i.e. f'(x) * f''(x) < 0
			x0 = b
			xn = x0 - (f(b)*(b-a)/(f(b)-f(a)))
			while m.fabs(xn - x0) > epsilon:
				x0 = xn
				xn = x0 - f(x0)*(x0-a)/(f(xn)-f(a))
			roots.append(round(xn, 4))
	return roots

if __name__ == "__main__":
	main()