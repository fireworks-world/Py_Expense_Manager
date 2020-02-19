from expenseData import listofExpense
import ast
import datetime


def readdata():
    fopen = open('expense.txt', 'r')
    data = fopen.read()
    d = ast.literal_eval(data)
    fopen.close()
    return d

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
    fopen=open('expense.txt','w')
    fopen.write(str(listofExpense))
    fopen.close()


def pushData(id,value):
    #id=['2020', '02', '19']
    #value=['Grocery', '200','others', '800']
    d=readdata()
    if id[0] in d:
        if id[1] in d[id[0]]:
            exp={id[2]:value}
            d[id[0]][id[1]].update(exp)



    # data={id[0]: {
    #     id[1]:{
    #         id[2]: value
    #         }
    #     }
    # }
    # listofExpense.update(data)
    saveData(d)
    return listofExpense




def insertExpense():
    dummydata=getexpense()
    dayToday=str(datetime.date.today())
    key=dayToday.split('-')
    savedData=pushData(key,dummydata)
    return savedData

def fetchData(userDate):
    d=readdata()
    date = userDate.split('-')
    exp = d[date[2]][date[1]][date[0]]
    counter = 1
    totalexpense = 0
    for i in range(int(len(exp) / 2)):
        totalexpense = totalexpense + int(exp[i + counter])
        counter += 1
    return totalexpense