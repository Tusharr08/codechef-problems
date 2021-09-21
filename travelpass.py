try:
    t=int(input())

    def travelpass(t):
        if(t>=1 and t<=100):
            while(t!=0):
                n,a,b=[int(x) for x in (input().split(" "))]
                s=input()
                c1=0
                c2=0
                for i in s:
                    #print(i,'\n')
                    if i=='0':
                        c1+=1
                    else:
                        c2+=1
                total= c1*a + c2*b
                print(total,'\n')
                t-=1

    travelpass(t)

except EOFError:
    pass
