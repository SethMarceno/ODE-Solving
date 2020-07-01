def FECS(l, N, m, T, alpha, sigma, f):
    '''
    Forward Eulers time, Central difference in space
    '''
    k= T/m
    print('k', k)
    h= N/l
    print('h', h)
    lambd = sigma*(k/(h**2))
    #numList = []

    U = alpha #Vector valued
    Uvec = np.zeros([l+1])
    
    for j in range(0, m): 
        #Through Time
        
        for i in range(0, l+1): 
            #Through space
            if i == 0:
                Uvec[i] = 0
            elif i == 100:
                Uvec[i] = 0
            else:
                Uvec[i] = (lambd*U[i+1]) + ((1 - (2*lambd))*U[i]) + (lambd*U[i-1])
                

        #numList.append(Uvec)
        U[:]=Uvec
        
    return U #numList
