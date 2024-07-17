from logsservice import filter_logs_by_level
from constants import log_types

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for log_type in log_types:
        spaces = get_spaces(log_type)
        print(f"{log_type}{spaces}| {counts[log_type]}")

def get_spaces(level: str):
    return " " * (17 - len(level))

def display_level_details(logs, client_log_level):
    logs_by_level = filter_logs_by_level(logs, client_log_level)
    if len(logs_by_level) > 0:
        print(f"Деталі логів для рівня '{client_log_level}':")
        for log in logs_by_level:
            date = log['datetime']
            message = log['message']
            print(f"{date} - {message}")
