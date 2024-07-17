from constants import Commands, Messages

def validate_input(command, args):
    if command not in vars(Commands).values():
        raise KeyError #with no message inside of error
    if command in [Commands.ALL, Commands.HELLO] and len(args) != 0:
        return Messages.WrongParameters
    elif command == Commands.PHONE and len(args) != 1:
        raise IndexError(Messages.EnterUserName) #with message inside of error
    elif command in [Commands.ADD, Commands.CHANGE] and len(args) != 2:
        raise ValueError(Messages.GiveNameAndPhone) #with no message inside of error
    return None