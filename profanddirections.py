# cook your dish here
'''
def substrings(arr):
    n=len(arr)
    tmp=[]
    for i in range(n+1):
        for j in range(i+1,n+1):
            tmp.append(arr[i:j])
            
    return tmp
'''
t=int(input())
while(t!=0):
    n=int(input())
    arr=[]
    #arr=[1 if x=='L' else -1 for x in input().split()]
    for i in input():
        if i=='L':
            arr.append('1')
        else:
            arr.append('-1')
    print('arr',arr)
    s=0

    n=len(arr)
    tmp=[]
    res=False
    for i in range(n+1):
        for j in range(i+1,n+1):
            print([int(x) for x in arr[i:j]])
            s=sum([int(x) for x in arr[i:j]])
            print('s',s)
            if s==2 or s==(-2):
                res=True
                break
        s=0
    if res==False:
        print('NO')
    else:
        print('YES')

    t-=1
'''
    sub=substrings(arr)
    print('sub',sub)
    res=False
    for k in sub:
        print(k)
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
        print('NO')'''