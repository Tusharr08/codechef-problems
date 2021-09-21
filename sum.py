t=int(input())
while(t!=0):
    n,s=[int(x) for x in input().split(" ")]
    ans=0
    sum=(n*(n+1))//2
    if sum>s:
        ans=sum-s
    if ans>=1 and ans<=n:
        print(ans)
    else:
        print("-1")
    t-=1