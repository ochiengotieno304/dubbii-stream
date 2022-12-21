import sqlite3

connection = sqlite3.connect('database.sqlite')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO movies (title, link, quality, genre) VALUES (?, ?, ?, ?)",
            ('Black Adam', 'fmlqvrhrnbp2', 'hd', 'action')
            )

cur.execute("INSERT INTO movies (title, link, quality, genre) VALUES (?, ?, ?, ?)",
            ('Amsterdam', '8ihc90peu82m', 'hd', 'history')
            )

cur.execute("INSERT INTO movies (title, link, quality, genre) VALUES (?, ?, ?, ?)",
            ('Bullet Train', 'ix3hrd6u4434', 'hd', 'action')
            )

cur.execute("INSERT INTO movies (title, link, quality, genre) VALUES (?, ?, ?, ?)",
            ('Disenchanted', 'drumup3up78i', 'hd', 'fantacy')
            )

cur.execute("INSERT INTO movies (title, link, quality, genre) VALUES (?, ?, ?, ?)",
            ('Elvis', 'pt19bqwe3nl9', 'hd', 'biography')
            )

cur.execute("INSERT INTO movies (title, link, quality, genre) VALUES (?, ?, ?, ?)",
            ('High Heat', 'hsu5viqt2mt2', 'hd', 'action')
            )


connection.commit()
connection.close()
