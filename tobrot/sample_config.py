import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1478165891:AAHjNBWosfJa-8El1ILJd2-9PyHaxzw_MpM")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 1667813))
    API_HASH = os.environ.get("API_HASH", "1f6921c27bf6cd01aba471a14ff33bcb")
    OWNER_ID = int(os.environ.get("OWNER_ID", 1326703864))
    # Get these values from my.telegram.org
    # to store the channel ID who are authorized to use the bot
    AUTH_CHANNEL = set(int(x) for x in os.environ.get("AUTH_CHANNEL", "-1001491078689").split())
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://telegra.ph/file/cf483ebb111e65b69d965.jpg")
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    #
    ARIA_TWO_STARTED_PORT = int(os.environ.get("ARIA_TWO_STARTED_PORT", 6800))
    EDIT_SLEEP_TIME_OUT = int(os.environ.get("EDIT_SLEEP_TIME_OUT", 1))
    MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START = int(os.environ.get("MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START", 600))
    MAX_TG_SPLIT_FILE_SIZE = int(os.environ.get("MAX_TG_SPLIT_FILE_SIZE", 2097152000))
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = os.environ.get("FINISHED_PROGRESS_STR", "✪ ")
    UN_FINISHED_PROGRESS_STR = os.environ.get("UN_FINISHED_PROGRESS_STR", "")
    # add offensive API
    TG_OFFENSIVE_API = os.environ.get("TG_OFFENSIVE_API", None)
    CUSTOM_FILE_NAME = os.environ.get("CUSTOM_FILE_NAME", "")
    LEECH_COMMAND = os.environ.get("LEECH_COMMAND", "getfile@AiTorrentWare_Bot")
    YTDL_COMMAND = os.environ.get("YTDL_COMMAND", "utube@AiTorrentWare_Bot")
    RCLONE_CONFIG = os.environ.get("RCLONE_CONFIG", "")
    DESTINATION_FOLDER = os.environ.get("DESTINATION_FOLDER", "New AiTorrentWare")
    GLEECH_COMMAND = os.environ.get("GLEECH_COMMAND", "loadlink@AiTorrentWare_Bot")
    INDEX_LINK = os.environ.get("INDEX_LINK", "https://bot.aitorrentware.workers.dev/New%20AiTorrentWare")
    TELEGRAM_LEECH_COMMAND_G = os.environ.get("TELEGRAM_LEECH_COMMAND_G", "loadfile@AiTorrentWare_Bot")
    CANCEL_COMMAND_G = os.environ.get("CANCEL_COMMAND_G", "cancel")
    GET_SIZE_G = os.environ.get("GET_SIZE_G", "getsize@AiTorrentWare_Bot")
    STATUS_COMMAND = os.environ.get("STATUS_COMMAND", "status@AiTorrentWare_Bot")
    SAVE_THUMBNAIL = os.environ.get("SAVE_THUMBNAIL", "setpic@AiTorrentWare_Bot")
    CLEAR_THUMBNAIL = os.environ.get("CLEAR_THUMBNAIL", "clearpic@AiTorrentWare_Bot")
    UPLOAD_AS_DOC = os.environ.get("UPLOAD_AS_DOC", "True")
    PYTDL_COMMAND_G = os.environ.get("PYTDL_COMMAND_G", "utubelist@AiTorrentWare_Bot")
    LOG_COMMAND = os.environ.get("LOG_COMMAND", "log@AiTorrentWare_Bot")
    CLONE_COMMAND_G = os.environ.get("CLONE_COMMAND_G", "getclone@AiTorrentWare_Bot")
