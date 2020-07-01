f = lambda t, x: #Insert relevant ODE here

def TrapezoidalMethod(a, b, N, alpha, TOL, M):
    '''
    a: start point
    b: endpoint
    N: Number of points to approximate solution at
    alpha: Initial Condition
    TOL: Error tolerance
    M: maximum number of iterations
    '''
    numList = []
    timeList = []
    h = (b-a)/N
    t = a + h
    j = 1
    
        
    numList.append([a, alpha])
        
    K1 = alpha + ((h/2)*(f1(a, alpha)))
    w0 = K1
    FLAG = 0
    
    while FLAG == 0:
        w = w0 - ((w0 - ((h/2)*(f(t + h, w0))) - K1)/(1 - ((h/2)*fy(t + h, w0))))
        
        if abs(w - w0)< TOL:
            FLAG = 1
        else:
            numList.append([t, w])
            j = j+1
            
            w0 = w
            if j > M:
                return [numList, 'Maximum # of iterations exceeded']
        
        if t >= b:
            return numList
        
        t = a + (h*j)
