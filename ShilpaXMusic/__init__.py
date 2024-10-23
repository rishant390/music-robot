from ShilpaXMusic.core.bot import Shilpa
from ShilpaXMusic.core.dir import dirr
from ShilpaXMusic.core.git import git
from ShilpaXMusic.core.userbot import Userbot
from ShilpaXMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Shilpa()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
