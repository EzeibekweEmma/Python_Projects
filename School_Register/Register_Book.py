import datetime
import json
from os import path


def save_data(my_data) -> None:
    with open("data.json", "w") as out_file:
        json.dump(my_data, out_file, indent=2)

    print("Save to data")


def add_student(my_data) -> None:
    name = input("What your name? ")
    age = input("How old are you? ")
    dob = input("Enter Date of birth: ")
    parent_num = input("Enter your parent number: ")
    num_of_class_att = my_data["class_1"]["students"][0]["present"]

    my_data["class_1"]["students"].append({
        "name": name,
        "age": age,
        "parent number": parent_num,
        "Date of birth": dob,
        "present": [0 for i in num_of_class_att],
        "registered date": datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
    })

    my_data["class_1"]["total_num"] = len(my_data["class_1"]["students"])

    save_data(my_data)


def marking_attendance(my_data) -> None:
    student_att = my_data["class_1"]["students"]
    count = 0
    while count < len(student_att):
        try:
            mark = int(input("Is {:s} present? 0 or 1: ".format(student_att[count]["name"])))
            if mark == 1:
                student_att[count]["present"].append(1)
                print("marked present for {:s}".format(student_att[count]["name"]))
                count += 1
            elif mark == 0:
                student_att[count]["present"].append(0)
                print("marked absent for {:s}".format(student_att[count]["name"]))
                count += 1
            else:
                print("Enter 1 for present and 0 for absent")
        except:
            count = count
            print("Wrong input, Mark again")

    save_data(my_data)


def get_all_student(key) -> None:
    names_of_student = data["class_1"]["students"]

    arr = [names_of_student[i][key] for i in range(len(names_of_student))]

    print(arr)


# Check if file exists
if path.isfile('data.json') is False:
    print("File not found")
else:
    with open('data.json', "r") as my_file:
        data = json.load(my_file)

    # Verify existing list
    # print(data["class_1"])

    add_student(data)

    # marking_attendance(data)

    # print(len(data["class_1"]["students"][0]["present"]))

    # get_all_student("age")
