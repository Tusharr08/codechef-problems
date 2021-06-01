try:
    t=int(input())

    def hoopjump(t):
        if(t>100000):
            print(0)
        else:
            while(t!=0):
                n=int(input())
                if n%2==0 or n>2*(10**5):
                    print(0)
                else:

                    x=0
                    y=0
                    for i in range(n):
                        if i%2==0:
                            x+=1
                        else:
                            y+=1
                    print(x)
                    t-=1
    hoopjump(t)
except EOFError:
    pass

            
            
            
