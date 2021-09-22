try:
    t=int(input())
    while(t!=0):

        a,b,c=[int(x) for x in input().split()]
        x,y,z=[int(x) for x in input().split()]
        minx=[a,b,c]
        scorex=[x,y,z]
        timeneeded=0
        score=0
        totalmin=240
        totalprblm=60
        for i in range(3):
            if minx[i]*20<totalmin:
                totalmin-=minx[i]*20
                score+=scorex[i]*20
                totalprblm-=20
                #print("totalmin:",totalmin," score:",score," totalprblm:",totalprblm)
            else:
                prblms=totalmin/minx[i]
                #print("prblms*scorex[i]",prblms*scorex[i])
                score+= abs(prblms*scorex[i])
                break
        
        print(int(score))
        t-=1

except EOFError:
    pass