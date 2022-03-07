d=0
x=0
for i in range(1000):
    b=input()
    if b[0]=='f':
        x+=int(b[len(b)-1])
    elif b[0]=='d':
        d+=int(b[len(b)-1])
    elif b[0]=='u':
        d-=int(b[len(b)-1])
print(d*x)
