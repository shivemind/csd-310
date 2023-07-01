import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "EllieBobo31!*$",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    
    cursor = db.cursor()

    # First query: select all fields from the studio table
    cursor.execute("SELECT * FROM studio")
    print("--DISPLAYING studio RECORDS--")
    for (studio_id, studio_name) in cursor:
        print("Studio ID:", studio_id)
        print("Studio name:", studio_name)
        print()

    # Second query: select all fields from the genre table
    cursor.execute("SELECT * FROM genre")
    print("--DISPLAYING genre RECORDS--")
    for (genre_id, genre_name) in cursor:
        print("Genre ID:", genre_id)
        print("Genre name:", genre_name)
        print()

    # Third query: select movie names with runtime less than 2 hours
    cursor.execute("SELECT film_name, runtime FROM movies WHERE runtime < 120")
    print("--DISPLAYING short film RECORDS--")
    for (film_name, runtime) in cursor:
        print("Film name:", film_name)
        print("Runtime:", runtime)
        print()

    # Fourth query: select film names and directors ordered by director
    cursor.execute("SELECT film_name, director FROM movies ORDER BY director")
    print("--DISPLAYING Director RECORDS in Order--")
    for (film_name, director) in cursor:
        print("Film name:", film_name)
        print("Director:", director)
        print()
    
    input("\n\n Press any key to continue...")

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


