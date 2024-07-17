from typing import Callable

from constants import Messages
#decorator for returning message depending of error type
# I supposed that it is correct to send message of error inside the error, 
# but there is an option for decorator to return custom error message
def input_error(func: Callable):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as err:
            return err.args[0] if len(err.args) > 0 else Messages.GiveNameAndPhone
        except KeyError as err:
            return err.args[0] if len(err.args) > 0 else Messages.InvalidCommand
        except IndexError as err:
            return err.args[0] if len(err.args) > 0 else Messages.EnterUserName
        except Exception as err: 
            if len(err.args) > 0:
                 return "Error: {err.__name__}. Message: {err.args[0]}" 
            else: "Error: {err.__name__}"
    return inner