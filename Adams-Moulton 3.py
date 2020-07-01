f = lambda t, x: #Insert relevant ODE here

def AdamsMoulton3(a, b, N, alpha, alpha1, alpha2):
    '''
    a: start point
    b: endpoint
    N: Number of points to estimate solution at
    alpha: first initial condition
    alpha1: second initial condition
    alpha2: third initial condition
    '''
    numList = []
    timeList = []
    wList = []    
    h = (b-a)/N
    
    for i in range(0, N+1):
        timeList.append(a + (i*h))

    wList.append(alpha)
    wList.append(alpha1)
    wList.append(alpha2)
    numList.append([timeList[0], wList[0]])
    numList.append([timeList[1], wList[1]])
    numList.append([timeList[2], wList[2]])
    
    for i in range(2, N):
        w = wList[i] + ((h/24)*
                        ((9*f(timeList[i+1], NewtonsMethod(wList[i], 10**-5, 100, 0.01, wList[i], wList[i-1], 
                                                           wList[i-2]))) + (19*f(timeList[i], wList[i]))-
                         (5*f(timeList[i-1], wList[i-1]))+(f(timeList[i-2], wList[i-2])) ))
        wList.append(w)
        numList.append([timeList[i+1], wList[i+1]])
        
    return numList
