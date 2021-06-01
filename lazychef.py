try:

    t=int(input())

    def lazychef(t):
        if(t>10000):
            print(0)
        else:
            while(t!=0):
                x,m,d=[int(x) for x in input().split(" ")]
                p=x*m
                s=x+d
                print(min(p,s))
                t-=1
    
    lazychef(t)

except EOFError:
    pass

