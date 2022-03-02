def secret_password(message):
    b=[]
    c=[]
    z=""
    p=""
    if len(message)!=9:
        return "BANG! BANG! BANG!"
    else:
        for i in range(len(message)):
            b.append(message[i])
            if ord(message[i])>123 or ord(message[i])<97:
                return "BANG! BANG! BANG!"
        for j in range(len(b)):
            if j==0 or j==2:
                c.append(ord(b[j])-96)
            elif j==1:
                c.append(b[j])
            elif j>2 and j<6:
                c.insert(0,b[j])
            else:
                if b[j]=='z':
                    z+="a"
                else:
                    z+=chr(ord(b[j])+1)
        c.insert(3,z)
        p+=str(c[0])+str(c[1])+str(c[2])+str(c[3])+str(c[4])+str(c[5])+str(c[6])
        return p
