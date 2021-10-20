# cook your dish here
try:
    t=int(input())
    while(t!=0):
        n=int(input())
        b=[int(x) for x in input().split()]
        a=[]
        k=0
        i=0
        c=[]
        while(len(c)<n and len(a)<n):
            tmp=[]
            for i in range(n):
                tmp.append(k%b[i])
            #print('tmp',tmp)
            for i in tmp:
                if i not in c:
                    c.append(i)
                    #if k not in a:
                   #     a.append(k)
            a.append(k)
            #print('a',a)
            #print('c',c)
            k+=1
        #print(c)
        print(a)

        t-=1
except EOFError:
    pass