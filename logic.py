from expenseData import listofExpense
import ast
import datetime
def getexpense():
    choice='y'
    totalexpense=[]
    while True:
        if(choice=='n'):
            break
        elif(choice=='y'):
            expenseamt=input(">>>Enter Expense Amount: ")
            expensefor=input(">>>Enter Expense Remark: ")
            totalexpense.extend([expensefor,expenseamt])
            choice=input(">>>Do you want to enter more expense(y/n):")
    return totalexpense


def saveData(listofExpense):
    fopen=open('expense.txt','a')
    fopen.write(str(listofExpense))
    fopen.close()


def pushData(id,value):
    data={id[0]: {
        id[1]:{
            id[2]: value
            }
        }
    }
    listofExpense.update(data)
    saveData(listofExpense)
    return listofExpense




def insertExpense():
    dummydata=getexpense()
    dayToday=str(datetime.date.today())
    key=dayToday.split('-')
    savedData=pushData(key,dummydata)
    return savedData
def fetchData(userDate):
    fopen = open('expense.txt', 'r')
    data=fopen.read()
    d=ast.literal_eval(data)
    fopen.close()
    date = userDate.split('-')
    exp = d[date[2]][date[1]][date[0]]
    counter = 1
    totalexpense = 0
    for i in range(int(len(exp) / 2)):
        totalexpense = totalexpense + int(exp[i + counter])
        counter += 1
    return totalexpense