## Final Project by Andrew C. Everitt
## Computer Science 480: Sofware Innovations
## Honor Code: This work is mine and solely mine unless otherwise cited

## Project & Description
This project will develop the final project that my group and I worked on and failed to complete in its entirety during the Introduction to Computer Science course (111) during the Fall 2016 semester. It was intended to serve as a calendar that the user could run in order to plan for events (and assignments for students). In addition to serving the same purpose as any calendar application on a smartphone, it would feature a ranking system in which the user could assign numerical values to each event, encouraging them to finish higher priority items sooner, if possible. Furthermore, the application would be able to tell the user how many days until the event occurs or assignment is due regardless of the amount of time between it and the current date. It would also provide the user with reminders/check-ups depending on its priority. I would also like to add the ability to choose between different profiles so that different people could use the program without seeing all events that have been entered. If I had unlimited time to complete the project, I would want to implement a clean user-interface instead of running the program in the terminal.

## Building & Running the Program
The user simply needs to run the code `python3 calendar.py` in the terminal. If the user does not have Python, one can download it [here](https://www.python.org/downloads/) Due to the fact that the group was unable to finalize working code, my program was built from the ground up.

## Testing the Application
Throughout the development of the program, I conducted a plethora of tests to ensure that it was functioning as intended.

## Tools Used
The original version of the program was built in Java, but I have decided to use Python for this project because I am currently using it in my other computer science courses and personally find it more enjoyable. In order to get the program functioning as intended, I used several tools such as the datetime library in order the current date, the pickle package in order to save objects and their attributes to a text file to be used when the program is restarted (acting as the profile feature), and several classes, namely two that create an event and user objects.

## Results
Ultimately, the program doesn't work as intended. Despite enjoying Python, I struggled the most while trying to work with objects. Initially, I tried to find a way give an object's attributes its own attributes, but realized that it wouldn't work. For example, I wanted to make a user's events a part of the user object; with each event having its own properties such as the date and priority. Another challenge that I experienced during the development of the project was entering the user's inputs into the objects properties. A plethora of the tests that I conducted ended abruptly when the program couldn't process the information. This issue grew due to the fact that the way that I structured the program made it difficult to keep track of certain variables and by a multitude of variable type conflicts. Clearly, the project would have benefitted from additional work time as it was often on the backburner compared to other obligations. In all, the frustrations I experienced during the development process has ignited a desire to produce my intial vision and I hope to do so in the near future. 
