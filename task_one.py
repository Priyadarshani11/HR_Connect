"""
Write a program to get details of employees who's salary is > 9000. The output should
be in following format

{
"Name": "<first_name last_name>",
"email": "<email>",
"phone number": "<phone number without DOT>"
}
"""

from pprint import pprint
from my_utils.csv_operations import HandleCSV


data = HandleCSV.read_entire_csv()
def main():
    emp_details = {}
    j = 1
    for i in data:
        if int(i["SALARY"]) > 9000:
            phone_number = i["PHONE_NUMBER"].split(".")
            phone_number = "".join(phone_number)
            emp_details[j] = {
                "name": (i["FIRST_NAME"] + " " + i["LAST_NAME"]),
                "email": i["EMAIL"],
                "phone_number": phone_number,
            }
            j += 1

    return emp_details


if __name__ == "__main__":
    result = main()
    pprint(result)
