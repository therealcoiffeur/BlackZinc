import random
import os

import constants as LC
import variables as LV

from utils import *


class Operation:
    # Operation number (int).
    number = None
    # Path to directory containing sockets
    # related to operation (string).
    path = None
    # Comments on the operations (string).
    comments = None

    def __init__(self, comment):
        self.comment = comment
        # Creating an operation number which do not exists.
        number = random.randint(1, LC.MAX_OPERATION_NUMBER)
        while number in list(LV.OPERATIONS.keys()):
            number = random.randint(0, LC.MAX_OPERATION_NUMBER)
        self.number = number
        print(f"[*] New operation number generated: {self.number}")

        self.path = f"{LC.SOCKETS_PATH}{self.number}/"
        # Check whether the specified path exists or not.
        dir_exist = os.path.exists(self.path)
        if not dir_exist:
            # Create a new directory because it does not exist.
            os.makedirs(self.path)
            print(f"[*] New directory created: {self.path}")
        
        # Array of bot (array).
        self.bots = []