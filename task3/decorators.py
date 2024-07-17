from typing import Callable

#decorator for error handling during parsing logs
def parse_error_handler(func: Callable):
    def inner(line: str, log_type: str):
        try:
            return func(line, log_type)
        except:
            print(f"Error parsing line: {line}") 
    return inner