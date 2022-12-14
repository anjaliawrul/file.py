a=open("myself.txt","r")
count=0
for line in a:
    word=line.split(" ")
    count+=1
a.close()
print("number of words in a text file",count)