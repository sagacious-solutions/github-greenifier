from pathlib import Path
from datetime import datetime

from dotenv import dotenv_values
from RPA.Email.ImapSmtp import ImapSmtp
from RPA.Windows import Windows

from bot_config import bot_config

win = Windows()

def email_alert_on_failure(failure_msg: str = "") -> None :
    """Takes a screenshot of the desktop, then sends it the recipient
        from the dotenv

    Args:
        wait_between_commits_secs (int): Wait time to display in message
    """     
    email = ImapSmtp(**bot_config["email"])
    
    screenshot_path = screenshot_desktop(bot_config["path_for_screenshots"])
    
    email.authorize()    
    email.send_message(
        sender="GitHub Greenifier",
        recipients=[dotenv_values(".env")["RECIPIENT"]],
        subject="Your robot had a hiccup.",
        body=f"The robot has experienced a failure. Please check on it. \n{failure_msg}",
        attachments=[screenshot_path]
    )
                        
def screenshot_desktop(save_directory : Path = Path.cwd()) -> Path :
    save_directory.mkdir(parents=True, exist_ok=True)
    date_and_time = str(datetime.now()).split('.')[0].split(' ')
    filename = date_and_time[0] + ' ' + date_and_time[1].replace(':', '.') + '.png'
    return win.screenshot("desktop", save_directory / filename)

