"""Command line utilities
"""


class Command:
    """Represents a command
    """
    command: str
    pre_condition: bool = True
    actions: list

    def __init__(self, command: str, actions: list, pre_condition: bool = True) -> None:
        self.command = command
        self.actions = actions
        self.pre_condition = pre_condition


def interpret_command(command: str, command_list: list, argument_list: list):
    """Interpret a command

    :param command: Command to execute
    :type command: str
    :param command_list: Available commands list
    :type command_list: list
    :param argument_list: Arguments to command
    :type argument_list: list
    """
    for com in command_list:
        if com.command == command:
            if com.pre_condition:
                for action in com.actions:
                    action(argument_list)
