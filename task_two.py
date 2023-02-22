"""
Write a program to get "HIRE DATE" of employee who's department is within range 30
to 110 AND who's salary is > 4200.
The output should be in following format.

{
"<HIRE DATE in YYYY-MM-DD format>": [
"<first_name last_name>",
...,
"<first_name last_name>"
],
}
"""


from datetime import datetime
from my_utils.csv_operations import HandleCSV


data = HandleCSV.read_entire_csv()

def main():

        emp_details = {}
        for column in data:
            if 110 > int(column['DEPARTMENT_ID']) > 30 and int(column['SALARY']) > 4200:
                date = column['HIRE_DATE']
                date = datetime.strptime(date, "%d-%b-%y")
                date = date.strftime("%Y-%m-%d")
                emp_details.setdefault(date, [column['FIRST_NAME'] +" " +column['LAST_NAME']])

        return emp_details

if __name__ == "__main__":
    print(main())



