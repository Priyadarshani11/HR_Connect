from flask import Flask, render_template
from datetime import datetime
from my_utils.csv_operations import HandleCSV

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("Welcome.html")


@app.route("/task_one")
def task_one():
    data = HandleCSV.read_entire_csv()

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

    return render_template("task_one.html", emp_details=emp_details)


@app.route("/task_two")
def task_two():
    data = HandleCSV.read_entire_csv()
    emp_details = {}
    for i in data:
        if 110 > int(i["DEPARTMENT_ID"]) > 30 and int(i["SALARY"]) > 4200:
            date = i["HIRE_DATE"]
            date = datetime.strptime(date, "%d-%b-%y")
            date = date.strftime("%Y-%m-%d")
            emp_details.setdefault(date, [i["FIRST_NAME"] + " " + i["LAST_NAME"]])

    return render_template("task_two.html", emp_details=emp_details)
