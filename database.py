import sqlite3

connection = sqlite3.connect("roommates.db", check_same_thread=False) 
#squlite3.connect() - creates roommates.db if it is not created or opens it , if it is already created
cursor = connection.cursor() #we need to create a cursor in order to make changes in our database
#retrieve data from it and give commands to it 

#execute() is a method of cursor - we do not need to use triple quotes -but it is the standard
#also we do not need to use capital letter - but it is the standard to use it in order to distinguise sql commands properly 
cursor.execute("""CREATE TABLE IF NOT EXISTS views(
count INTEGER
)
""")
#count INTEGER - creates a column of sorts which stores integers and count is the name of our coloum 

cursor.execute("SELECT * FROM views") 
# SELECT count FROM views - would work similarly since we only have one col
#SELECT - i  want to retrive/get some data from database (table-views)
# * - take every column from the table views

#doing the following is imp as .execute() doesn't really give us data in the form of a python variable, so we do the following
# fetchone - means take one row and give it to me (stored in tupples)
result = cursor.fetchone()

if result is None:
    cursor.execute("INSERT INTO views (count) VALUES (0)")
    #this is exactly what it says - insert the value 0 inside col of name count which is inside the table view

connection.commit() #this is what we use to makes changes in our database

def get_views(): #this function is what we will give to flask
    cursor.execute("SELECT count FROM views")
    result = cursor.fetchone()

    return result[0]

def increment_views():
    cursor.execute("UPDATE views SET count = count + 1")
    connection.commit()


'''
notes about sql-----

cursor.execute("SELECT count FROM views")

cursor.execute("SELECT * FROM users")

result = cursor.fetchone() 

#the chronology matter, .execute() and .fetchone() work in pairs, cursor will temporarly store the data it fetched from database internally
fetchone will use that data and only select the first row
'''