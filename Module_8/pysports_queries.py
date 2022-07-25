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

#Query data
query = "SELECT team_id, team_name, mascot FROM team"

cursor.execute(query)
print("-- Displaying Team Records --")
#Print data from query
for team in cursor:
    print("Team ID: {}".format(team[0]))
    print("Team Name: {}".format(team[1]))
    print("Mascot: {}".format(team[2]))
    print()
#Repeat process targeting table player
query = "SELECT player_id, first_name, last_name, team_id FROM player"

cursor.execute(query)
print("-- Displaying Player Records --")
for player in cursor:
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {}".format(player[2]))
    print("Team ID: {}".format(player[3]))
    print()

#Close cursor
cursor.close()

input("\n\n Press any key to continue...")

#Close the database
db.close()