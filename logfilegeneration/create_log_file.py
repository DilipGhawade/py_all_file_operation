from datetime import datetime


while True:

    action = input("Enter action: ")

    time = datetime.now()

    log = f"{time} -> {action}\n"


    with open("app.log", "a") as file:

        file.write(log)


    more = input("Add more logs? y/n: ")

    if more == "n":
        break