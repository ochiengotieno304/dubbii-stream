import sqlite3

connection = sqlite3.connect('database.sqlite')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO movies (title, link, genre) VALUES (?, ?, ?)",
            ('Black Adam', 's9e5cpyoa252', 'action')
            )

cur.execute("INSERT INTO movies (title, link, genre) VALUES (?, ?, ?)",
            ('Amsterdam', 'wrlfq5ys2gxp', 'action')
            )

cur.execute("INSERT INTO movies (title, link, genre) VALUES (?, ?, ?)",
            ('Jumanji The Next Level', 'qgakd0bxv6ri', 'action')
            )

cur.execute("INSERT INTO movies (title, link, genre) VALUES (?, ?, ?)",
            ('Disenchanted', 'hxhvt1ycb8pj', 'action')
            )

cur.execute("INSERT INTO movies (title, link, genre) VALUES (?, ?, ?)",
            ('Top Gun Maverick', '3aaqk5emh1s3', 'action')
            )


cur.execute("INSERT INTO movies (title, link, genre) VALUES (?, ?, ?)",
            ('Top Gun Maverick', '3aaqk5emh1s3', 'action')
            )

cur.execute("INSERT INTO movies (title, link, genre) VALUES (?, ?, ?)",
            ('Top Gun Maverick', '3aaqk5emh1s3', 'action')
            )

cur.execute("INSERT INTO movies (title, link, genre) VALUES (?, ?, ?)",
            ('Top Gun Maverick', '3aaqk5emh1s3', 'action')
            )
            
connection.commit()
connection.close()
