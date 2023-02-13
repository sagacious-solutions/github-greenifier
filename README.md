# Github Greenifier Bot

As a developer, I firmly believe well written and tested code is of utmost importance. Never write 100 lines when 10 will do. More lines, means more complexity, and more complexity increases risk of technical debt and failure. 

Therefore this project is to make my github look more green at a glance while I spend time upskilling and working on more technically challenging projects.

For awesome examples of my work, see the below links.
 - <a href="https://www.youtube.com/watch?v=1xCQsEJd7FI">RGB Everywhere Comercial</a>
 - <a href="https://github.com/sagacious-solutions/rgb-everywhere-web-interface">RGB Everywhere Whole Home Lighting Solution</a>
 - <a href="https://github.com/sagacious-solutions/Planet-Snake-HardwareAPI">Planet Snake Hardware API</a>
 - <a href="https://github.com/sagacious-solutions/planet-snake-website">Planet Snake React Website</a>
 - <a href="https://github.com/sagacious-solutions/react-christmas-tree">React Christmas Tree</a>
 - <a href="https://github.com/sagacious-solutions/raspberry-xmas-tree">Raspberry Christmas Tree</a>
 - <a href="https://github.com/sagacious-solutions/alexa-holiday-lights">Alexa Holiday Lights</a>

# Deploying this bot

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
   5) Create a virtual enviroment for the bot, install requirements, and run main.py
        ```
        python -m venv .venv
        .venv\scripts\activate
        pip install --upgrade pip
        pip install -r requirements.txt
        python main.py
        ```
   6) Exit the remote desktop via specific command to leave bot running after closing RDP connection
        ```
        qwinsta (This will give you rdp session name and number)
        C:\Windows\System32\tscon.exe rdp-tcp#1 /dest:console        
        ```
   
 
 
