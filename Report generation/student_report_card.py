name = input("Enter student name: ")
python = int(input("Python marks: "))
java = int(input("Java marks: "))
sql = int(input("SQL marks: "))

total = python + java + sql

avarage = total/3
report = f"""
----------STUDENT REPORT CARD-----------
Name: {name}
Python: {python}
Java: {java}
SQL: {sql}

Total: {total}

Avarage: {avarage}
"""
with open(f"{name}_report.txt","w") as file:
    file.write(report)
print("Report Generated successfully.")
