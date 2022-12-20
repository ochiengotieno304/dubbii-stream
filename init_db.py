import sqlite3

connection = sqlite3.connect('database.sqlite')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO movies (title, link, quality, genre) VALUES (?, ?, ?, ?)",
            ('Black Adam', 's9e5cpyoa252', 'hd', 'action')
            )

cur.execute("INSERT INTO movies (title, link, quality, genre) VALUES (?, ?, ?, ?)",
            ('Amsterdam', 'wrlfq5ys2gxp', 'hd', 'action')
            )

cur.execute("INSERT INTO movies (title, link, quality, genre) VALUES (?, ?, ?, ?)",
            ('Jumanji The Next Level', 'qgakd0bxv6ri', 'hd', 'action')
            )

cur.execute("INSERT INTO movies (title, link, quality, genre) VALUES (?, ?, ?, ?)",
            ('Disenchanted', 'hxhvt1ycb8pj', 'hd', 'action')
            )

cur.execute("INSERT INTO movies (title, link, quality, genre) VALUES (?, ?, ?, ?)",
            ('Top Gun Maverick', '3aaqk5emh1s3', 'hd', 'action')
            )


connection.commit()
connection.close()
