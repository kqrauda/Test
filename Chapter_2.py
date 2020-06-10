import csv
import os
from datetime import date
from datetime import datetime


FILENAME = "tasks.csv"
today = date.today()
today = today.strftime("%d/%m/%Y")
print("Today:", today)

while True:
    print("\n====================","\n    TASK MANAGER   ","\n====================")
    print("1. Add task")
    print("2. Upgrade task")
    print("3. Remove task")
    print("4. List of all tasks")
    print("5. List of today's tasks")
    print("0. Exit")
    choise = input("Choose an option (0...5): ")
    choise = int(choise)
    if choise in range(6):
        if choise == 0:
            break
            
        elif choise == 1:           
            print("\n------------= ADD TASK =--------------")
            name = input("Input name: ")
            deadline = input("Input deadline (DD/MM/YYYY): ")
            dataHash = datetime.strptime(deadline, "%d/%m/%Y")
            dataHash = dataHash.strftime("%Y/%m/%d")
            description = input("Input description: ")           
            while True:
                save = input("Save task (Y/N)? ")
                if save.upper() == "Y":
                    taskHash = name[:3].upper() + "_" + dataHash
                    with open(FILENAME, "a", newline="") as file:
                        columns = ["name", "deadline", "description", "taskHash"]
                        writer = csv.DictWriter(file, fieldnames=columns)
                        # writer.writeheader()                 
                        task = {"name" : name, "deadline": deadline, "description": description, "taskHash": taskHash}
                        writer.writerow(task)
                    break
                elif save.upper() == "N":
                    break
                else:
                    print("You need input Y or N only!")
                    
        elif choise == 2:
            print("\n-----------= UPDATE TASK =------------")
            name = input("Edit name: ")
            deadline = input("Edit deadline: ")
            description = input("Edit description: ")
            while True:
                save = input("Save updates (Y/N)?: ")
                if save.upper() == "Y":
                    # update task and save file
                    break
                elif save.upper() == "N":
                    break
                else:
                    print("You need input Y or N only!")
                    
        elif choise == 4:
            if not os.path.exists(FILENAME):
                print("A list of tasks cannot be displayed now becouse file", FILENAME, "not found!")
            else:
                print("\n--------= LIST OF ALL TASKS =---------")
                with open(FILENAME, "r", newline="") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        print(row["name"], row["deadline"], row["description"], row["taskHash"])
                    input("\nPress Enter for continue...")
                    
        elif choise == 5:
            if not os.path.exists(FILENAME):
                print("A list of tasks cannot be displayed now becouse file", FILENAME, "not found!")
            else:
                print("\n------= LIST OF TODAY'S TASKS =-------")
                with open(FILENAME, "r", newline="") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row["deadline"] == today:
                            print(row["name"], row["deadline"], row["description"], row["taskHash"])
                input("\nPress Enter for continue...")
    else:
        print("Warning! Option number cannot be greater than 5!")
        continue  

print("Task Manager closed.")        