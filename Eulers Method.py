def EulersMethod(a, b, N, alpha):
    '''
    a: start point
    b: endpoint
    N: number of points to estimate at
    alpha: initial condition
    '''
    numList = []
    h = (b-a)/N
    t = a
    w = alpha
    numList.append([t,w])
    for i in range(1, N+1):
        w = w + (h*f(t, w))
        t = a + (i*h)
        numList.append([t,w])
    return numList
