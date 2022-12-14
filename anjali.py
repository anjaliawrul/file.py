a=open("monika.txt","w")
a.write ("hello/n")
a.write("queen/n")
a.write("How are you")
a.close()
print("writing success")

a=open("monika.txt","r")
data=a.read()
print(data)
a.close()

a=open("monika.txt","rb")
data=a.read()
print(data)
a.close()

