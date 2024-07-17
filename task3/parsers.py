from datetime import datetime
from constants import log_types
from decorators import parse_error_handler

def parse_logs(log_lines) -> list[dict]:
    return [log_dict for log_dict in list(map(parse_log_line, log_lines)) if log_dict]

#parse logs by creating separate dict objects depending on log type
def parse_log_line(line: str) -> dict:
    for log_type in log_types:
        if log_type in line: 
            return parse_log_line_by_type(line, log_type)

@parse_error_handler
def parse_log_line_by_type(line, log_type) -> dict:
    datetime_str, error_message = line.split(log_type, 1)
    log_datetime = datetime.strptime(datetime_str.strip(), '%Y-%m-%d %H:%M:%S')
    message = error_message.strip()  
    log_dict: dict = {
        "datetime": log_datetime,
        "log_type": log_type,
        "message": message
    }
    return log_dict