#Author:Alma, 2019
#Connect to database
import sqlite3
def db_conn():
    conn=sqlite3.connect('library.sqlite')
    return(conn)
