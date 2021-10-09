def mex(a,n):
    l=[]
    for i in range(n+2):
        l.append(i)

    print(l)
    for i in range(n):
        if arr[i] not in l:
            return 0
        l.remove(a[i])
    print(l)
    return l[0]

if __name__ == "__main__":
    n=int(input())
    arr=[int(x) for x in input().split()]

    res=mex(arr,n)
    print(res)