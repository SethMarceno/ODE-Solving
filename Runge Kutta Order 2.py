f = lambda t, x: #ODE to solve

def RungeKutta2(a, b, N, alpha):
    '''
    a: start point
    b: endpoint
    N: number of points to approximate at
    alpha: initial condition
    '''
    endList = []
    h = (b-a)/N
    t = a
    w = alpha
    endList.append([t, w])
    
    for i in range(1, N+1):
        K1 = f(t, w)
        K2 = f(t+h, w + (h*K1))
        
        w = w + ((h/2)*(K1 + K2))
        t = a + (i * h)
        endList.append([t, w])
        
    return endList
