import mysql.connector
from datetime import datetime

# contains al the datahandeling with te database
'''
def connection():
    # making a connection with the database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="codekid"
    )
    return mydb.cursor()
'''
def get_C():
    # making a connection with the database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="codekid"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT number, name FROM data")
    myresult = mycursor.fetchall()

    data = dict()
    for key, name in myresult:
        data[key] = name

    # return a dict with key as number and value as name
    return data

def info_C():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="codekid"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT name, explanation FROM data")
    myresult = mycursor.fetchall()

    data = dict()
    for name, explanation in myresult:
        data[name] = explanation

    # return a dict with key as name and value as explanation
    return data

# function that gets al scores from the database
def get_score():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="codekid"
    )
    mycursor = mydb.cursor()

    # query that selects the 5 users with the highest score
    mycursor.execute("SELECT name, score FROM score ORDER BY score DESC LIMIT 5")
    myresult = mycursor.fetchall()

    # list instead of a dict because the names of the users in the database are not unique 
    data = list()
    for name, score in myresult:
        data.append(f"Naam: {name}  Score: {score}")

    return data

# saves the name of the user and the score with a timestamp
def save_score(name, score):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="codekid"
    )
    mycursor = mydb.cursor()

    sql = "INSERT INTO score (name, score, datetime) VALUES (%s, %s, %s)"
    val = (name, score, datetime.now())
    mycursor.execute(sql, val)
    mydb.commit()