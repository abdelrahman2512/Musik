from dotenv import load_dotenv
from os import environ

load_dotenv("config.env")

BOT_TOKEN = environ.get("BOT_TOKEN")
API_ID = int(environ.get("API_ID","7634570"))
API_HASH = environ.get("API_HASH","49265e23e8cb8218ac89d60777f280a6")
SUDO_USERS_ID = environ.get("SUDO_USERS_ID")
LOG_GROUP_ID = environ.get("LOG_GROUP_ID","-1001569455288")
MONGO_URL = environ.get("MONGO_URL","mongodb+srv://vampir:Al2552001@cluster0.yeaoc.mongodb.net/vampir?retryWrites=true&w=majority")
BASE_DB = MONGO_URL
BANNED_USERS = filters.user()
ARQ_API_URL = environ.get("ARQ_API_URL", "https://arq.hamker.in")
ARQ_API_KEY = environ.get("ARQ_API_KEY","PLBNYD-CGIRFG-RECXWF-UFZIOA-ARQ")
F_SUB_CHANNEL = environ.get("F_SUB_CHANNEL", "FA9SH")
OWNER_ID = int(environ.get("OWNER_ID","1970797144"))
