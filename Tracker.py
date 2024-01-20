'''
Class concerned with:
    1) Prompting user to add, update, or delete a workout
    2) Updating the database
    3) Querying the database

Example usage from command line:
    > Tracker add
    > Tracker delete
    > Tracker edit
    > Tracker query queryString
'''
import sys
class Tracker:
    # Constructor
    def __init__(self) -> None:
        pass
    
    # Add a new workout
    def add(self):
        return 'add'

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
    def update(self,responses):
        print('Updating: ' + responses)
        

if __name__ == "__main__":
    # Collect arguments
    action = sys.argv[1]
    if action == "query":
        assert len(sys.argv) >= 3,"For query, you need to pass a query string"
        queryString = sys.argv[2]

    # Construct tracker
    tracker = Tracker()

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
            responses = tracker.query(queryString)
            print(responses)
        case _:
            assert False, "Unrecognized input argument " + action
