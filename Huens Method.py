f = lambda t, x: #Insert ODE to be solved here


def HeunsMethod(a , b, N, alpha):
    '''
    a: start point
    b: endpoint
    N: Number of points to estimate
    alpha: initial condition
    '''
    numList = []
    h = (b-a)/N
    t = a
    w = alpha
    numList.append([t,w])
    for i in range(1, N+1):
        w = w + ((h/4)*((f(t, w)) + (3*(f(t + ((2*h)/3), w + (((2*h)/3)*(f(t + (h/3), w + ((h/3)*(f(t, w)))))))))))
        t = a + (i*h)
        numList.append([t,w])
    return numList 
