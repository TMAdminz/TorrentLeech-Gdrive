from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
    TG_BOT_TOKEN= "1035693074:AAENK8UARvnap7sEKSqiuxZj2IfvhZfLIMo"
    APP_ID = 1667813
    API_HASH = "1f6921c27bf6cd01aba471a14ff33bcb"
    OWNER_ID = 1054316613
    AUTH_CHANNEL = [-1001186041542]
    DESTINATION_FOLDER = "HelloMan" #Name of your folder read readme
    RCLONE_CONFIG = """type = drive\scope = drive\root_folder_id = 0AAiPaAkudSLFUk9PVA\token = {"access_token":"ya29.a0AfH6SMCXk33x_4dwg8gWhT2AqiUQNVucUCOCA5hDQaevipIIfmEaPFPqLYFErdQQRtZdAEaFRfrhjlMO40OvlnOR-xlnU8khDDMJqiAV1EXQUXIUxRGjYUUVlNNpO2GCkVMhK4qTDWfSdvUJQ6iYPTXcUR56ePaY9_I","token_type":"Bearer","refresh_token":"1//0gyg8GQAeAoVNCgYIARAAGBASNwF-L9IrtQrswMe13q7Xy9MJnqFP7H9yOXrkj8dUXkRcLnLgqbd5R5qYdrRa5u_F74ICyBKDKfg","expiry":"2020-07-19T02:00:43.0228054+05:30"}\team_drive = 0AAiPaAkudSLFUk9PVA"""
    #fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = 128
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = "https://telegra.ph/file/170504c96e2fa1ebbc708.jpg"
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    #
    ARIA_TWO_STARTED_PORT = 6800
    EDIT_SLEEP_TIME_OUT = 1
    MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START = 600
    MAX_TG_SPLIT_FILE_SIZE = 2097152000
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = "█"
    UN_FINISHED_PROGRESS_STR = "░"
    # add offensive API
    TG_OFFENSIVE_API = None
    CUSTOM_FILE_NAME = "TM "
    LEECH_COMMAND = "leech@TM_PrivateBot"
    YTDL_COMMAND = "ytdl@TM_PrivateBot"
    GLEECH_COMMAND = "gleech@TM_PrivateBot"
    TELEGRAM_LEECH_COMMAND_G = "tleech@TM_PrivateBot"
    CANCEL_COMMAND_G = "cancel@TM_PrivateBot"
    GET_SIZE_G = "getsize@TM_PrivateBot"
    STATUS_COMMAND = "status@TM_PrivateBot"
    SAVE_THUMBNAIL = "savethumb@TM_PrivateBot"
    CLEAR_THUMBNAIL = "clearthumb@TM_PrivateBot"
    UPLOAD_AS_DOC = "True"
    PYTDL_COMMAND_G = "pytdl@TM_PrivateBot"
    LOG_COMMAND = "log@TM_PrivateBot"
    CLONE_COMMAND_G = "gclone@TM_PrivateBot"
