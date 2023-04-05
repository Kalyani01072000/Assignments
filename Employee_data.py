import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

# Create employee information
employee_data = {
    "employees": [
        {
            "Name": "John Doe",
            "DOB": "1985-07-15",
            "Height": "6'0\"",
            "City": "New York",
            "State": "New York"
        },
        {
            "Name": "Jane Smith",
            "DOB": "1990-04-20",
            "Height": "5'6\"",
            "City": "Los Angeles",
            "State": "California"
        },
        {
            "Name": "Mark Johnson",
            "DOB": "1988-11-30",
            "Height": "5'10\"",
            "City": "Chicago",
            "State": "Illinois"
        },
        {
            "Name": "Emma Brown",
            "DOB": "1995-02-10",
            "Height": "5'5\"",
            "City": "Houston",
            "State": "Texas"
        },
        {
            "Name": "Michael Wilson",
            "DOB": "1987-09-25",
            "Height": "5'11\"",
            "City": "Miami",
            "State": "Florida"
        }
    ]
}

# Write employee information into JSON file
with open('employee.json', 'w') as f:
    json.dump(employee_data, f)

# Read employee information from JSON file and create Employee objects
with open('employee.json', 'r') as f:
    data = json.load(f)
    employee_list = data['employees']
    employees = []
    for emp in employee_list:
        employee = Employee(emp['Name'], emp['DOB'], emp['Height'], emp['City'], emp['State'])
        employees.append(employee)

# Print the list of Employee objects
for emp in employees:
    print("Name:", emp.name)
    print("DOB:", emp.dob)
    print("Height:", emp.height)
    print("City:", emp.city)
    print("State:", emp.state)
    print("----")

