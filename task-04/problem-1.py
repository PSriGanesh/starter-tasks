n=int(input())
for i in range(n):
    num=int(input())
    a3=num//3
    a5=num//5
    a15=num//15
    three=a3
    five=a5
    fift=a15
    if a3*3>=num:
        three=a3-1
    if a5*5>=num:
        five=a5-1
    if a15*15>=num:
        fift=a15-1
    print(3*(three*(three+1)//2)+5*(five*(five+1)//2)-15*(fift*(fift+1)//2))
