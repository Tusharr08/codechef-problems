t=int(input())
if(t>=1 and t<=1000):
    while(t!=0):
        n,s=[int(x) for x in input().split(" ")]
        if(s<=n):
            ans=s-0
        else:
            crr=s-n
            ans=n-crr

        print(ans)
        t-=1