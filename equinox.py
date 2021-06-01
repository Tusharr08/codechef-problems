try:
    t=int(input())
    str=['E','Q','U','I','N','O','X']
    l1=len(str)

    def equinox(t):
        if t>1000:
            print(0)
        else:
            while(t!=0):
                n,a,b=[int(x) for x in input().split(" ")]
                lst=[]
                while(n!=0):
                    lst.append(input())
                    n -= 1
                l2=len(lst)
                cs=0
                ca=0
                flag=0
                for i in range(l2):
                    lst[i] = lst[i].upper()
                print(lst)
                for i in range(l2):
                    for j in range(l1):
                        if lst[i][0]==str[j]:
                            cs += a
                            flag =1
                            break
                        flag=0
                    if flag ==0:
                        ca += b
                print(cs,ca)
                if cs>ca :
                    print("SARTHAK")
                elif cs<ca:
                    print("ANURADHA")
                else:
                    print("DRAW")
                cs=0
                ca=0
                lst=[]
                t -= 1

                
    equinox(t)
except EOFError:
    pass