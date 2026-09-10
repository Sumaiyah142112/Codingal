import sqlite3

import pandas as pd

conn = sqlite3.connect('database.db')

conn.execute("DROP TABLE IF EXISTS Attraction")
conn.execute("DROP TABLE IF EXISTS Destination")

conn.execute("CREATE TABLE Destination (Destination_id INTEGER PRIMARY KEY,Destination_name TEXT,Country TEXT NOT NULL)")
conn.execute("CREATE TABLE Attraction(Attraction_id INTEGER PRIMARY KEY,Attraction_name TEXT, Destination_id  INTEGER)")

conn.executemany("INSERT INTO Destination VALUES(?,?,?)",[

        (1,'Paris','France'),

        (2,'Riyadh','KSA'),

        (3,'Istanbul','Turkey'),

        (4,'California','USA'),

        (5,'London','UK'),

    ])

conn.executemany("INSERT INTO Attraction VALUES(?,?,?)",[

        (1,'Eiffel Tower',1),

        (2,'Time Square',10),

        (3,'GO karting',7),

        (4,'Disney land',4),

        (5,'Rumeli Fortress',3),

        (6,'Big Ben',5),

        (7,'Workshops',6),

        (8,'Kingdom Tower',2),

    ])

conn.commit()



Destiantion = pd.read_sql("""SELECT * FROM Destination""",conn);
print(Destiantion)

Attraction = pd.read_sql("""SELECT * FROM Attraction""",conn);
print(Attraction)

Inner = pd.read_sql("""SELECT Destination.Destination_id AS ID,Destination.Destination_name AS Name,Attraction.Attraction_name FROM Destination INNER JOIN Attraction ON Destination.Destination_id= Attraction.Destination_id""",conn);
 
print(Inner)

Left = pd.read_sql("""SELECT Destination.Destination_id,Destination.Country,Destination.Destination_name,Attraction.Attraction_name FROM Destination LEFT JOIN Attraction ON Destination.Destination_id = Attraction.Destination_id""",conn);
print(Left)

Cross = pd.read_sql("""SELECT * FROM Destination CROSS JOIN Attraction WHERE Destination.Destination_id <= 2""",conn);
print(Cross)

Union = pd.read_sql("""
SELECT Destination_name AS Place, 'Destination' AS type
FROM Destination

UNION

SELECT Attraction_name AS Place, 'Attraction' AS type
FROM Attraction
""", conn)

print(Union)

conn.close()
