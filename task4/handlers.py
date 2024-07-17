from constants import Messages, Commands
import repository
from decorators import input_error
from validators import validate_input

@input_error 
def handle(command, args):
    validate_input(command, args)
    match command:
        case Commands.HELLO:
            return Messages.HowCanIHelpYou
        case Commands.ADD:
            return add_contact(args)
        case Commands.CHANGE:
            return change_contact(args)
        case Commands.DELETE:
            return delete_contact(args)
        case Commands.PHONE:
            return show_phone(args)
        case Commands.ALL:
            return show_all()

def add_contact(args):
    name, phone = args
    if name in repository.contacts:
        return Messages.ContactAlreadyExists
    repository.contacts[name] = phone
    return Messages.ContactAdded

def change_contact(args):
    name, phone = args
    if name not in repository.contacts:
        return Messages.ContactDoesNotExist
    repository.contacts[name] = phone
    return Messages.ContactChanged

def show_phone(args):
    name = args[0]
    if name not in repository.contacts:
        raise KeyError(Messages.ContactDoesNotExist) #throwing error with message here
    return repository.contacts[name]

def delete_contact(args):
    name = args[0]
    if name not in repository.contacts:
        return Messages.ContactDoesNotExist
    repository.contacts.pop(name)
    return Messages.ContactDeleted

def show_all():
    return repository.contacts