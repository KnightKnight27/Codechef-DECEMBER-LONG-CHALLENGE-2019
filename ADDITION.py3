# import sys
# sys.stdin=open("input1.in","r")
# sys.stdout=open("outpul.out","w")  
def makeEqualLength(str1, str2): 
    len1 = len(str1)     
    len2 = len(str2)     
    if len1 < len2: 
        str1 = (len2 - len1) * '0' + str1 
        len1 = len2 
    elif len2 < len1: 
        str2 = (len1 - len2) * '0' + str2 
        len2 = len1 
    return len1, str1, str2 
def addBitStrings(first,second,length): 
    ha=0
    maximum=0
    count=1
    carry=0
    for i in range(length - 1, -1, -1):
        firstBit=int(first[i]) 
        secondBit=int(second[i])
        if carry==0:
            if firstBit==1 and secondBit==1:
                carry=1
                if count==1:
                    count+=1
        elif carry==1:
            if firstBit!=secondBit:
                ha+=1
            else:
                if ha>maximum:
                    maximum=ha
                if firstBit==1 and secondBit==1:
                    carry=1
                else:
                    carry=0
                ha=0
        if ha>maximum:
            maximum=ha
    return maximum+count
for _ in range(int(input())):
    X=input()
    Y=input()
    if int(Y,2)==0:
        print(0)
    else:
        N,X,Y=makeEqualLength(X,Y)
        ans=addBitStrings(X,Y,N)
        print(ans)

      
