class Employee:
    def __init__(self, name, age, salary, gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def employee_details(self):
        print("Name of employee is:", self.name)
        print("Age of employee is:", self.age)
        print("Salary of employee is:", self.salary)
        print("Gender of employee is:", self.gender)


emp = Employee("Sridhar", 23, 20000, "Male")
emp.employee_details()

output:
Name of employee is: Sridhar
Age of employee is: 23
Salary of employee is: 20000
Gender of employee is: Male
