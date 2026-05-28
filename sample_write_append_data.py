file = open("student.txt","w")
file.write("Name: Dilip \n")
file.write("Course: Python\n")
file.write("Age: 32\n")
file.close()
print("file creted and dagta written")

# append the file 

file= open("student.txt","a")
file.write("\nCity: Pune")
file.write("\nSkill: Python")
file.close()

print("Data updated.")