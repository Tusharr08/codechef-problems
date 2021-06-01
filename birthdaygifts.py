t=int(input())
def bdaygifts(t):
    if t> 100:
        print(0)
    else:

        while(t!=0):
            n,k=[int(x) for x in input().split(" ")]
            if (2*k+1)>n:
                print(0)
            else:

                A=[]
                cc=k
                tc=k
                chef=0
                twin=0
                A=list(map(int,input().split()))
                for i in range(1,n):
                    m=max(A)
                    print("max-- ",m)
                    if(len(A)!=2):
                        if(i%2!=0):
                            chef += m
                            cc-=1
                        elif i%2==0:
                            twin+=m
                            tc-=1
                        A.remove(m)
                    else:
                        twin += sum(A)
                    
                    print(A)
                print("chef cost--",chef)
                t-=1
bdaygifts(t)


        