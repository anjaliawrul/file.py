a=open("nikita.txt","r")
c=a.read()
b=c.split()
c=0 
count=0
i=0 
while i<len(b):
    j=0    
    while j<len(b[i]):
        if b[i][j]=="A" or b[i][j]=="a":
            c+=1 
        elif b[i][j]=="M" or b[i][j]=="m":
            count+=1
        j+=1
    i=i+1
print("A or a",c) 
print("M or m",count) 
print(b)
a.close()



