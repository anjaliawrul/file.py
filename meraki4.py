batch1_student=["shivam","rahul","kavay","dhannu","deepanshu"]
students_file=open("navgurukul_students.html","w")
students_file.write("\n")
students_file.write("\n")
students_file.write("\n")
students_file.write("\n")
students_file.write("\n")
students_file.write("\n") 
for student in batch1_student:
    students_file.write(""+student+"\n")
students_file.write("\n")
students_file.write("\n")
students_file.close()


my_files=open("test_file4.txt","w")
my_files.write("yahan main kuch likha")
my_files.write("\nyaha main kuch aur bhi likha.")
my_files.close()