def prefix(string):
    p=[] 
    for i in range(-1,len(string)):
        print('i',i)
        p.append(string[:i + 1])
    return p

#print(prefix('ab'))

def displaysublist(A): 
        # store all the sublists  
        B = [[ ]] 
            
        # first loop  
        for i in range(-1,len(A) + 1):   
            # second loop  
            for j in range(i + 1, len(A) + 1):         
                # slice the subarray  
                sub = A[i:j] 
                B.append(sub) 
        return B[1:]

t=int(input())
while(t!=0):
    p=input()
    q=input()
    x=input()
    psub=prefix(p)
    qsub=prefix(q)
    xsub=displaysublist(x)
    print(psub,qsub,xsub)
    c=0
    '''
    for i in psub:
        for j in qsub:
            if i+j in xsub:
                c+=1
                print('i:',i,'j:',j)
'''
    i=0
    j=0
    while(i<len(psub)):
        print(i,j)
        if psub[i]+qsub[j] in xsub:
            print('i:',i,psub[i],'j:',j,qsub[j])
            c+=1
        j+=1
        if j==len(qsub):
            i+=1
            j=0
    print(c)
    t-=1