for _ in range(int(input())):
    N=int(input())
    L=[0]*12
    for i in range(N):
        X,Y=map(int,input().split())
        if L[X]<Y:
            L[X]=Y
    ans=0
    for i in range(9):
        ans=ans+L[i]
    print(ans)
