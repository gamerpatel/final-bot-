import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "20831039"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "ea20b722f7af827db12fb85f4d55238c")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("@Gujju_Boys_Uploder_bot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "7597020624"))
# ------------------X------------------------------
CREATOR_ID = int(os.environ.get("CREATOR_ID", "7597020624"))
LOG_CHANNEL_ID = int(os.environ.get("LOG_CHANNEL_ID", "-1003874496367"))


SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7597020624").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003874496367"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://gbot11007:gbot11007@cluster0.qnknxxh.mongodb.net/?appName=Cluster0")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1003874496367"))
