def LeapFrogMethod(a, b, N, alpha, alpha1, f):
    '''
    a: start point
    b: endpoint
    N: number of points to approximate at
    alpha: initial condition
    alpha1: second initial condition
    f: ODE to approximate
    '''
    numList = []
    h = (b-a)/N
    t = a+h
    w = []
    w.append(alpha)
    w.append(alpha1)
    numList.append([t-h, w[0]])
    numList.append([t, w[1]])    
    for i in range(1, N):
        w.append( w[i-1] + (2*h*f(t, w[i])) )
        numList.append([t+h, w[i+1]])
        t = t + h      
    return numList
