from Iteration import Iteration, check_iteration
from math import cos, sin, sqrt
from gradient import gradient

F1 = [lambda x,y: 2*y - cos(x+1), lambda x,y: x + sin(y) + 0.4]
F_d1 = [
    [lambda x,y: sin(x+1), lambda x,y: 2],
    [lambda x,y: 1, lambda x,y: cos(y)]
]

F2 = [lambda x, y: sin(x+y) - 1.5*x - 0.1, 
	  lambda x, y: x ** 2 + y ** 2 - 1]

F_d2 = [
	[lambda x, y: cos(x+y) - 1.5, lambda x, y: cos(x+y)],
	[lambda x, y: 2*x, lambda x, y: 2*y]
]

if __name__ == '__main__':
    #result1 = Iteration([-0.8, 0.5], 0.001, F1, F_d1)
    result2 = gradient([0.6, 0.8], 0.001, F2, F_d2)