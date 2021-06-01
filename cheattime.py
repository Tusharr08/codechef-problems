try:
    t=int(input())

    def cheatime(t):
        if(t>100000):
            print(0)

        while(t!=0):
            n,k,f=[int(x) for x in input().split(" ")]
            if(n>0)
            sl=[]
            el=[]
            for i in range(n):
                s,e=[int(x) for x in input().split()]
                #print(s,e)
                sl.append(s)
                el.append(e)
                s=e=0
            #print("Si",sl)
            #print("Ei",el)
            d=[]
            for i in range(0,n):
                d.append(el[i] - sl[i])
            inv=sum(d)
            diff=f-inv
            if diff>=k:
                print("Yes")
            else:
                print("no")
            t-=1
    cheatime(t)

except EOFError:
    pass

