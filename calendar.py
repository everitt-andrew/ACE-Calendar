## Created by Andrew C. Everitt
## Final Project for CMPSC480 Software Innovations I
## Honor Code: This work is mine and solely mine unless otherwise cited.

## TODO: 1) Main function connect to account 2) Create event class 3) Create calculator function to find difference between dates 4) Clean up code & write comments

def main():
    response = input(" Welcome to the ACE Calendar! Please enter your UserID to access your account, type 'new' to make a new account, or 'quit' to exit: ")
    if response.upper() == "NEW":
        response2 = input(" Thanks for choosing ACE Calendar. Enter the UserID you would like to use: ")
        print(" Welcome ", response2)
        info = input(" We thank you for your interest in ACE Calendar, but we need some more information before you get started. Please enter your first and last names: ")
        info2 = input(" Great! Now enter your birthday as one, eight-digit number. For example, if your birthday is January 1, 1999, you would enter 01011999 (MMDDYYYY): ")
        info3 = input(" Please make note of your account details. Enter 'yes' if everything is correct or 'no' if something needs to be changed: ")
        if info3.upper() == "YES":
            print(" Your account has now been created.") #add code to create user
            interact()
        elif info3.upper() == "NO":
            print(" Your account has NOT been created. Returning to the main menu...")
            main()
        else:
            print(" The answer you provided is not 'yes' or 'no.' Returning to the main menu...")
            main()
    elif response.upper() == "QUIT":
        quit()
    else:
        print(" Welcome ", response)
        interact()
# end of main function

def interact():
    action = input("What action would you like to take today? Enter '1' to view event list, '2' to view priority list, '3' to add an additional event, '4' to delete an event, or '5' to switch users: ")
    if action == "1":
        answer = input(" Enter '1' to see your events, '2' to see global events, or '3' to see all events: ")
        if answer == "1":
            print(" Your events, based on date, are: ")
        elif answer == "2":
            print(" The global events, based on date, are: ")
        elif answer == "3":
            print(" The list of your events and the global ones, based on date, is as follows: ")
            ret = input(" Please type 'back' when you are ready to return to the action screen: ")
            if ret.upper() == "BACK":
                interact()
            else:
                print(" Please type 'back' when you are ready to return to the action screen: ")
        else:
            print(" The number you entered isn't an available option. Returning to the action screen...")
            main()
    elif action == "2":
        answer = input(" Enter '1' to see the priority of your events, '2' to see the priority of global events, '3' to see the priority of all events, or '4' to go back: ")
        if answer == "1":
            print(" Your events, from highest to lowest priority, are: ")
        elif answer == "2":
            print(" The global events, from highest to lowest priority, are: ")
        elif answer == "3":
            print(" The list of your events and the global ones, from highest to lowest priority, is as follows: ")
        elif answer == "4":
            print(" Returning to the action screen...")
            interact()
        else:
            print(" The number you entered isn't an available option. Returning to the action screen...")
            interact()
    elif action == "3":
        answer = input(" Please enter 'global' to create a global event, 'private' for an event that can only be seen by you, or type 'back' to go back: ")
        if answer.upper() == "GLOBAL":
            answer2 = input(" Please enter the name of the global event you want to add or type 'back' to go back: ")
            if answer2.upper() == "BACK":
                print(" Returning to the action screen...")
                interact()
            else:
                answer3 = input(" Now enter the date as one, eight-digit number. For example, if the event is January 1, 2019, you would enter 01012019 (MMDDYYYY):") #need to add check for past dates
        elif answer.upper() == "PRIVATE":
            answer2 = input(" Please enter the name of the private event you want to add or type 'back' to go back: ")
            if answer2.upper() == "BACK":
                print(" Returning to the action screen...")
                interact()
        else:
            print(" Returning to the action screen...")
            interact()
    elif action == "4":
        answer = input(" Please enter the name of the event you want to delete or type 'back' to go back: ")
    elif action == "5":
        main()
    else:
        print(" The number that you entered isn't an available option. Returning to main menu...")
        main()

# end of interact function

class User:
    """This class creates the user's profile, which stores name, userID, and up to 10 events."""
    def __init__(self, full_name, birthday): ## userID):
        self.name = full_name
        self.birthday = birthday #yyyymmdd
        #self.userID = userID #string
        # Extract the first and last names
        name_pieces = full_name.split(" ") #ret a list
        self.first_name = name_pieces[0] # first element
        self.last_name = name_pieces[1]  # second element
    #end of __init__()
#end of class

class Event:
    """This class creates the ability to create events with a name, date, and priority."""
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday #yyyymmdd
        #self.userID = userID #string
        #self.event = event #string
        # Extract the first and last names
        name_pieces = full_name.split(" ") #ret a list
        self.first_name = name_pieces[0] # first element
        self.last_name = name_pieces[1]  # second element
    #end of __init__()
#end of class


    def getToday(self):
        """returns today's data in yyyy-mm-dd format"""
        import datetime #library
        today = datetime.datetime.today().strftime('%Y-%m-%d') # On one line. Is a string
        yyyy = int(today[0:4])
        mm = int(today[5:7])
        dd = int(today[8:10])
        today = datetime.date(yyyy,mm,dd) #date of birth
        return today
        #end of getToday()

    def ageMethod(self):
        """Return the age of the person in years. Convert birthday to get these years."""
        yyyy_b = int(self.birthday[0:4])
        mm_b = int(self.birthday[4:6])
        dd_b = int(self.birthday[6:8])
         #date of birth
        dob = datetime.date(yyyy_b,mm_b,dd_b)
        today = self.getToday()
        age_in_days = (today - dob).days
        age_in_years = age_in_days/365
        return int(age_in_years)
        #end of age()

import datetime # library

#create another instance of this object with a new name

#help(User)
main()
