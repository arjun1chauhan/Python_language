mark=[99,90,80,87]
fruit=["Apple","Mango","lichi",8]#any data type can be stored in list and is mutable

print(mark)

mark[1]=98#mutable
print(mark)

#Slicing
print(mark[1:3])

print(max(mark))
print(min(mark))
mark.append(88)
print(mark)
mark.sort()
print(mark)
mark.pop(1)#index value
print(mark)
