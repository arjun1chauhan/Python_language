class student:
    schoolname="ABC School"

    def __init__(self,name,course):
        self.name=name
        self.course=course

student1=student("Arjun","B.Tech")
print("Student1 Name: ",student1.name)
print("Student1 Course: ",student1.course)

student2=student("Vivek","B.Tech")
print("Student2 Name: ",student2.name)
print("Student2 Course: ",student2.course)