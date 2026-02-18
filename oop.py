#object-oriented programming ~ approach of writing a program

class Student: #Class is point of reference/ blueprint of an object

#Attributes
    name = "Dan"
    age = 20
    grade = "A"
    gender = "Male"

#Behaviours ~ Functions/Methods
    def study(self):
        print("Student is studying")
    def motion(self):
        print("Student is walking")

# CREATING OBJECTS
student1 = Student()
print(student1.name)

student2 = Student()
print(student2.name)


student3 = Student()




