f = lambda t, x: #Insert relevant ODE here

def MilneMethod(a, b, N, alphaList):
    '''
    a: start point
    b: endpoint
    N: Number of points to approximate solution at
    alphaList: List of initial conditions
    '''
    numList = []
    timeList = []
    wList = []    
    h = (b-a)/N
    
    for i in range(0, N+3):
        timeList.append(a + (i*h))

    for i in range(0, len(alphaList)):
        wList.append(alphaList[i])
        numList.append([timeList[i], wList[i]])
        
    
    
    for i in range(3, N):
        
        #predict
        w = wList[i-1] + ((h/3)*((f(timeList[i+1], w)) + (4*f(timeList[i], wList[i])) + f(timeList[i-1], wList[i-1]) ))
         
        #correct
        w = wList[i-3] + (((4*h)/(3))*((2*f(timeList[i], wList[i])) - 
                                       (f(timeList[i-1], wList[i-1])) + (2*f(timeList[i-2], wList[i-2])) ))
        wList.append(w)
        numList.append([timeList[i+1], wList[i+1]])
        
    return numList[-1] 
