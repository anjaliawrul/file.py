a=["singing","playing","dancing","sharing","sleeping","everthing","kho-kho"]
b=open("sai.txt","w")
i=0
while i<len(a):
    if "ing" in a[i]:
        b.write(a[i])
        b.write("\n")
    i=i+1
b.close()   