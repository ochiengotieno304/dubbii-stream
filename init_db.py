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

cur.execute("INSERT INTO movies (title, link, quality, genre) VALUES (?, ?, ?, ?)",
            ('Everything Everywhere All At Once', 'nde5tntm3ao7', 'hd', 'action')
            )

cur.execute("INSERT INTO movies (title, link, quality, genre) VALUES (?, ?, ?, ?)",
            ('Guillermo del Toros Pinocchio', 'g2uq7htwpngt', 'hd', 'action')
            )

cur.execute("INSERT INTO movies (title, link, quality, genre) VALUES (?, ?, ?, ?)",
            ('Luck', '6b40paum70kc', 'hd', 'action')
            )

cur.execute("INSERT INTO movies (title, link, quality, genre) VALUES (?, ?, ?, ?)",
            ('Mindcage', 'l2awsaesp5px', 'hd', 'action')
            )

cur.execute("INSERT INTO movies (title, link, quality, genre) VALUES (?, ?, ?, ?)",
            ('Nanny', '6cenp4zrms4d', 'hd', 'action')
            )

cur.execute("INSERT INTO movies (title, link, quality, genre) VALUES (?, ?, ?, ?)",
            ('Nope', 'tmdr9b89mw0s', 'hd', 'action')
            )

cur.execute("INSERT INTO movies (title, link, quality, genre) VALUES (?, ?, ?, ?)",
            ('Prey for the Devil', '5rnceihtjrnz', 'hd', 'action')
            )

cur.execute("INSERT INTO movies (title, link, quality, genre) VALUES (?, ?, ?, ?)",
            ('Resurrection', 'hwpdiawyqw0f', 'hd', 'action')
            )

cur.execute("INSERT INTO movies (title, link, quality, genre) VALUES (?, ?, ?, ?)",
            ('The Banshees of Inisherin', 'n26uv5b51q4a', 'hd', 'action')
            )

cur.execute("INSERT INTO movies (title, link, quality, genre) VALUES (?, ?, ?, ?)",
            ('The Batman', '7qf5plkohtri', 'hd', 'action')
            )

cur.execute("INSERT INTO movies (title, link, quality, genre) VALUES (?, ?, ?, ?)",
            ('The Fabelmans', '4j2l41lelrif', 'hd', 'action')
            )

cur.execute("INSERT INTO movies (title, link, quality, genre) VALUES (?, ?, ?, ?)",
            ('The Northman', 'igj1pw6by3z4', 'hd', 'action')
            )

cur.execute("INSERT INTO movies (title, link, quality, genre) VALUES (?, ?, ?, ?)",
            ('The Unbearable Weight of Massive Talent',
             'eaj3pch0x91f', 'hd', 'action')
            )

cur.execute("INSERT INTO movies (title, link, quality, genre) VALUES (?, ?, ?, ?)",
            ('Turning Red', '9iqzenyulola', 'hd', 'action')
            )

cur.execute("INSERT INTO radios (title, link) VALUES (?, ?)",
            ('Homeboyz Radio (KE)', 'http://homeboyzradio-atunwadigital.streamguys1.com/homeboyzradio'))

cur.execute("INSERT INTO radios (title, link) VALUES (?, ?)",
            ('Heart London (UK)', 'http://icecast.thisisdax.com/HeartLondonMP3'))

cur.execute("INSERT INTO radios (title, link) VALUES (?, ?)",
            ('NRG Radio (KE)', 'https://streamingv2.shoutcast.com/nrg-radio-ke'))

cur.execute("INSERT INTO radios (title, link) VALUES (?, ?)",
            ('Classic 105 (KE)', 'https://classic105-atunwadigital.streamguys1.com/classic105'))

cur.execute("INSERT INTO radios (title, link) VALUES (?, ?)",
            ('Ghetto Radio (KE)', 'https://stream.zeno.fm/kvudezx1h2zuv'))

cur.execute("INSERT INTO radios (title, link) VALUES (?, ?)",
            ('Radio Maisha (KE)', 'http://stream.zeno.fm/0nb1sqerqy5tv'))

cur.execute("INSERT INTO radios (title, link) VALUES (?, ?)",
            ('Capital FM (KE)', 'https://atunwadigital.streamguys1.com/capitalfm'))



connection.commit()
connection.close()
