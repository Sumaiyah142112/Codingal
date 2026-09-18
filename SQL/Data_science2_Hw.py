import pandas as pd

marks = [70,60,40,90,79]
series = pd.Series(marks,index= ["Sara","Jasima","Jasmine","Mariya","Eba"])

print(series)

Report = {
    "Student_Name":["Sara","Jasmia","Jasmine","Mariya","Eba"],
    "Subject_marks": [90,94,75,60,75],
    "Attendence": [222,240,350,299,300]
}
data = pd.DataFrame(Report)
print(data)
print(data.loc[1])

data.to_csv("marks.csv",index= False)

Students = pd.read_csv("marks.csv")


print("CSV File Ready!!")
print(Students.to_string)

print("Head & Tail /n")

print(Students.head(4))
print(Students.tail())
print(Students.info())

