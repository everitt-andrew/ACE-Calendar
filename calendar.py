## Created by Andrew C. Everitt
## Final Project for CMPSC480 Software Innovations I
## Honor Code: This work is mine and solely mine unless otherwise cited.

## TODO: 1) Main function connect to account 2) Create event class 3) Create calculator function to find difference between dates 4) Clean up code

def main():
    response = input(" Welcome to the ACE Calendar! Please enter your UserID or type 'new' to make a new account: ")
    if response.upper() == "NEW":
        response2 = input(" Thanks for choosing ACE Calendar. Enter the UserID you would like to use: ")
        userID = response2
        print(userID)
# end of main function


class User:
    """This class creates the user's profile, which stores name, userID, and up to 10 events."""
    def __init__(self, full_name, birthday): ## userID, event):
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


    def ageMethod1(self):
        """Return the age of the person in years. Convert birthday to get these years."""
        today = datetime.date(2018, 10, 29)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy,mm,dd) #date of birth
        print( " Hi, I'm ageMethod1. dob = ",dob)
        age_in_days = (today - dob).days
        age_in_years = age_in_days/365
        return int(age_in_years)
        #end of age()

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

    def ageMethod2(self):
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
user = User("Frank Wright","18670608") # Make instance for Frank, June 8, 1867
print("    FullName: ",user.name)
print("       First: ",user.first_name)
print("        Last: ",user.last_name)
print("    Birthday: ",user.birthday)
print("  AgeMethod1: ",user.ageMethod1()) # old technique
#print("  AgeMethod2: ",user.ageMethod2()) #dynamic date getting


#create another instance of this object with a new name

#help(User)
main()
