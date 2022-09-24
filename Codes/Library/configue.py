#Author:Alma, 2019
#Create database
import sqlite3 
def create_database():
    database_name='library'
    TABLES = {}
    TABLES['books'] = (
        "CREATE TABLE IF NOT EXISTS `books` ("
        "  `book_no` INTEGER PRIMARY KEY AUTOINCREMENT,"
        "  `publish_date` TEXT  NULL,"
        "  `name` TEXT  NULL,"
        "  `summary` TEXT NULL,"
        "  `author` TEXT  NULL,"
        "  `genres_ids` TEXT NULL,"
        "  `number_of_copies` INTEGER NULL,"
        "  `Is_available` TEXT NULL"  
        ")")

    TABLES['customers'] = (
        "CREATE TABLE IF NOT EXISTS `customers` ("
        "  `customer_no` INTEGER PRIMARY KEY AUTOINCREMENT,"
        "  `birth_date` INTEGER NOT NULL,"
        "  `first_name` TEXT NOT NULL,"
        "  `last_name` TEXT NOT NULL,"
        "  `gender` TEXT NOT NULL,"
        "  `date_of_registration` INTEGER NOT NULL"
        ")")

    TABLES['genre'] = (
        "CREATE TABLE IF NOT EXISTS `genre` ("
        "  `genre_no` INTEGER PRIMARY KEY AUTOINCREMENT,"
        "  `name` TEXT NOT NULL"
        ")")

    TABLES['checkout'] = (
        "CREATE TABLE IF NOT EXISTS `checkout` ("
        "  `checkout_no` INTEGER PRIMARY KEY AUTOINCREMENT,"
        "  `customer_no` INTEGER NOT NULL,"
        "  `book_no` INTEGER NOT NULL,"
        "  `checkout_Date` INTEGER NOT NULL,"
        "  `returned_Date` INTEGER NULL,"
        "  FOREIGN KEY (`customer_no`) "
        "     REFERENCES `customers` (`customer_no`) ON DELETE CASCADE,"
        "  FOREIGN KEY (`book_no`) "
        "     REFERENCES `books` (`book_no`) ON DELETE CASCADE"
        ")")

    conn=sqlite3.connect('library.sqlite')
    cursor = conn.cursor()

    for table_name in TABLES:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='table_name'")
        if(not cursor.fetchall()):
            table_description = TABLES[table_name]
            cursor.execute(table_description)

    cursor.close()
    conn.close()
