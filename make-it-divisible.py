t=int(input())
while(t!=0):
    n=int(input())
    l=10**n
    i=10**(n-1)
    #print(i)
    output=0
    while(i<l):
        #print(i)
        if i%2!=0:
            if i%3==0 and i%9!=0:
                output=i
                break
        i+=1
    print(i)
    
    t-=1