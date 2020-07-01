f = lambda t, x: #Insert ODE to be solved here

def RungeKutta4(a, b, N, alpha):
    '''
    a: start point
    b: endpoint
    N: Number of points to estimate
    alpha: initial condition
    '''
    endList = []
    h = (b-a)/N
    t = a
    w = alpha
    endList.append([t, w])
    
    for i in range(1, N+1):
        K1 = h * f(t, w)
        K2 = h * f(t + (h/2), w + (K1/2))
        K3 = h * f(t + (h/2), w + (K2/2))
        K4 = h * f(t + h, w + K3)
        
        w = w + ((K1 + (2*K2) + (2*K3) + K4)/6)
        t = a + (i * h)
        endList.append([t, w])
    return endList
