import pandas as pd

series = [1,2,3,4,5]
se = pd.Series(series, index = ["Keerthana","Sumaiyah","Oladipo","Satvik","Uzair"])
print(se)

Data = {
    "Name": ["Sumaiyah","Keerthana","Oladipo","Satvik","Uzair"],
    "Class": ["9","9","9","8","8"],
    "Country":["India","Qatar","","Qatar","India"]}

data1 = pd.DataFrame(Data)
print(data1)
print(data1.loc[0])

pa = pd.read_csv('country_vaccinations.csv')
print(pa)
print(pa.head())
print(pa.tail())

