import sys

def get_logs_filepath_arg() -> str:
    if(len(sys.argv)) > 1:
        return sys.argv[1]
    else:
        print("Please provide file path")
        return None
    
def get_log_type_arg() -> str:
    if(len(sys.argv)) > 2:
        return sys.argv[2]