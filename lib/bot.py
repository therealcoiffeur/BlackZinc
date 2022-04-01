import random
import os

import constants as LC
import variables as LV

from utils import *


class Bot:
    # Bot number (int).
    number = None
    # Path to directory containing the socket related to bot (string).
    path = None
    # Path to the unix socket to handle the SSH session.
    master_socket = None
    # Target (example: roo@localhost).
    target = None

    def __init__(self, operation_number):
        # Creating a bot number which do not exists.
        number = random.randint(1, LC.MAX_BOT_NUMBER)
        while number in list(LV.OPERATIONS[operation_number].keys()):
            number = random.randint(0, LC.MAX_BOT_NUMBER)
        self.number = number
        print(f"[*] New bot number generated: {self.number}")

        self.path = f"{LV.OPERATIONS[operation_number]['path']}{self.number}/"
        # Check whether the specified path exists or not.
        file_exist = os.path.exists(self.path)
        if not file_exist:
            os.makedirs(self.path)
        self.master_socket = f"{self.path}ssh.sock"
        self.target = input("Enter target (example: root@localhost, localhost, etc.):\n> ")
        print(f"[*] Target added to bot.")