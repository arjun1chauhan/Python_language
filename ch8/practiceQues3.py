#Print how many lines are present in notes.txt
with open("notes.txt","r") as f:
    listOflines=f.readlines()
    print("Total no of lines",listOflines)
    print("Total no of lines",len(listOflines))