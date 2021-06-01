try:

    t=int(input())

    def chefinheaven(t):
        while(t!=0):
            l=int(input())
            s=input()
            s= [int(x) for x in s]
            ones=0
            flag=0
            zeros=0
            for i in range(l):
                if s[i]==0:
                    zeros += 1
                else:
                    ones += 1
                if(ones >= zeros):
                    flag=1
                    break
            if flag==0:
                print("NO")
            else:
                print("YES")
            t-=1

    chefinheaven(t)
except EOFError:
    pass