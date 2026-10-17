#Expence Tracker Project

expenses=[] #list of expences in form of dictionary
print("Welcome to Expence Tracker")

while True:
    print("=====MENU=====")
    print("1. Add Expense")
    print("2. View all Expenses")
    print("3. View total Expense")
    print("4. Exit")

    choice=int(input("Please Enter Your Choice: "))

#ADD Expense
    if (choice==1):
        date=input("Please Enter the Date: ")
        category=input("Enter the Category of Expense(travel,food,fashion): ")
        description=input("Enter the Detail of Expense: ")
        amount=float(input("Enter the amount of Expense: "))

        expense={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }

        expenses.append(expense)
        print("The Expense is Added Successfully")

#View all Expenses
    elif(choice==2):
        if(len(expenses)==0):
            print("No Expense Added")
        else:
            print("Expense Detail")
            count=1
            for each in expenses:
                print(f"Expense Number{count} -> {each["date"]},{each["category"]},{each["description"]},{each["amount"]}")
                count=count+1


#View Total Spending
    elif(choice==3):
        total=0
        for each in expenses :
            total=total+each["amount"]
        print("\n Total Expense: ",total)


#Exit
    elif( choice==4):
        print("Thankyou Visit Again")
        break

    else:
        print("Invalid Input")
