# Github Greenifier Bot

As a developer, I firmly believe well written and tested code is of utmost importance. Never write 100 lines when 10 will do. More lines, means more complexity, and more complexity increases risk of technical debt and failure. 

Therefore this project is to make my github look more green at a glance while I spend time upskilling and working on more technically challenging projects.

Currently I'm enhancing my C++, Recurison and Algorithm skills by taking <a href="https://see.stanford.edu/Course/CS106B">CS106B from Stanford Engineering Everywhere</a>. You can find any repos associated with that below.
- <a href="https://github.com/sagacious-solutions/CS106B-Practice">CS106B-Practice</a>

Previously I've also completed <a href="https://see.stanford.edu/Course/CS106A">CS106A</a> prior to learning version control.

For awesome examples of my work, see the below links.
 - <a href="https://www.youtube.com/watch?v=1xCQsEJd7FI">RGB Everywhere Commercial</a>
 - <a href="https://github.com/sagacious-solutions/rgb-everywhere-web-interface">RGB Everywhere Whole Home Lighting Solution</a>
 - <a href="https://github.com/sagacious-solutions/rgb-everywhere-hardware-api">RGB Everywhere Lighting Hardware API</a>
 - <a href="https://github.com/sagacious-solutions/Planet-Snake-HardwareAPI">Planet Snake Hardware API</a>
 - <a href="https://github.com/sagacious-solutions/planet-snake-website">Planet Snake React Website</a>
 - <a href="https://github.com/sagacious-solutions/alexa-holiday-lights">Alexa Holiday Lights</a>
 - <a href="https://github.com/sagacious-solutions/interview-scheduler">React JS Interview Scheduler</a>

# Deploying this bot

This bot constantly runs making commits to its self. When running, it will update the commit tracker with the current commit count for the day,
then it will commit and push that file. The bot is configured with email, so if the bot experiences an exception it will email you a screenshot
of the VMs desktop. It will still attempt to continue to run if theres an error. If you find yourself constantly getting error emails though,
the bot is likely hung.

 - Create a free tier ec2 instance with Windows Sever 2022 on AWS 
 - Configure the security group to allow for RDP Access from only your IP Address to prevent unwanted access
 - Connect via RDP to the new machine
   1) Install git for windows
   2) Install Python 3.9.x
   3) Generate ssh key, set your git credentials, copy the new ssh public key to your github
       ```
       ssh-keygen
       git config --global user.email "MY_NAME@example.com"
       git config --global user.name "FIRST_NAME LAST_NAME"
       ```
   4) Clone the repo onto the machine, and change to its directory
   5) Populate the .env file with the following keys
       USER : email address to send from
       PASS : email password for account
       RECIPIENT : email address to send the alert emails too    
   6) Create a virtual enviroment for the bot, install requirements, and run main.py
        ```
        python -m venv .venv
        .venv\scripts\activate
        pip install --upgrade pip
        pip install -r requirements.txt
        python main.py
        ```
   7) Exit the remote desktop via specific command to leave bot running after closing RDP connection
        ```
        qwinsta (This will give you rdp session name and number)
        C:\Windows\System32\tscon.exe rdp-tcp#1 /dest:console        
        ```
   
 
 
