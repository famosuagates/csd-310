import mysql.connector
from mysql.connector import errorcode

config = {                                  # Config Settings
    "user": "root",
    "password": "!!Vhbfmv2011201120",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}


def show_players(cursor, title):
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")     # Join query   
    players = cursor.fetchall()                                                                                                           # grab the results from the cursor 
    print("\n  -- {} --".format(title))

    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3])) # Loop over the player data set and display the results 

try: 
    db = mysql.connector.connect(**config)                                                      # Connect to the database 
    cursor = db.cursor()                                                                        # Get the cursor object
    add_player = ("INSERT INTO player(first_name, last_name, team_id)""VALUES(%s, %s, %s)")     # Insertion a player
    player_data = ("Gimli", "Shire Folk", 1)                                                  # The player data 
    cursor.execute(add_player, player_data)                                                     # Insertion of a new player record

    db.commit()                                                                                 # commit to the database  

    show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")                                                                             # show all records in the player table 
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Gimli', last_name = 'Ring Stealer' WHERE first_name = 'Gimli'")   # update the newly inserted record 
    cursor.execute(update_player)                                                                                                       # execute the update query


    show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")                                                                             # Show all records in the player table
    delete_player = ("DELETE FROM player WHERE first_name = 'Gimli'")                                                                  # Delete player
    cursor.execute(delete_player)
 
    show_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")                                                                             # Show all records in the player table
    input("\n\n  Press any key to continue... ")    

except mysql.connector.Error as err:                                                                                                    # Error 
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
    else:
        print(err)

finally:
    db.close()                                                                                                                         # Close the connection to MySQL