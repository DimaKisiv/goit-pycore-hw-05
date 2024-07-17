from pathlib import Path
from args import get_logs_filepath_arg
from parsers import parse_logs
from constants import log_types

def load_logs() -> list[dict]:
    file = Path(get_logs_filepath_arg())
    if not file.exists():
       print("File does not exist")
       return []
    return parse_logs(file.read_text("utf-8").splitlines())

def count_logs_by_level(logs: list) -> dict:
    logs_by_level = {}
    for log_type in log_types:
        logs_by_level[log_type] = len(filter_logs_by_level(logs, log_type))
    return logs_by_level

def filter_logs_by_level(logs: list[dict], level: str) -> list:
    return [log for log in logs if log["log_type"] == level]