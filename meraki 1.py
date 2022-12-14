# shimla=open("shimla.txt","a")
# delhi=open("delhi.txt","a")
# others=open("others.txt","a")
# f=open("people3.txt","r")
# a=f.read()
# b=a.split("/n")
# # print(b)
# i=0
# while i<len(b):
#     if "delhi" in b[i]:
#         delhi.write (b[i])
#         delhi.write("/n")
#     elif "shimla"in b[i]:
#         shimla.write(b[i])
#         shimla.write("/n")
#     else:
#         others.write(b[i])
#         others.write("/n")  
#     i=i+1
# f.close()      

my_file = open("people1.txt")
file_data = my_file.read()
print (file_data)
my_file.close()