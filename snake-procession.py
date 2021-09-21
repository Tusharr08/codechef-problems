try:
    t=int(input())

    while(t!=0):
        n=int(input())
        s=input()
        snake=[]
        for i in s:
            if(i!='.'):
                snake.append(i)
        #print(snake)
        l=len(snake)
        flag=0
        if(l%2!=0):
            print("INVALID")
        else:
            for i in range(l):
                if i%2==0 and snake[i]!='H':
                    flag=1
                    break
                elif i%2!=0 and snake[i]!='T':
                    flag=1
                    break
            if(flag):print("INVALID")
            else: print("VALID")
        t-=1

except EOFError:
    pass