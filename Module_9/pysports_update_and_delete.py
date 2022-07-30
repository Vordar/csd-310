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

#Insert Smeagol record to player DB
cursor.execute("INSERT INTO player(first_name, last_name, team_id) VALUES ('Smeagol', 'Shire Folk', 1)")
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
player = cursor.fetchall()

#Print record after insert
print("\n  -- DISPLAYING PLAYERS AFTER INSERT --")
for i in player:
    print(f"\n Player ID: {i[0]}\n First Name: {i[1]}\n Last Name: {i[2]}\n Team Name: {i[3]}\n")

#Update Smeagol record (first, last and team)
cursor.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
player = cursor.fetchall()

#Print record after update
print("\n  -- DISPLAYING PLAYERS AFTER UPDATE --")
for i in player:
    print(f"\n Player ID: {i[0]}\n First Name: {i[1]}\n Last Name: {i[2]}\n Team Name: {i[3]}\n")

#Delete Gollum record from player DB
cursor.execute("DELETE FROM player WHERE first_name = 'Gollum'")
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
player = cursor.fetchall()

#Print record after deletion
print("\n  -- DISPLAYING PLAYERS AFTER DELETE --")
for i in player:
    print(f"\n Player ID: {i[0]}\n First Name: {i[1]}\n Last Name: {i[2]}\n Team Name: {i[3]}\n")

#Close cursor
cursor.close()

input("\n\n Press any key to continue...")

#Close the database
db.close()