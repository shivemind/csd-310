import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "EllieBobo31!*$",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

def show_films(cursor, title):
    cursor.execute("SELECT film_name AS Name, film_director AS Director, genre_name AS Genre, studio_name AS 'Studio Name' FROM film "
                   "INNER JOIN genre ON film.genre_id = genre.genre_id "
                   "INNER JOIN studio ON film.studio_id = studio.studio_id")
    films = cursor.fetchall()
    print("\n-- == {} == --".format(title))
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    cursor = db.cursor()

    show_films(cursor, "DISPLAYING FILMS")

    # insert a new record into the film table
    cursor.execute("INSERT INTO film (film_name, film_director, genre_id, studio_id, film_releaseDate, film_runtime) VALUES ('Star Wars', 'George Lucas', 2, 3, '1977', 121)")
    db.commit()

    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # update the film Alien to being a Horror film
    cursor.execute("UPDATE film SET genre_id = 2 WHERE film_name = 'Alien'")
    db.commit()

    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")

    # delete the movie Gladiator
    cursor.execute("DELETE FROM film WHERE film_id = 1")
    db.commit()

    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)

finally:
    if 'db' in locals() or 'db' in globals():
        db.close()