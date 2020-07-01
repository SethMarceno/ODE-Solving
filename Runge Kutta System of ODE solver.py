def RungeKuttaODE(f, a, b, alpha, N):
    '''
    f: array of system of functions of ODEs to solve
    a: start point
    b: endpoint
    alpha: initial condition
    N: Number of points to approximate solution at
    '''
    
    numList = []
    timeList = []
    h = (b - a)/N
        
        
    for i in np.arange(0, N+1):
        timeList.append(a + (i*h))
    
    m = np.size(alpha)
    
    w = np.zeros((1, m))  
    t = a
    
    for j in np.arange(0, m):
        w[0][j] = alpha[j]
    
        
    k = np.zeros((4, m))
    
    
    for i in np.arange(1, N+1):
        args = w[0][:]
        
        for j in np.arange(0, m):
            k[0][j] = h*(f[j](t, *args))
        
        for j in np.arange(0, m):
            args = []
            for n in np.arange(0, m):
                args.append(w[0][n] + ((1/2)*k[0][n]))
           
            k[1][j] = h*f[j](t+(h/2), *args)
            
        for j in np.arange(0, m):
            args = []
            
            for n in np.arange(0, m):
                args.append(w[0][n] + ((1/2)*k[1][n]))
                
            k[2][j] = h*f[j](t + (h/2), *args)
            
        for j in np.arange(0, m):
            args = []
            
            for n in np.arange(0, m):
                args.append(w[0][n] + (k[2][n]))
                
            k[3][j] = h*f[j](t + h, *args)
           
        
        for j in np.arange(0, m):
            w[0][j] = w[0][j] + ((1/6)*(k[0][j] + (2*k[1][j]) + (2*k[2][j]) + k[3][j]))
            

        
        
        numList.append([timeList[i], w[0][0], w[0][1]])
        t = a + i*h
        
        
    return numList
