import glob
import json
import subprocess
import os
import jsonpickle
import shutil

from lib.bot import Bot
from lib.operation import Operation

import constants as LC
import variables as LV


# Name: init
# Description: Check if BlackZinc directory exist.
#              If it does not create it. And create
#              the database.
# Return: (void)
def init():
    # Check BlackZinc directory existence.
    for path in [LC.BLACKZINC_PATH, LC.SOCKETS_PATH]:
        dir_exist = os.path.exists(path)
        if not dir_exist:
            os.makedirs(path)
            print(f"[*] Directory created: {path}")
    path = LC.DATABASE
    file_exist = os.path.exists(path)
    if not file_exist:
        with open(path, "w") as f:
            f.write("\"{}\"")

# Name: load_operations
# Description: Load from a JSON file all the
#              running operations.
# Return: (void)
def load_operations():
    # Opening JSON database.
    with open(LC.DATABASE, "r") as f:
        # Loading JSON to variable OPERATIONS.
        operations_encoded = jsonpickle.decode(f.read())
        LV.OPERATIONS = json.loads(operations_encoded)

# Name: save_operations
# Description: Save to a JSON file all the
#              running operations.
# Return: (void)
def save_operations():
    operations_encoded = jsonpickle.encode(LV.OPERATIONS, unpicklable=True)
    with open(LC.DATABASE, "w") as f:
     f.write(json.dumps(operations_encoded, indent=4))

# Name: list_operations
# Description: Pretty print running operations.
# Return: (void)
def list_operations():
    print(f"Operations ({len(LV.OPERATIONS)}):")
    for key, value in LV.OPERATIONS.items():
        print(f"    - {key}: {value['comment']}")

# Name: operation_details
# Description: Get details about an operation.
# Return: (void)
def operation_details(operation_number):
    operation_number = str(operation_number)
    if operation_number in list(LV.OPERATIONS.keys()):
        print(f"Operation: {operation_number}")
        print(json.dumps(LV.OPERATIONS[operation_number], sort_keys=True, indent=4))
    else:
        print(f"[x] Operation does not exists.")

# Name: add_operation
# Description: Add an operation from the database.
# Return: (void)
def add_operation():
    comments = input("Enter comments on the operation (examples: sploit used, targets, etc.):\n> ")
    new_operation = Operation(comments)
    LV.OPERATIONS.update({new_operation.number: new_operation})
    print(f"[*] Operation added.")

# Name: remove_operation
# Description: Remove an operation from the database.
# Return: (void)
def remove_operations(operations_number):
    operations_number = operations_number.split(",")
    for operation_number in operations_number:
        if operation_number in LV.OPERATIONS:
            shutil.rmtree(LV.OPERATIONS[operation_number]["path"])
            del LV.OPERATIONS[operation_number]
            print(f"[*] Operation {operation_number} deleted.")
        else:
            print(f"[x] Operation {operation_number} does not exists.")

# Name: add_bot
# Description: Add a bot to an operation.
# Return: (void)
def add_bot(operation_number):
    operation_number = str(operation_number)
    if operation_number in LV.OPERATIONS:
        new_bot = Bot(operation_number)
        LV.OPERATIONS[operation_number]["bots"].append(new_bot)
        print(f"[+][Operation:{operation_number}] Bot {new_bot.number} added.")
    else:
        print(f"[x] Operation {operation_number} does not exists.")

# Name: remove_bot
# Description: Remove a bot from an operation.
# Return: (void)
def remove_bots(operation_number, bots_number):
    bots_number = bots_number.split(",")
    operation_number = str(operation_number)
    operation_bots = []
    for bot_number in bots_number:
        condition = 0
        for data in LV.OPERATIONS[operation_number]["bots"]:
            if bot_number == str(data["number"]):
                condition = 1
                try:
                    shutil.rmtree(data['path'])
                    print(f"[*][Operation:{operation_number}] Bot {bot_number} deleted.")
                except:
                    pass
            else:
                operation_bots.append(data)
        if not condition:
            print(f"[x][Operation:{operation_number}] Bot {bot_number} does not exists.")
    LV.OPERATIONS[operation_number]["bots"] = operation_bots

# Name: execute
# Description: Execute a command on one or multiple bots.
# Return: (void)
def execute(operation_number, bots_number, command):
    bots_number = bots_number.split(",")
    operation_number = str(operation_number)
    for bot_number in bots_number:
        condition = 0
        for data in LV.OPERATIONS[operation_number]["bots"]:
            if bot_number == str(data["number"]):
                condition = 1
                try:
                    p = subprocess.Popen(["ssh", "-S", data['master_socket'], data['target'], command], stdout=subprocess.PIPE)
                    out, err = p.communicate()
                    print(f"[+][Operation:{operation_number}|bot:{bot_number}] => {out}")
                except:
                    pass
        if not condition:
            print(f"[x][Operation:{operation_number}] Bot {bot_number} does not exists.")
