d=0
x=0
a=0
for i in range(1000):
    b=input()
    if b[0]=='f':
        x+=int(b[len(b)-1])
        d+=a*int(b[len(b)-1])
    elif b[0]=='d':
        a+=int(b[len(b)-1])
    elif b[0]=='u':
        a-=int(b[len(b)-1])
print(d*x)
