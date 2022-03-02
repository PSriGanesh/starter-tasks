b=[]
c=[]
for i in range(2000):
    a=int(input())
    b.append(a)
for j in range(len(b)-2):
    A=b[j]+b[j+1]+b[j+2]
    c.append(A)
count=0
for k in range(1,len(c)):
    if c[k]>c[k-1]:
        count+=1
print(count)
