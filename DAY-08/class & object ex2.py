class Student:
    def display_details(self):
        print("Student:",self.stuNo)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)

student1 = Student()
student2 = Student()

student1.stuNo=1
student1.name = "Sridhar"
student1.age = 20
student1.marks = 85.5

student2.stuNo=2
student2.name = "Hari"
student2.age = 19
student2.marks = 89.4

student1.display_details()
student2.display_details()

output:
Student: 1
Name: Sridhar
Age: 20
Marks: 85.5
Student: 2
Name: Hari
Age: 19
Marks: 89.4

