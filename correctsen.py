try:
    t=int(input())

    def correctsen(t):
        if(t>500000):print(0)
        else:
            while(t!=0):
                k,s=input().split(maxsplit=1)
                sen=s.split()
                flag=0
                lc=0
                uc=0
                inv=0
                l=['a','b','c','d','e','f','g','h','i','j','k','l','m']
                u=['N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
                print(sen)
                for wd in sen:
                    print(wd)
                    for i in wd:
                        if i in l:
                            lc+=1
                        elif i in u:
                            uc+=1
                        else:
                            inv+=1
                            print(i)
                    print(lc,uc,inv)
                    if lc>0 and uc>0 or inv>0 :
                        flag=1
                        break
                    else:
                        lc=0
                        uc=0
                        inv=0
                if flag==1:
                    print("NO")
                else:
                    print("YES")
                
                t-=1
    correctsen(t)

except EOFError:
    pass
                            
            

