import sqlite3
import pandas as pd

conn = sqlite3.connect('data.db')

conn.execute("DROP TABLE IF EXISTS Experiment")
conn.execute("DROP TABLE IF EXISTS Material")

conn.execute("CREATE TABLE Experiment(experiment_id INTEGER PRIMARY KEY,experiment_name TEXT NOT NULL,subject TEXT,duration_mins INTEGER)")

conn.execute("CREATE TABLE Material(material_id INTEGER PRIMARY KEY,experiment_id INTEGER NOT NULL,item TEXT,quantity_g INTEGER NOT NULL)")

conn.executemany("INSERT INTO Experiment VALUES(?,?,?,?)",[
       (1, 'Volcano Reaction', 'Chemistry', 20),
        (2, 'Plant Growth Test', 'Biology', 15),
        (3, 'Magnet Strength Test', 'Physics', 45),
        (4, 'Light Reflection', 'Physics', 30),
        (5, 'Water Filtration', 'Earth Science', 10),
    ])
    
conn.executemany("INSERT INTO Material VALUES (?, ?, ?, ?)", [
        (1, 1, 'Baking Soda', 100),
        (2, 1, 'Vinegar', 150),
        (3, 2, 'Soil', 250),
        (4, 2, 'Seeds', 20),
        (5, 3, 'Bar Magnet', 80),
        (6, 4, 'Mirror', 120),
        (7, 5, 'Sand', 150),
        (8, 5, 'Filter Paper', 10),
    ])

conn.commit()

Experiment = pd.read_sql("""SELECT * FROM Experiment""",conn)
print(Experiment)

Material = pd.read_sql("""SELECT * FROM Material""",conn)
print(Material)

Exp = pd.read_sql("""SELECT experiment_name AS Activity,subject AS Topic,duration_mins AS Time FROM Experiment""",conn)
print(Exp)

Inner_Join = pd.read_sql("""SELECT e.experiment_name AS Experiment,m.item AS Item FROM Experiment e INNER JOIN Material m ON e.experiment_id = m.experiment_id""",conn)
print(Inner_Join)

Subquery = pd.read_sql("SELECT e.experiment_id AS ID, e.experiment_name AS Activity,e.duration_mins AS Time,M.quantity_g AS G "
"FROM Experiment AS e INNER JOIN Material AS M ON e.experiment_id=M.experiment_id "
"WHERE e.experiment_id IN(SELECT e.experiment_id FROM Material WHERE quantity_g > 100)",conn)
print(Subquery)

Min = pd.read_sql("SELECT experiment_id AS ID, experiment_name AS Activity,duration_mins AS Time "
"FROM Experiment " 
"WHERE duration_mins =(SELECT MIN(duration_mins)FROM Experiment)",conn)
print(Min)

conn.close()