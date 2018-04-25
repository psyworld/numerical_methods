from numpy import *
from math  import *

def gradient(X0, eps, F2, F_d):
 
	print("Solving system by Gradient descent")
	X0 = array(X0)
	X1 = X0.copy()

	while True:

		X0 = X1.copy()
		W = array([
			[F_d[0][0](*X0), F_d[0][1](*X0)],
			[F_d[1][0](*X0), F_d[1][1](*X0)]
		])

		F = array([F2[0](*X0), F2[1](*X0)])
		W_ = W.T
		mu_ = (W.dot(W_).dot(F))
		mu = (((F.dot(W)).dot(W_)).dot(F))/(mu_.dot(mu_))
		X1 = X0 - mu*(W_.dot(F))
		
		if all([abs(i) <= eps for i in X0 - X1]):
			break

	print("Solution is ", X1)
	print("Ckeck result:", check(X1, F2, eps))

	return X1


def check(X1, F, eps):
	a = F[0](*X1)
	b = F[1](*X1)
	print("After substitution into system:", '%f' % a, '%f' % b)
	return "okay!" if a < eps and b < eps else "You r loser"