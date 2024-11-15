import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "26187953"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1c3051e447b0e1c5ddf03fb3a62869fc")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://dharmveerydv883:skYixZdRBcAC9UeW@cluster0.nne6c.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
