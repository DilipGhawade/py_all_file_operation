file = open("student.txt","r")

# Reads complete file
# data = file.read()
# print(data)

## Read Line by Line

for line in file:
    print(line)
file.close()