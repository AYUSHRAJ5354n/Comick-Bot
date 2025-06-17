#___Every Variable Is Mandatory/Required So Fill Those With Causion___#


import logging

#--------------------------------------------------------------------------------------------------------------------------#
# Telegram API credentials
API_ID = 24500584 # Replace with your API_ID 
API_HASH = "449da69cf4081dc2cc74eea828d0c490" # Replace with your HASH
BOT_TOKEN = "" # Replace with your BOT TOKEN
BOT_UN = "Anime_donghuo_bot" # Replace with your BOT Username Without @


# MongoDB setup
DB_URL = "postgresql://postgres:AYUSHRA5354n@db.pxkqlgnluhnqrmvrreqq.supabase.co:5432/postgres" # Replace with your mongo db url
DB_NAME = "Comick" # Do Need To Change This 

# Admin and Channel details
ADMIN = 1685470205  # Replace with your Telegram user ID
CHANNEL = "-1002862417331" # Replace with your force sub channel username. add bot as admin in yourforce sub channel before start the bot  
DB_CHANNEL_UN = "Donghua_First"  # Replace with your File store channel username .Must Be Public
IS_NOTIFY = "True"   # "True" or "False". If "True" Then It Will Send New Aired Chapter Notification In DM

# Download directory
DOWNLOAD_DIRECTORY = "./downloads" # Do Need To Change This

# Copyright Banner
BANNER_PATH = "banner.jpg" # Replace with your Copyright Banner Path

#--------------------------------------------------------------------------------------------------------------------------#

# Logging configuration
LOGGING_CONFIG = {  # Do Not Change This
    'level': logging.INFO,
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'handlers': [
        logging.FileHandler("manga_bot.log"),
        logging.StreamHandler()
    ]
}
