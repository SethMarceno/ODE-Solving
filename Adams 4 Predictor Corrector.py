f = lambda t, x: #Insert relevant ODE here

def Adams4PC(a, b, N, alpha):
    '''
    a: start point
    b: endpoint
    N: Number of points to approximate solution at
    alpha: Initial Condition
    '''
    numList = []
    timeList = []
    
    wList = [entry[1] for entry in RungeKutta4(a, b, N, alpha)][0:4]
    h = (b-a)/N
    
    
    for i in range(0, N+1):
        timeList.append(a + (i*h)) 

    for i in range(0, len(wList)):
        numList.append([timeList[i], wList[i]])        
     
        
    for i in range(4, N+1):
        
        #Predict
        w = wList[i-1] + ((h/24)* ((55*f(timeList[i-1], wList[i-1])) - (59*f(timeList[i-2], wList[i-2])) + (37*f(timeList[i-3], wList[i-3])) - (9*f(timeList[i-4], wList[i-4])) ) )
        
        #Correct
        w = wList[i-1] + ((h/24)* ((9*f(timeList[i], w)) + (19*f(timeList[i-1], wList[i-1])) - (5*f(timeList[i-2], wList[i-2])) + (f(timeList[i-3], wList[i-3])) ))
        wList.append(w)
        numList.append([timeList[i], wList[i]])
        
    return numList 
