a=open("diamond.txt","w")
a.write("i am awrul anjali  ")
a.write("i am from maharashtra ")
a.write("i have completed my 12th class ")
a.write ("i am pursing BA second year ")
a.close()
b=open("diamond.txt","r")
c=b.read(48)
print(c)
b.close()


