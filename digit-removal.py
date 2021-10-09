# cook your dish here
try:
    t=int(input())

    while(t!=0):
        n,d=[int(x) for x in input().split()]
        new=n
        c=0
        ans=0
        while(new>0):
            rem=new%10
            new//=10
            print(new)
            c+=1
            if(rem==d):
                new=new*(10**c) + (rem+1)*(10**(c-1))
                print(new)
                ans=new-n
                print(ans)
                c=0
        print(ans)
        t-=1
    
except EOFError:
    pass