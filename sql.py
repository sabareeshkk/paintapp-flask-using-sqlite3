import sqlite3

with sqlite3.connect('pics.db') as conn:
	cursor = conn.cursor()
	#cursor.execute("DROP TABLE IF EXISTS paintstore")
	cursor.execute("CREATE TABLE paintstore(id serial,title text,imagedata text);")
	
