'''
Class concerned with:
    1) Prompting user to add, update, or delete a workout
    2) Updating the database
    3) Querying the database
    4) Creating a new database to hold 

Example usage from command line:
    > Tracker create databaseName.db
    > Tracker add
    > Tracker delete
    > Tracker edit
    > Tracker query queryString
'''
import sys
import sqlite3

class Tracker:
    # Constructor
    def __init__(self, database='zach2024.db'):
        self.Database = database

    # Create new database
    @staticmethod
    def makeDatabase(name):
        # Handle inputs
        if not '.db' in name:
            name = name + '.db'
        print('Creating database: ' + name)
        
        # Create database connection
        con = sqlite3.connect(name)
        cursor = con.cursor()

        # Fill database
        createTableStr = 'CREATE TABLE workouts(id INTEGER PRIMARY KEY ASC, date TEXT, timeOfDay TEXT, description TEXT, duration TEXT, feelingRating INTEGER CHECK(feelingRating <= 5 AND feelingRating >= 0))'
        cursor.execute(createTableStr)

        # Log when complete
        print('Database ' + name + ' created!')
    
    # Add a new workout
    def add(self):
        '''
        Collect the information we need:
            1) Description
            2) Date
            3) Time of day
            4) Feeling rating (0-5)
        '''
        date = input('What day did you workout? Format: MM/dd/yyyy \n')
        timeOfDay = input('What time of day did you work out? Pick one of ["morning", "afternoon", "evening"]\n')
        description = input('Describe your workout\n')
        duration = input('How long was this workout (in hours)?\n')
        rating = input('From 0-5, how did you feel about this workout?')

        outStr = 'INSERT INTO workouts (date, timeOfDay, description, duration, feelingRating) VALUES (%s, %s, %s, %s, %d)' %(date, timeOfDay, description, duration, rating)
        return outStr

    # Edit existing workout
    def edit(self):
        return 'edit'

    # Delete existing workout
    def deleteWorkout(self):
        return 'delete'

    # Query for workouts or information about workouts
    def query(self,queryString):
        return 'query'
    
    # Update database
    def update(self,updateString):
        con = sqlite3.connect(self.Database)
        cur = con.cursor()
        cur.execute(updateString)
        print('Update complete!')
        

if __name__ == "__main__":
    # Collect arguments
    action = sys.argv[1]
    if action in ["query","create"]:
        assert len(sys.argv) >= 3,"For query or create, you need a second argument"
        modifier = sys.argv[2]
    
    if len(sys.argv) > 3:
        db = sys.argv[3]
    else:
        db = 'zach2024.db'

    # Construct tracker
    tracker = Tracker(database=db)

    # Action based on what arguments were passed
    match action:
        case "add":
            responses = tracker.add()
            tracker.update(responses)
        case "edit":
            responses = tracker.edit()
            tracker.update(responses)
        case "delete":
            responses = tracker.deleteWorkout()
            tracker.update(responses)
        case "query":
            responses = tracker.query(modifier)
            print(responses)
        case "create":
            Tracker.makeDatabase(modifier)
        case _:
            assert False, "Unrecognized input argument " + action
