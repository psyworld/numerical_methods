from numpy.linalg import det, inv
from numpy import array


def Iteration(X0, e, F, F_d):
    print("Solving system by ITERATION METHOD")
    X0 = array(X0)
    X1 = X0.copy()
    l = array([
        [F_d[0][0](*X0), F_d[0][1](*X0)],
        [F_d[1][0](*X0), F_d[1][1](*X0)]
    ])
    print("Yakoby matrix", l)
    if not det(l):
        print("Determinant = 0, inv matrix does not exist!")
        return
    print("Det =", det(l))
    lambda_ = -inv(array(l))
    print("Inv matrix =", lambda_)
    while True:
        X0 = X1.copy()
        X1 = X0 + lambda_.dot(array([F[0](*X0), F[1](*X0)]))
        if all([abs(i) <= e for i in X0 - X1]):
            break
    print("Solution by Iteration method is:", X1)
    print("Check iteration result", check_iteration(X1, F))
    print()
    return X1


def check_iteration(X1, F):
    r1 = F[0](*X1)
    r2 = F[1](*X1)
    print('After substitution into system:', '%f' % r1, '%f' % r2)
    return "OK!" if r1 < 0.001 and r2 < 0.001 else "FAIL!"
