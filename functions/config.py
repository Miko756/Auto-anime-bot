#    This file is part of the AutoAnime distribution.
#    Copyright (c) 2024 Kaif_00z
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/kaif-00z/AutoAnimeBot/blob/main/LICENSE > .

# if you are using this following code then don't forgot to give proper
# credit to t.me/kAiF_00z (github.com/kaif-00z)

from decouple import config


class Var:
    # Version

    __version__ = "v0.0.8"

    # Telegram Credentials

    API_ID = config("API_ID", "27692015")
    API_HASH = config("API_HASH", "25278a8394b5914ee1b8d6a6c79d572d")
    BOT_TOKEN = config("BOT_TOKEN", "7716433955:AAFyRm41MWU-K0MslxcRWvE5tOYFMCS3pO8")
    SESSION = config("SESSION", default=None)

    # Database Credentials

    MONGO_SRV = config("MONGO_SRV", "mongodb+srv://Premium:aloksingh@cluster0.4ykpo.mongodb.net/?retryWrites=true&w=majority")

    # Channels Ids

    BACKUP_CHANNEL = config("BACKUP_CHANNEL", "-1002266633867")
    MAIN_CHANNEL = config("MAIN_CHANNEL", "-1002329482262")
    LOG_CHANNEL = config("LOG_CHANNEL", "-1002381050327")
    CLOUD_CHANNEL = config("CLOUD_CHANNEL", "-1002482492010")
    FORCESUB_CHANNEL = config("FORCESUB_CHANNEL", "0")
    OWNER = config("OWNER", "7092511418")

    # Other Configs

    THUMB = config(
        "THUMBNAIL", default="https://graph.org/file/ad1b25807b81cdf1dff65.jpg"
    )
    FFMPEG = config("FFMPEG", default="ffmpeg")
    CRF = config("CRF", default="27")
    SEND_SCHEDULE = config("SEND_SCHEDULE", default=False, cast=bool)
    RESTART_EVERDAY = config("RESTART_EVERDAY", default=True, cast=bool)
    LOG_ON_MAIN = config("LOG_ON_MAIN", default=False, cast=bool)
    FORCESUB_CHANNEL_LINK = config("FORCESUB_CHANNEL_LINK", default="", cast=str)

    # Dev Configs

    DEV_MODE = config("DEV_MODE", default=False, cast=bool)
