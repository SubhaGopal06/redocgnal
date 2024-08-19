#Longest subset - same ends
#Input: 55 44 55 90 66 48 44 52 66 66
#Output: 66
a=list(map(int,input().split()))
d=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            c=a[i:j+1]
            d.append(c)
e=[]
for i in d:
    i=len(i)
    e.append(i)
r=max(e)
p=[]
for i in range(len(d)):
    s=len(d[i])
    if(s==r):
        t=d[i][0]
        p.append(i)
print(max(p))