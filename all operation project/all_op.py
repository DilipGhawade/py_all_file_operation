print("1.Write")
print("2.Append")
print("3.Read")

choice = input("Choose operations: ")

if choice == "1":
    file= open("demo.txt","w")
    text = input("Enter a text: ")
    file.write(text)
    file.close()
    print("Written successfully")
elif choice =="2":
    file = open("demo.txt","a")
    text= input("Enter a Text: ")
    file.write("\n"+text)
    file.close()
    print("Updated Successfully.")
elif choice =="3":
    # file = open("demo.txt","r")
    # print(file.read())
    # file.close()
    # Professional way to read the file
    with open("demo.txt","r") as file:
        print(file.read())
else:
    print("Invalid choice")