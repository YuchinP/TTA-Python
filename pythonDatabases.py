import sqlite3

connection = sqlite3.connect("test_database.db")

c = connection.cursor()

#c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")

#c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)")

connection.commit()

#temporary one time database for tests ect
#connection = sqlite3.connect(':memory:')

c.execute("DROP TABLE IF EXISTS People")

connection.close()

'''simple and alternative way

with sqlite3.connect("test_database.db") as conenction:

perform any SQL operations useeing connection here'''
#With this no need to commit unless you want to see immediately

#multistrings
'''
import sqlite3

with sqlite3.connect('test_database.db') as connection

c = connection.curser()

c.executescript("""

DROP TABLE IF EXISTS People;

CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);

INSERT INTO People VALUES('Ron','Obvious','42');

""")
'''

#executemany()
peopleValues=(

('Ron','Obvious',42),

('Luigi','Vercotti',43),

('Arthur','Belling',28)

#or
#c.executemany("INSERT INTO People VALUES(?,?,?)", peopleValues)


 # select all first and last names from people over age 30

c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")

for row in c.fetchall():

print row
