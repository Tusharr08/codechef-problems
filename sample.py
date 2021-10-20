# cook your dish here
def substrings(arr):
    n=len(arr)
    tmp=[]
    for i in range(n+1):
        for j in range(i+1,n+1):
            tmp.append(arr[i:j])
            
    return tmp

t=int(input())
while(t!=0):
    n=int(input())
    arr=input()
    s=0
    sub=substrings(arr)
    print('sub',sub)
    res=False
    for k in sub:
        print('k',k)
        for i in k:
            if i=='L':
                s+=1
            else:
                s-=1
            print('s in i',s,i)

        if s==2 or s==(-2):
            print('res',k)
            res=True
            break
        
        s=0
    if res==False:
        print('NO')
    else:
        print('YES')
            
        
    t-=1