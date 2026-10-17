#Open a file called report.txt in write mode.

file=open("report.txt","w")
file.write("I am learning Python")

# a is used to append

file=open("report.txt","a")
file.write("This is append")
file.close()

