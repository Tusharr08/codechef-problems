def mex(a,n):
    l=[]
    for i in range(1,n+2):
        l.append(i)

    print('bef',l)
    for i in range(1,n+1):
        if a[i] not in l:
            return l[0]
        l.remove(a[i])
    print('aft',l)
    return l[0]

if __name__ == "__main__":
    n=int(input())
    arr=[int(x) for x in input().split()]

    res=mex(arr,n)
    print(res)