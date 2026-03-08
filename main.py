
# Expense Tracker Project

Expenses_List=[]

print("Welcome To Expense Tracker ")
print()

while True:
    print("=====MENU=====")
    print()

    print("1. Add Expense ")
    print("2. View All Expense ")
    print("3. View Total Expense ")
    print("4.Exit ")

    print()

    choice= int(input("Please Enter Your choise: "))

#ADD Expense
    if(choice==1):
        Date=input("Enter a Date: ")
        Category=input("Enter a Category(Food,Shopping,Travel,etc): ")
        Description=input("Enter Discription: ")
        Amount=int(input("Enter The Amount: "))


        expense={
            "Date":Date,
            "Category":Category,
            "Description":Description,
            "Amount":Amount
            
                }


        Expenses_List.append(expense)
        print("\nExpense Added Successfully")

#View All Expense 
    elif(choice==2):
        if(len(Expenses_List)==0):
            print("No Added Expenses ") 
        else:
            print("Your All Expenses: ")

            count=1

            for each_expense in Expenses_List:
                print(f"Expense_Number {count}--> {each_expense['Date']},{each_expense['Category']},{each_expense['Description']},{each_expense['Amount']}")
                count=count+1

#View Total Expense
    elif(choice==3):
        Total = 0
        for each_expense in Expenses_List:
            Total += each_expense["Amount"]

        print("\n Total Expense = ",Total)  


#Exit
    elif(choice==4):
        print("Thank You. ")
        break

    else:
        print("Invalid Choise. Try Again.")





