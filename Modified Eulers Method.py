f = lambda t, x: #Insert ODE to be solved here

def ModifiedEulersMethod(a, b, N, alpha):
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
        w = w + (h/2)*(f(t,w) + f((a + (i*h)), w + ((h)*(f(t, w)))))
        t = a + (i*h)
        numList.append([t,w])
    return numList
