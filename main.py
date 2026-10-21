"""TASK 01"""

"""print("Hello ,I'm Programmer")
students = ["Ali" , "Sara" , "Umar"]
for x in students:
    print(x)"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def passed(self):
        if self.marks >= 50:
            return "Pass" 
        else:
            return "Fail"
    def __str__(self):
        return f"{self.name} ({self.marks})  {self.passed()}"
from course import load_course

course = load_course("Programming for AI", "marks.txt")

print(course)
print("Top student:", course.top_student())


s1 = Student("Ali" , 72)
s2 = Student("Sara" , 45)
s3 = Student("Umer" , 50)
"""print(s1.passed())
print(s2.passed())
print(s3.passed())"""
print(s1)
print(s2)
print(s3)











# Import the required class, exception and function
from course import Course, InvalidMarksError, load_course


# Test the Course class
c = Course("Programming for AI")
c.add_student("Ali", 88)
c.add_student("Sara", 92)
c.add_student("Omar", 75)

print(c)
print("Top student:", c.top_student())


# Test the custom exception
try:
    c.add_student("Bilal", 120)
except InvalidMarksError as e:
    print("Error:", e)


# Load students from the correct file
course = load_course("Programming for AI", "marks.txt")
print(course)
print("Top student:", course.top_student())


# Test a wrong filename
load_course("Programming for AI", "mark.txt")


