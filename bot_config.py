from dataclasses import dataclass
from dotenv import dotenv_values
from pathlib import Path

email_config = dotenv_values(".env")

email_configuration = {
    "account" : email_config["USER"],
    "password" : email_config["PASS"],
    "smtp_server" : "smtp.gmail.com",  
    "smtp_port" : 587
}
   
bot_config = {
    "email": email_configuration,
    "path_for_screenshots" : Path.cwd() / "error_screenshots"    
}

