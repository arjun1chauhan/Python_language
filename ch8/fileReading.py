file=open("report.txt","r")
data=file.read()
file.close()

#or

with open("report.txt","r") as f:
    data=f.read()
    print(data)


#Read line by line

with open("demofile1.txt","r") as g:
    data1=g.readline()
    data2=g.readline()
    print("This is 1st",data1)
    print("This is 2nd",data2)


#Read all lines

with open("demofile1.txt","r") as f:
    data=f.readlines()
    print(data)