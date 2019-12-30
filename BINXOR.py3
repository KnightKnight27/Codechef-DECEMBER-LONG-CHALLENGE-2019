fact=[0]*(100001)
fact[0]=1
for i in range(1,10**5+1):
    fact[i]=(fact[i-1]*i)%1000000007
for _ in range(int(input())):
    N=int(input())
    X1=input()
    X2=input()
    ca0=X1.count("0")
    ca1=N-ca0
    cb0=X2.count("0")
    cb1=N-cb0
    ma=min(ca0,cb1)
    ma=ma+min(ca1,cb0)
    mi=min(ca0,cb0)
    mi=N-(mi+min(cb1,ca1))
    result=0
    x=10**9+7
    for i in range(mi,ma+1,2):
        result=result+(fact[N]%x)*(pow(fact[i]*fact[N-i],x-2,x))
    print(result%1000000007)
    
