try:
    t=int(input())

    while(t!=0):
        n,k=[int(x) for x in input().split(" ")]
        s=[int(x) for x in input().split(" ")]
        s.sort(reverse=True)
        #print(s)
        c=0
        for i in range(0,n):
            if s[i]>= s[k-1]:
                c+=1
        print(c)
        t-=1

except EOFError:
    pass