# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID',"23990433"))
    API_HASH = str(getenv('API_HASH',"e6c4b6ee1933711bc4da9d7d17e1eb20"))
    BOT_TOKEN = str(getenv('BOT_TOKEN',"5822452610:AAEENVB1jI1cIaqI9Wsxxwl_I9ANSHLaQ20"))
    name = str(getenv('name', 'filetolinkbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', "-1001682397310"))
    PORT = int(getenv('PORT', "8080"))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', 'https://preliminary-alameda-skvillageboys.koyeb.app/'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "5821871362").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME',"sankar2k02"))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME',))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', "https://preliminary-alameda-skvillageboys.koyeb.app/")) if not ON_HEROKU or getenv('FQDN', 'https://preliminary-alameda-skvillageboys.koyeb.app/') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL',"mongodb+srv://Test:1234@cluster0.2bzsp0q.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', "-1001682397310"))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split())) 
