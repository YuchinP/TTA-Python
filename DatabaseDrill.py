import sqlite3


a = input("name")
b = input("species")
c = input("iq")
rosterData = (a,b,c)

connection = sqlite3.connect(':memory:')

c = connection.cursor()

c.executescript("""

CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)

rosterValues =(
('Jean-Baptiste Zorg', 'Human', 122),
('Korben Dallas', 'Meat Popsicle', 100),
)

        

c.execute("INSERT INTO Roster VALUES(?,?,?)",rosterData)

c.execute("UPDATE Roster SET Species = ? WHERE Name = ? AND IQ = ?",

('Human', 'Korben Dallas', 100))
""")

