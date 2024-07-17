from constants import Messages, Commands
from handlers import handle
from parser import parse_input
from validators import validate_input

def main():
    print(Messages.Wellcome)
    while True:
        command, *args = parse_input(input(Messages.EnterACommand))
        if command == Commands.CLOSE or command == Commands.EXIT:
            print(Messages.GoodBye)
            break
        print(handle(command, args))

if __name__ == "__main__":
    main()