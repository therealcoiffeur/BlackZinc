# Use tool in debug mode.
DEBUG = False

# BackZinc path.
BLACKZINC_PATH = "/tmp/black_zinc/"

# Path of the database storing informations.
# Need to be moved to a tmpFS in production
# environment.
DATABASE = f"{BLACKZINC_PATH}db.json"

# Path containing sockets to SSH sessions.
SOCKETS_PATH = f"{BLACKZINC_PATH}sockets/"

# Max number of operations in concurrency.
MAX_OPERATION_NUMBER = 1337

# Max number of bots per operation.
MAX_BOT_NUMBER = 1337
