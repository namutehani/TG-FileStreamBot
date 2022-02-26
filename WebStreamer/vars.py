# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from os import environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    MULTI_CLIENT = False
    API_ID = 19969226
    API_HASH = "c7b7138d241b136382f50f9fc2b4005e"
    BOT_TOKEN = "5243106034:AAFkOwkHBfvX6yJhNS2GbOEIdWV7VRejZH4"
    SLEEP_THRESHOLD = int(environ.get("SLEEP_THRESHOLD", "60"))  # 1 minte
    WORKERS = int(environ.get("WORKERS", "6"))  # 6 workers = 6 commands at once
    BIN_CHANNEL = -1001641179917
    PORT = int(environ.get("PORT", 8080))
    BIND_ADDRESS = "0.0.0.0"
    PING_INTERVAL = 500
    HAS_SSL = environ.get("HAS_SSL", False)
    HAS_SSL = True if str(HAS_SSL).lower() == "true" else False
    NO_PORT = environ.get("NO_PORT", False)
    NO_PORT = True if str(NO_PORT).lower() == "true" else False
    if "DYNO" in environ:
        ON_HEROKU = True
        APP_NAME = str(environ.get("APP_NAME"))
    else:
        ON_HEROKU = False
    FQDN = (
        str(environ.get("FQDN", BIND_ADDRESS))
        if not ON_HEROKU or environ.get("FQDN")
        else APP_NAME + ".herokuapp.com"
    )
    if ON_HEROKU:
        URL = f"https://{FQDN}/"
    else:
        URL = "http{}://{}{}/".format(
            "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
        )
