t=int(input())
j=1
while(t!=0):
    n,d,c,m=[int(x) for x in input().split()]
    s=input()
    flag=0
    if 'D' not in s:
        print('Case #{}: YES'.format(j))
        j+=1
        t-=1
        continue
    for i in s:
        if i=='C':
            c-=1
        else:
            d-=1
            c+=m
        if c<0 or d<0:
            flag=1
            break
    if flag==1:
        print('Case #{}: NO'.format(j))
    else:
        print('Case #{}: YES'.format(j))
    j+=1
    t-=1