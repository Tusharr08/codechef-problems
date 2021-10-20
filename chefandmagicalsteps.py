# cook your dish here
#from sympy import *

def isprime(num):
    for n in range(2,int(num**1/2)+1):
        if num%n==0:
            return False
    return True

t=int(input())
while(t!=0):
    x,y=[int(x) for x in input().split()]
    s=0
    i=x
    while(i<y):
        print(i,s)
        if i+2<=y and isprime(i+2)==True:
            print('prime',i+2)
            i+=2
        else:
            i+=1
        s+=1
        
    print(s)
    t-=1