#create a class laptop with attributes brand,RaM,price. create two object with different values
class laptop:
    brand="macbook"
    RAM="64GB"
    price="120000"

obj1=laptop()
obj1.brand="Lenovo"
print("laptop brand is ",obj1.brand)
obj2=laptop()
obj2.RAM="12GB"
print("laptop RAM is ",obj2.RAM)