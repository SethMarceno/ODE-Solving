f = lambda t, x: #Insert relevant ODE here

def NewtonsMethod(p0, tol, n0, h, w0, t):
    f = lambda x: x - w0 - (h*((-15*(x - (t**(-3)))) - (3/(t**4))) )
    f_prime = lambda x: 1 + 15*h
    i = 1
    while i <= n0:
        p = p0 - (f(p0)/f_prime(p0))
        if abs(p - p0) < tol:
            return p
        i += 1
        p0 = p
    return ('Method failed after ', n0, ' iterations')


def BackwardEulersMethod(a, b, N, alpha):
    '''
    Note this method uses Newtons Iteraition
    a: start point
    b: endpoint
    N: Number of points to approximate solution at
    alpha: Initial Condition
    '''
    numList = []
    timeList = []
    h = (b-a)/N
    
    for i in range(0, N+1):
        timeList.append(a + (i*h))
        
    w0 = alpha
    numList.append([timeList[0], w0])
    
    for i in range(0, N):
        w = w0 + (h*f(timeList[i+1], NewtonsMethod(w0, 10**-5, 50, h, w0, timeList[i+1])))
        numList.append([timeList[i+1], w])
        w0 = w
    
    return numList
