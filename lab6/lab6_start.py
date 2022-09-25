"""Startup code for Lab 6 SQLite database

Author: Luke Chang (xcha011@aucklanduni.ac.nz)
Date: 16/09/2022

NOTE:
- `sqlite3` is a built-in library, you do not need to create a virtual environment 
to run this code.
- Note that the location of the database matters, the root directory should be 
'cs235_lab_code/lab6'.
"""
import os
import sqlite3

print('ROOT:', os.getcwd())

connection = sqlite3.connect('covid-19.db')
cursor = connection.cursor()

response = cursor.execute('SELECT title FROM articles LIMIT 5;').fetchall()
print(*response, sep='\n')

################################################################################
# Task 4: Add your code here:


# Insert a comment to Article id=10 by 'fmercury'
cursor.execute(
    f"INSERT INTO comments (id, user_id, article_id, comment, timestamp) \
        VALUES (4, 2, 10, 'pog champ', datetime());"
)

# Insert a comment to Article id=20 by 'fmercury'
cursor.execute(
    f"INSERT INTO comments (id, user_id, article_id, comment, timestamp) \
        VALUES (5, 2, 20, 'not so pog champ', datetime());"
)

# Delete Article id=50
cursor.execute(
    f"DELETE FROM articles \
        WHERE id == 50;"
)

# Print all comments by 'fmercury'
response = cursor.execute(
    "SELECT * FROM comments \
        LEFT JOIN users ON comments.user_id = users.id;"
).fetchall()
print(*response, sep='\n')

################################################################################

connection.commit()
connection.close()
