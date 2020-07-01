f = lambda t, x: #Insert relevant ODE here

def AdamsBashforth5(a, b, N, alpha, alpha1, alpha2, alpha3, alpha4):
    '''
    a: start point
    b: endpoint
    N: Number of points to estimate solution at
    alpha: first initial condition
    alpha1: second initial condition
    alpha2: third initial condition
    alpha3: fourth initial condition
    alpha4: fifth initial condition
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
    wList.append(alpha3)
    wList.append(alpha4)
    numList.append([timeList[0], wList[0]])
    numList.append([timeList[1], wList[1]])
    numList.append([timeList[2], wList[2]])
    numList.append([timeList[3], wList[3]])
    
    for i in range(4, N+1):
        w = wList[i] + ((h/720)*((1901*f(timeList[i], wList[i]))-(2774*f(timeList[i-1], wList[i-1]))+
                                 (2616*f(timeList[i-2], wList[i-2]))-(1274*f(timeList[i-3], wList[i-3]))+
                                 (251*f(timeList[i-4], wList[i-4]))))
        wList.append(w)
        numList.append([timeList[i], wList[i]])
        
    return numList
