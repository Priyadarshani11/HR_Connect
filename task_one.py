"""
Write a program to get details of employees who's salary is > 9000. The output should
be in following format

{
"Name": "<first_name last_name>",
"email": "<email>",
"phone number": "<phone number without DOT>"
}
"""


from my_utils.csv_operations import HandleCSV
from pprint import pprint

data = HandleCSV.read_entire_csv()

def main():

        emp_details = {}

        for column in (data):

            if int(column['SALARY']) > 9000:
                  emp_details['name'] = ((column['FIRST_NAME'] + " " + column['LAST_NAME']))
                  emp_details['email'] = column['EMAIL']
                  phone_number = column['PHONE_NUMBER'].split(".")
                  phone_number = "".join(phone_number)
                  emp_details['phone numer'] = phone_number
                  pprint(emp_details)

        return emp_details

if __name__ == "__main__":

    result=main()























