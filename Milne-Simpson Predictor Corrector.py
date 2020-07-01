f = lambda t, x: #Insert relevant ODE here

def MilneSimpsonPC(a, b, N, alpha, alpha1, alpha2, alpha3):
    '''
    a: start point
    b: endpoint
    N: Number of points to estimate solution at
    alpha: first initial condition
    alpha1: second initial condition
    alpha2: third initial condition
    alpha3: fourth initial condition
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
    numList.append([timeList[0], wList[0]])
    numList.append([timeList[1], wList[1]])
    numList.append([timeList[2], wList[2]])
    numList.append([timeList[3], wList[3]])
    
    
    for i in range(3, N):
        
        #predict
        w = wList[i-3] + (((4*h)/(3))*((2*f(timeList[i], wList[i])) - (f(timeList[i-1], wList[i-1])) + 
                                       (2*f(timeList[i-2], wList[i-2])) )) 
        
        #correct
        w = wList[i-1] + ((h/3)*((f(timeList[i+1], w)) + (4*f(timeList[i], wList[i])) + 
                                 f(timeList[i-1], wList[i-1]) ))
        wList.append(w)
        numList.append([timeList[i+1], wList[i+1]])
        
    return numList 
