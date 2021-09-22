try:
    s=int(input())

    def temple(s):
        while(s!=0):
            n=int(input())
            h=[int(x) for x in input().split(" ")]
            flag=True
            if n%2==0: flag=False
            elif h[0]!=1 or h[n-1]!=1 : flag=False
            else:
                #print("else:flag: ",flag)
                mid=n//2
                for i in range(0,mid):
                    if h[i]+1==h[i+1]:
                        continue
                    else:
                        flag=False
                        break
                #print("<mid: ",flag)
                for i in range(mid,n-1):
                    if h[i]-1!=h[i+1]:
                        flag=False
                        break
                #print(">mid: ",flag)
            if flag==False:
                print("no")
            else:
                print("yes")
            s-=1

    temple(s)

except EOFError:
    pass