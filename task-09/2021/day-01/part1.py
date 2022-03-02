a=int(input())
count=0
for i in range(1999):
    b=int(input())
    if b>a:
        count+=1
    a=b
print(count)
