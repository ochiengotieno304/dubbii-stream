DROP TABLE IF EXISTS movies;
CREATE TABLE movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    link TEXT NOT NULL,
    quality TEXT NOT NULL,
    genre TEXT NOT NULL
);

DROP TABLE  IF EXISTS radios;
CREATE TABLE radios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    name TEXT NOT NULL,
    url TEXT NOT NULL
);


-- DROP TABLE IF EXISTS requests;
-- CREATE TABLE requests (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
--     user TEXT NOT NULL,
--     title TEXT NOT NULL,
-- );
