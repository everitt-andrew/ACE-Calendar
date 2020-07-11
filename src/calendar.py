## Created by Andrew C. Everitt
## Final Project for CMPSC480 Software Innovations I
## Honor Code: This work is mine and solely mine unless otherwise cited.

## TODO: 1) Main function connect to account 2) Create event class 3) Create calculator function to find difference between dates 4) Clean up code & write comments
import pickle as pc

def main():
    response = input(" Welcome to the ACE Calendar! Please enter your UserID to access your account, type 'new' to make a new account, 'list' to see all accounts, or 'quit' to exit: ")
    if response.upper() == "NEW":
        response2 = input(" Thanks for choosing ACE Calendar. Enter the UserID you would like to use: ")
        print(" Welcome ", response2)
        info = input(" We thank you for your interest in ACE Calendar, but we need some more information before you get started. Please enter your first and last names: ")
        info2 = input(" Great! Now enter your birthday as one, eight-digit number. For example, if your birthday is January 1, 1999, you would enter 01011999 (MMDDYYYY): ")
        info3 = input(" Please make note of your account details. Enter 'yes' if everything is correct or 'no' if something needs to be changed: ")
        if info3.upper() == "YES":
            return info, response2, info2
            print(" Your account has now been created.")
            make_account(info, response2, info2) #add code to create user
            interact()
        elif info3.upper() == "NO":
            print(" Your account has NOT been created. Returning to the main menu...")
            main()
        else:
            print(" The answer you provided is not 'yes' or 'no.' Returning to the main menu...")
            main()
    elif response.upper() == "LIST":
        print(" Here are all of the accounts: ")
        #print account list (name only)
        main()
    elif response.upper() == "QUIT":
        quit()
    else:
        print(" Welcome ", response)
        interact()
# end of main function

def make_account(info, response2, info2): #full name, userID, birthday
    account = User(info, response2, info2)
    return account

def make_event(answer, answer4, answer3, answer5): #userID, status, event name, date, priority
    event = Event(answer, answer4, answer3, answer5)
    return event

def interact():
    action = input("What action would you like to take today? Enter '1' to view event list, '2' to view priority list, '3' to add an additional event, '4' to delete an event, '5' to switch users, or '6' to quit: ")
    if action == "1": #event list by date
        answer = input(" Enter '1' to see your events, '2' to see global events, or '3' to see all events: ")
        if answer == "1": #showing personal events
            print(" Your events, based on date, are: ")
            print(account.userID)
            print(account.name)
            print(account.birthday)
            #code to print events
            ret = input(" Please type 'back' when you are ready to return to the action screen: ")
            if ret.upper() == "BACK":
                interact()
            else:
                print(" Response unknown, returning to the action screen... ")
                interact()
        elif answer == "2": #showing global events
            print(" The global events, based on date, are: ")
                #if status=global, print name and date
            #code to print events
            ret = input(" Please type 'back' when you are ready to return to the action screen: ")
            if ret.upper() == "BACK":
                interact()
            else:
                print(" Response unknown, returning to the action screen... ")
                interact()
        elif answer == "3": #showing personal and global events
            print(" The list of your events and the global ones, based on date, is as follows: ")
            ret = input(" Please type 'back' when you are ready to return to the action screen: ")
            if ret.upper() == "BACK":
                interact()
            else:
                print(" Response unknown, returning to the action screen... ")
                interact()
        else:
            print(" The number you entered isn't an available option. Returning to the main menu...")
            main()

    elif action == "2": #event list by priority
        answer = input(" Enter '1' to see the priority of your events, '2' to see the priority of global events, '3' to see the priority of all events, or '4' to go back: ")
        if answer == "1": #priority of personal events
            print(" Your events, from highest to lowest priority, are: ")
            ret = input(" Please type 'back' when you are ready to return to the action screen: ")
            if ret.upper() == "BACK":
                interact()
            else:
                print(" Response unknown, returning to the action screen... ")
                interact()
        elif answer == "2": #priority of global events
            print(" The global events, from highest to lowest priority, are: ")
            ret = input(" Please type 'back' when you are ready to return to the action screen: ")
            if ret.upper() == "BACK":
                interact()
            else:
                print(" Response unknown, returning to the action screen... ")
                interact()
        elif answer == "3": #priority of personal and global events
            print(" The list of your events and the global ones, from highest to lowest priority, is as follows: ") #if a global and personal event has the same priority, the event closest to the date is placed higher. If same date, global placed first.
            ret = input(" Please type 'back' when you are ready to return to the action screen: ")
            if ret.upper() == "BACK":
                interact()
            else:
                print(" Response unknown, returning to the action screen... ")
                interact()
        elif answer == "4":
            print(" Returning to the action screen...")
            interact()
        else:
            print(" The number you entered isn't an available option. Returning to the action screen...")
            interact()

    elif action == "3": #creating a new event
        answer = input(" Please enter 'global' to create a global event, 'private' for an event that can only be seen by you, or type 'back' to go back: ")
        if answer.upper() == "GLOBAL":
            answer2 = input(" Please enter the name of the global event you want to add or type 'back' to go back: ")
            if answer2.upper() == "BACK":
                print(" Returning to the action screen...")
                interact()
            else:
                answer3 = int(input(" Now enter the date as one, eight-digit number. For example, if the event is January 1, 2019, you would enter 01012019 (MMDDYYYY):")) #need to add check for past dates
                getToday() #returns todays date
                if today > answer3:
                    print(" The date you have entered has already passed. Returning to action screen... ")
                    interact()
                else:
                    answer4 = input(" Next, enter the name of your event: ")
                    answer5 = int(input(" Finally, enter the priority of this event (1 being the highest priority and please note that if an event with the designated priority exists, it will be moved to a lower priority): "))
                    #check for existing priority, changes priorities if needed
                    #create event object with date, name, and priority
        elif answer.upper() == "PRIVATE":
            answer2 = input(" Please enter the name of the private event you want to add or type 'back' to go back: ")
            if answer2.upper() == "BACK":
                print(" Returning to the action screen...")
                interact()
            else:
                answer3 = int(input(" Now enter the date as one, eight-digit number. For example, if the event is January 1, 2019, you would enter 01012019 (MMDDYYYY):")) #need to add check for past dates
                getToday() #returns todays date
                if today > answer3:
                    print(" The date you have entered has already passed. Returning to action screen... ")
                    interact()
                answer4 = input(" Next, enter the name of your event: ")
                answer5 = int(input(" Finally, enter the priority of this event (1 being the highest priority and please note that if an event with the designated priority exists, it will be moved to a lower priority): "))
                #check for existing priority, changes priorities if needed
                #create event object with date, name, and priority
        else:
            print(" Returning to the action screen...")
            interact()

    elif action == "4": #deleting an event
        answer = input(" Please enter the name of the event you want to delete or type 'back' to go back: ")
        if answer.back() == "BACK":
            print(" Returning to the action screen... ")
            interact()
        else:
            #checks to see if event with name exists
            answer2 = input(" Are you sure you want to delete the following event? Type 'yes to confirm: '")
            if answer2.upper() == "YES":
                #delete the event and change priorities
                print(" The event has been successfully deleted. Returning to the action screen... ")
                interact()
            else:
                print(" The event has not been deleted. Returning to the action screen... ")
                interact()
    elif action == "5":
        main()
    elif action == "6":
        quit()
    else:
        print(" The number that you entered isn't an available option. Returning to main menu...")
        main()

# end of interact function

class User:
    """This class creates the user's profile, which stores name, userID, and up to 10 events."""
    def __init__(self, info, reponse2, info2):
        self.name = response2
        self.birthday = info2 #yyyymmdd
        self.userID = info #string
        # Extract the first and last names
        name_pieces = response2.split(" ") #ret a list
        self.first_name = name_pieces[0] # first element
        self.last_name = name_pieces[1]  # second element
    #end of __init__()
#end of class

class Event:
    """This class creates the ability to create events with a name, date, and priority."""
    def __init__(self, userID, event_name, date, priority, status):
        self.userID = userID #string
        self.ename = event_name #string
        self.date = date #string
        self.priority = priority #int
        self.status = status #string
    #end of __init__()
#end of class


def getToday(self):
    """returns today's data in yyyy-mm-dd format"""
    import datetime #library
    today = datetime.datetime.today().strftime('%Y-%m-%d') # On one line. Is a string
    yyyy = int(today[0:4])
    mm = int(today[5:7])
    dd = int(today[8:10])
    today = datetime.date(yyyy,mm,dd) #todays date
    return today
    #end of getToday()

def daysAway(self):
    getToday(self)
    print(" This event is ___ days away")
    #end of daysAway()

import datetime # library

#create another instance of this object with a new name

#help(User)
main()
