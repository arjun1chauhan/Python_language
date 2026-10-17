#Read only the first line of bio

with open("bio.txt","r") as g:
    data=g.readline()
    print(data)