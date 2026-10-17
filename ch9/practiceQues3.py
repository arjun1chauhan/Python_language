#create class student that takes 3 marks and has a method average().

class student:
    def __init__(self,name,listOfMarks):
        self.name=name
        self.listOfMarks=listOfMarks
        
        

    def average(self):
        sum=0
        for eachValue in self.listOfMarks:
            sum=sum+eachValue

        average=sum/3
        print("Average is: ",average)

student1=student("Arjun",[90,95,98])
student1.average()
