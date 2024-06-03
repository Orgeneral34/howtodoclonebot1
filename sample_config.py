#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = "7462993574:AAGupJ-VV6YPDNO7kguJoFTb433cIZ__rXA"

    # Get from my.telegram.org
    APP_ID = int(27391583)

    # Get from my.telegram.org
    API_HASH = "ceb379be5a6706f6c3e3378fa231ee1b"

    # Generate a user session string
    TG_USER_SESSION = "Your_user_session_string_compatible_with_Pyrogram_v2"

    # Database URI
    DB_URI = "sqlite://Halil@C:\Users\Halil\Desktop\YOUR_USER YOUR_DB_NAME.db"


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
