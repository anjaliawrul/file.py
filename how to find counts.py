file =open("laxmi.txt",'r')
a=file.read()
c=0
for i in (a):
    c=c+len(i)
print(c)