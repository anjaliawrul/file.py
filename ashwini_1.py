file=open("ashwini_1.txt",'r')
c=file.read()
z=c.split()
count=0
i=0
while i<len(z):
    count+=1
    i+=1
print(count)
file.close()

# file =open("mathpati.txt",'')
# z=file.write("ashwini")
# print(z)
# file.close()

# file =open("mathpati.txt",'r')
# a=file.read()
# c=0
# for i in (a):
#     c=c+len(i)
# print(c)