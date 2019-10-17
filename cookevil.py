t=int(input())
for i in range(t):
    n=int(input())
    l1=[]
    l2=[]
    c1,c2=0,0
    l=[int(x) for x in input().split()]
    for k in range(len(l)):
        if(k%2!=0):
            l2.append(l[k])
        else:
            l1.append(l[k])
    l1.sort(reverse=True)
    l2.sort(reverse=True)
    for p in range(int(len(l)/2)):
        if(l1[p]>l2[p]):
            c1=c1+1
        elif(l1[p]<l2[p]):
            c2=c2+1
        else:
            c1=c1+1
            c2=c2+1
    if(c1>c2):
        print("1")
    elif(c2>c1):
        print("2")
    else:
        print("draw") 
