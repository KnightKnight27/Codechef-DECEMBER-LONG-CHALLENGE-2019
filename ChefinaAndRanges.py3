for _ in range(int(input())):
	N=int(input())
	X,Y=[],[]
	for i in range(N):
		H,Z=map(int,input().split())
		X.append([H,0])
		X.append([Z,1])
	X.sort()
	M=float("inf")
	count=0
	a=0
	for i in range(len(X)):
		if a==N:
			break
		if X[i][1]==0:
			count+=1
			a+=1
		else:
			count-=1
			if count<M:
				M=count
	if M<N-1:
		print(M)
	else:
		print("-1")
