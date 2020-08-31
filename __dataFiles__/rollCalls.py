
import csv

filename='symca.csv'

fields = [] 
rows = [] 

#fields = SR,Roll No.,Gr No.,Division,Name of the Student,Program,Year,Gender,Shift Name,Module Name,Category

with open(filename,'r') as file:
    csvreader=csv.reader(file)
    fields=next(csvreader)

    for row in csvreader:
        rows.append(row)

#print("Titles:\n"+(',').join(field for field in fields))
def getClassmates(roll_no):
    mates=[]
    for row in rows: 
        for i in range(1,4):
            if int(row[1]) == roll_no - i:
                mates.append(row[1]+' '+row[4].lower())
    return mates

def stringHandeler(str2):
    if '_' in str2:
        stra = str2.split('_')
        if ' ' in stra[1]:
            temp=[]
            for i in stra[1].split(' '):
                temp.append(i)
            stra[1]=temp[0]
            stra.append(temp[1])
        return stra

    elif '-' in str2:
        stra = str2.split('-')
        if ' ' in stra[1]:
            temp=[]
            for i in stra[1].split(' '):
                temp.append(i)
            stra[1]=temp[0]
            stra.append(temp[1])
        return stra
        
    elif ' ' in str2:
        stra=str2.split(' ')
        return stra

#print(getClassmates(54))
