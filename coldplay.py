t=int(input())
c=0
def coldplay(t):
    if t> 1000:
        print(0)
    else:
        while(t!=0):
            M,S=[int(x) for x in input().split()]
            if M<S:
                print(0)
            else:
                print( M//S )
            t -= 1

coldplay(t)
