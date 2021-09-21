try:
    t=int(input())

    if t>=1 and t<=100:
        while(t!=0):
            x=int(input())
            dir=["North","East","South","West"]
            while(x>3):
                x -= 4
            print(dir[x])
            t-=1

except EOFError:
    pass
