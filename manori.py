a=open("ganesh.txt","w")
for i in range(65,91):
    b=chr(i)
    a.write(b)
    a.write(' ')
a.close()