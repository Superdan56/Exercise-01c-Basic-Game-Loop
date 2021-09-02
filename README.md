# Exercise-01c-Basic-Game-Loop
Exercise for MSCH-C220, 31 August 2021

A demonstration of this exercise is available at [https://youtu.be/2HulLdM7xPw](https://youtu.be/2HulLdM7xPw)

This exercise will give you our first taste of solving a problem using programming. You will be implementing a basic game loop.

Begin by Forking this repository. Check that it has been forked successfully; the repository should now read [your username]/Exercise-01c-Basic-Game-Loop

Edit the LICENSE and replace BL-MSCH-C220-F21 with your full name. Commit your changes.

Press the green "Code" button and select "Open in GitHub Desktop". Allow the browser to open (or install) GitHub Desktop. Once GitHub Desktop has loaded, you should see a window labeled "Clone a Repository" asking you for a Local Path on your computer where the project should be copied. Choose a location. Make sure the Local Path ends with "Exercise-01c-Basic-Game-Loop" and then press the "Clone" button. GitHub Desktop will now download a copy of the repository to the location you indicated.

Open the folder in VS Code. You should see four files: .gitignore, LICENSE, main.py, and README.md. Open main.py.

In main.py, you will see a dictionary (lines 5–29) that represents a simplified version of what might be exported from Twine. Your task is to implement a basic game loop to navigate the passages represented in this "world" dictionary.

This is a little tricky because the only reference we have to connect one passage to another is the "name" field. The "current" variable on line 31 holds the first location that should be displayed; that will be updated as the player chooses valid options. The "response" variable should hold the player's response as the game asks them "Where do you want to go?".

You can implement this however you would like to, but if this seems overwhelming, feel free to follow my video demonstration. When you are  done, run the program to make sure it is functioning correctly. Then, save your files and return to Github Desktop.

In GitHub Desktop, you should now see main.py highlighted. Add a Summary message at the bottom of that panel, and push the "Commit to master" button. On the right side of the top, black panel, you should see a button labeled "Push origin". Press that now.

In GitHub Desktop, you should now see main.py highlighted. Add a Summary message at the bottom of that panel (something like "Implements game loop"), and push the "Commit to master" button. On the right side of the top, black panel, you should see a button labeled "Push origin". Press that now.

If you return to and refresh your GitHub repository page, you should now see that your files have been changed (with a new date).

Now edit the README.md file. When you have finished editing, commit your changes, and then turn in the URL of the main repository page (https://github.com/[username]/Exercise-01d-Basic-Game-Loop) on Canvas.

The final state of the file should be as follows (replacing my information with yours):
```
# Exercise-01c-Basic-Game-Loop
Exercise for MSCH-C220, 31 August 2021

A simple version of a game loop, designed to navigate an interactive fiction world (contained in a dictionary), implemented in Python.

## Implementation
Created using Python 3.9

## References
[Zork, 1977 by Tim Anderson, Marc Blank, Dave Lebling, and Bruce Daniels](https://en.wikipedia.org/wiki/Zork)

## Future Development
None

## Created by
Daniel Wright
```
