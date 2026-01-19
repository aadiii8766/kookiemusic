from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("22513641"))
API_HASH = getenv("94b048a304a268e50a816aeedfed055a")

BOT_TOKEN = getenv("8502208539:AAGFubaSt9J40PJEq3kCare50JuwjZibncc", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("8099478929"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+uGojToopWyJmNTZl")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/+fLVvGqzz_6s4NmFl")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
