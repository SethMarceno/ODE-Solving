f = lambda t, x: #Insert relevant ODE here

def AdamsMoulton2(a, b, N, alpha, alpha1):
    '''
    a: start point
    b: endpoint
    N: Number of points to estimate solution at
    alpha: first initial condition
    alpha1: second initial condition
    '''
    numList = []
    timeList = []
    wList = []    
    h = (b-a)/N
    
    for i in range(0, N+1):
        timeList.append(a + (i*h))

    wList.append(alpha)
    wList.append(alpha1)
    numList.append([timeList[0], wList[0]])
    numList.append([timeList[1], wList[1]])
    
    for i in range(1, N):
        w = wList[i] + ((h/12)*((5*f(timeList[i+1], 0)) + 
                                (8*f(timeList[i], wList[i]))-(f(timeList[i-1], wList[i-1]))))
        wList.append(w)
        numList.append([timeList[i+1], wList[i+1]])
        
    return numList
