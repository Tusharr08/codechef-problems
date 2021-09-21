try:
    t=int(input())
    
    def coconut(t):
        
        if(t<1 or t>15000):
            print(0)
        else:
            while(t!=0):
                xa,xb,Xa,Xb=[int(x) for x in input().split(" ")]
                if((xa<100 or xa>200)and (xb<400 or xb>500) and (Xa<1000 or Xa>1200) and (Xb<1000 or Xb>1500)):
                    print(0)
                else:
                    total=Xa//xa + Xb//xb
                    print(total)
                t-=1
    coconut(t)
except EOFError:
    pass


