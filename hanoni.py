def hanoni(n,a,b,c):
    if(n==1):
        print(a,'->',c)
    else:
        hanoni(n-1,a,c,b)
        hanoni(1,a,b,c)
        hanoni(n-1,b,a,c)

hanoni(4,'a','b','c')
