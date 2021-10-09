
try:
    t=int(input())

    def displaysublist(A): 
        # store all the sublists  
        B = [[ ]] 
            
        # first loop  
        for i in range(len(A) + 1):   
            # second loop  
            for j in range(i + 1, len(A) + 1):         
                # slice the subarray  
                sub = A[i:j] 
                B.append(sub) 
        return B[1:]

    def mex(a,n):
        l=[]
        for i in range(n+2):
            l.append(i)

        print(a,l)
        for i in range(n):
            if a[i] not in l:
                return 0
            l.remove(a[i])
        print(l)
        return l[0]

    while(t!=0):
        n,k=[int(x) for x in input().split()]
        arr=[int(x) for x in input().split()]
        #print("arr ",arr)
        fin=[]
        m=[]
        fin=displaysublist(arr)
        print(fin)
        for i in fin:
            #print(i,len(i))
            m.append(mex(i,len(i)))
        print(m)
        m.sort()
        print(m[k-1])
        t-=1


except EOFError:
    pass