# a=open("dad.txt","w+")
# b=a.write("i am anjali")
# p=a.read()
# print(p)
# a.close()

a=open("dad.txt","w+")
b=a.write()
a.read("i am anjali")
print(b)



a=open("x mode.txt","x+")
b=a.read()
a.write("hlo")
print(b)


