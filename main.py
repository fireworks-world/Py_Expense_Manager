#create a expense manager for user
from logic import insertExpense,fetchData
print("-------Expense Manager-------")
flag=True
while flag:
    print("Press 'A' to add Expense\nPress 'V' to show expense")
    useroption=input(">>>Enter Your Option:")
    if (useroption=='a' or useroption=='A'):
        totalExpense=insertExpense()
        print("Data Saved Successfully")
        print(totalExpense)
    elif(useroption=='v' or useroption=='V'):
        userinput = input("Enter a date in dd-mm-yyyy: ")
        data=fetchData(userinput)
        print(data)
    else:
        print("Invalid Option!!! Plz Try Again")
