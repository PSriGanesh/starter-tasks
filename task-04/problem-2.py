n=int(input())
for j in range(n):
    number=int(input())
    a=[]
    b=0
    v=0
    for i in range(number):
        if i<2:
            a.append(1)
        else:
            v=a[i-2]+a[i-1]
            if v>number:
                break
            elif v%2==0:
                b+=v
            a.append(v)
    print(b)
