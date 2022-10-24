import os
from os import getenv
from dotenv import load_dotenv
if os.path.exists("local.env"):
    load_dotenv("local.env")
load_dotenv()
admins = {}

#:::::::::::::@OFFICIALHACKERERA

API_ID = int(getenv("API_ID", "13152319"))

API_HASH = getenv("API_HASH", "ba87df5eaee5018229c8f7c04a51e03c")

BOT_TOKEN = getenv("BOT_TOKEN", "5371685561:AAFl7iaV5Vw7rhoYc7i41_VbouoMxp7SMmU")

DEEPAK_SESSION = getenv("DEEPAK_SESSION", "BQAeIrRyabKukgs1-2vqvhtrfHdyW7i4Qy7o-n6eG-GfGAiJtOTSlGxlD5F-CwYuapLyOdwj9l-VuPebnl6ZXfRf2D2B9ot0A-4wKX1IvVLxIRSnyWkqsO-Du_NpecWWp_J8vM2x5Y60yO7tZZrEZuunp65s5ZcwvVbWVZB90XpzR5uuFpYli5JY-c5hq3dzpu07iP876H-Bn3bvQXufBmzI0fZe1_7GpM4ARkU4-RDjrDd7KU5Ez0ATxBf1InQmixKU2k9qX0zo5vx_g1i99k77N_INeN7WQqUwKMxpSaS45w1dpA2Wk9w6MX-1krrMyMxo0mj1zHFnoWLDOjSRz1SFAAAAATMjpU0A")

OWNER_ID = getenv("OWNER_ID", "5152941389")

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001880824438"))

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5152941389").split()))

MONGO_URL = os.environ.get("MONGO_URL", "")

OWNER_NAME = getenv("OWNER_NAME", "Rajanmusicxd")

BOT_NAME = getenv("BOT_NAME", "Rajan")

ASSISTANT_NAME = getenv("ASSISTANT_NAME", "【𝄞≛⃝.݆݆݆݆ۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗۗ🇷𝐀𝐉𝐀𝐍 ❤️ ≛⃝🇵𝗔𝗡𝗗𝗜𝗧")

GROUP_SUPPORT = getenv("GROUP_SUPPORT", "rajanmusic285")

UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "rajanmusic2852")

OWNER_USERNAME = getenv("OWNER_USERNAME", "RajanPanditxd")

ALIVE_NAME = getenv("ALIVE_NAME", "Rajan")

BOT_USERNAME = getenv("BOT_USERNAME", "Rajan_MusicBot")






UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ANIL-XD/A-X-MUSIC-BOT")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "master")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "5000"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/ab04d080f30e7a7f91991.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/ab04d080f30e7a7f91991.jpg")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
EMOJI = getenv("EMOJI", "🥀")
