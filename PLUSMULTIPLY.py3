for _ in range(int(input())):
    N=int(input())
    L=list(map(int,input().split()))
    count0=0
    count2=0
    for i in L:
        if i==0:
            count0+=1
        elif i==2:
            count2+=1
    print((count0-1)*(count0)//2+(count2-1)*(count2)//2)
