import json
import re

with open('employee_data.json') as fin:
    contents = fin.read()

employee_data = json.loads(contents)

print("Search mode\n")
print("1:employee_number\n")
print("2:name\n")
print("3:email\n")
print("4:phone\n")

try:
    print("Select Number(1/2/3/4) :", end="")
    flag = int(input())

    flag2 = 0

    if flag == 1:
        print("search :", end="")
        pattern = str(input())

        for employee in employee_data:
            m = re.search(pattern, str(employee["employee_number"]))
            if m:
                print("number :", employee["employee_number"])
                print("name :", employee["name"])
                print("email :", employee["email"])
                print("phone :", employee["phone"])
                flag2 = 1

    elif flag == 2:
        print("search :", end="")
        pattern = str(input())

        for employee in employee_data:
            m = re.search(pattern, str(employee["name"]))
            if m:
                print("number :", employee["employee_number"])
                print("name :", employee["name"])
                print("email :", employee["email"])
                print("phone :", employee["phone"])
                flag2 = 1

    elif flag == 3:
        print("search :", end="")
        pattern = str(input())

        for employee in employee_data:
            m = re.search(pattern, str(employee["email"]))
            if m:
                print("number :", employee["employee_number"])
                print("name :", employee["name"])
                print("email :", employee["email"])
                print("phone :", employee["phone"])
                flag2 = 1

    elif flag == 4:
        print("search :", end="")
        pattern = str(input())

        for employee in employee_data:
            m = re.search(pattern.lstrip("+"), str(employee["phone"]))
            if m:
                print("number :", employee["employee_number"])
                print("name :", employee["name"])
                print("email :", employee["email"])
                print("phone :", employee["phone"])
                flag2 = 1

    else:
        print("Error")
        flag2 = 2

    if flag2 == 0:
        print("Not found")
    elif flag2 == 2:
        pass

except ValueError:
    print("Error")
