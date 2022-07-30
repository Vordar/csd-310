import mysql.connector
#Configuration
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}
#Connect to database
db = mysql.connector.connect(**config)

#Create cursor
cursor = db.cursor()

#Run query
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
player = cursor.fetchall()

#Print data from query
print("\n  -- DISPLAYING PLAYER RECORDS --")
for i in player:
    print(f"\n Player ID: {i[0]}\n First Name: {i[1]}\n Last Name: {i[2]}\n Team Name: {i[3]}\n")

#Close cursor
cursor.close()

input("\n\n Press any key to continue...")

#Close the database
db.close()