for _ in range(int(input())):
    N=int(input())
    L=list(input())
    alph=[]
    for i in range(26):
        x=chr(i+97)
        alph.append(x)
    minimum=N
    for i in range(26):
        count=0
        a1=0
        for j in range(N):
            if L[j]==alph[i]:
                count+=1
                if count==1:
                    a1=j
                elif count>1:
                    diff=j-a1
                    if diff<minimum:
                        minimum=diff
                    a1=j
    print(N-minimum)
