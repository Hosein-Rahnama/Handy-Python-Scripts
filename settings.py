import os

# path variables
CWD = os.getcwd()
DOWNLOAD_PATH = os.path.join(CWD, 'download')

# download request setting
MAX_RETRIES = 3

# numbering format
DIGITS = 2

# unit conversion
BYTE_TO_MB = 1 / (1024 * 1024)