a=int(input())
b=int(input())
c=a*1024
d=c//b
if(d != c/b):
    d+=1
if(d>500):
    print(d*1)
elif(500<d<1000):
    e=d-500
    print((e*2)+500)
else:
    f=(d-1500)*3
    print(f+3000)
    