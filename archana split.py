a=open("archanasplit.txt","r")
b=a.read()
d=0
c=b.split()
i=0
while i<len(c):
    if c[i]in c:
        d=d+1
        i=i+1
print(c)
print(d)