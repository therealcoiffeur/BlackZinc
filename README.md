# BlackZinc

## Description

BlackZinc is a tool for the explorer of the vast world that is Internet. It allows to manage with a python script working in CLI, several SSH sessions. If I talk about SSH sessions, it's because BlackZinc makes it easier to manage implants (connections to multiple SSH server or reverse SSH server) from a single terminal.

## Usage

```
usage: blackzinc.py [-h] [--list-operations] [--add-operation]
                    [--remove-operation REMOVE_OPERATION] [--operation-details OPERATION_DETAILS]
                    [--add-bot ADD_BOT] [--operation OPERATION] [--remove-bots REMOVE_BOTS]
                    [--bots BOTS] [--command COMMAND]

BlackZinc C2 client.

optional arguments:
  -h, --help            show this help message and exit
  --list-operations     List operation stored in the database.
  --add-operation       Add new operation to the database.
  --remove-operation REMOVE_OPERATION
                        Remove an operation from the database.
  --operation-details OPERATION_DETAILS
                        Get details about a specific operation.
  --add-bot ADD_BOT     Add a bot to an operation.
  --operation OPERATION
                        Specify operation on which to apply actions.
  --remove-bots REMOVE_BOTS
                        Remove a bot from an operation.
  --bots BOTS           Specify bots on which to apply actions.
  --command COMMAND     Command to execute on bots.
```

## Examples

### List operations

```
$ python3 blackzinc.py --list-operations
Operations (0):
```

### Add an operation then list operations again

```
$ python3 blackzinc.py --add-operation
Enter comments on the operation (examples: sploit used, targets, etc.):
> Test
[*] New operation number generated: 651
[*] New directory created: /tmp/black_zinc/sockets/651/
[*] Operation added.
```

```
$ python3 blackzinc.py --list-operations
Operations (1):
    - 651: Test
```

### Get the details about an operation

```
$ python3 blackzinc.py --operation-details 651
Operation: 651
{
    "bots": [],
    "comment": "Test",
    "number": 651,
    "path": "/tmp/black_zinc/sockets/651/"
}
```

### Add a bot to an operation and get details about the operation

```
$ python3 blackzinc.py --add-bot 651
[*] New bot number generated: 430
Enter target (example: root@localhost, localhost, etc.):
> user@X.X.X.X
[*] Target added to bot.
[+][Operation:651] Bot 430 added.
```

```
Operation: 651
{
    "bots": [
        {
            "master_socket": "/tmp/black_zinc/sockets/651/430/ssh.sock",
            "number": 430,
            "path": "/tmp/black_zinc/sockets/651/430/",
            "py/object": "lib.bot.Bot",
            "target": "user@X.X.X.X"
        }
    ],
    "comment": "Test",
    "number": 651,
    "path": "/tmp/black_zinc/sockets/651/"
}
```

### Execute commands on one or multiple bots

```
$ python3 blackzinc.py --operation 651 --bots 430 --command "uname -a"
[+][Operation:651|bot:430] => b'Linux XXXX 5.4.0-90-generic XXX-Ubuntu XXX XXX XXX XX XX:XX:XX XXX XXXX x86_64 x86_64 x86_64 GNU/Linux\n'
```

Information: It is possible to run the same command on several bots by separating them (the bots) with commas. 

Example:

```
$ python3 blackzinc.py --operation 651 --bots 430,1032,15 --command "uname -a"
```



### Remove a bot from an operation

```
$ python3 blackzinc.py --remove-bot 430 --operation 651
[*][Operation:651] Bot 430 deleted.
```

### Remove an operation

```
$ python3 blackzinc.py --remove-operations 651
[*] Operation 651 deleted.
```

Information: deleting an operation deletes all its bots