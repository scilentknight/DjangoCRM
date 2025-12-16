# Install MySql on your computer
# https://dev.mysql.com/downloads/installer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    port=3307
)
# prepare a cursor object
cursorObject = database.cursor()

# create a database
cursorObject.execute("CREATE DATABASE codexcrm")

print("All Done!")