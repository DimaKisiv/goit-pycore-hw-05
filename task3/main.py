
from pathlib import Path
from args import  get_log_type_arg
from displayservice import display_level_details, display_log_counts
from logsservice import count_logs_by_level, load_logs

def main():
    logs = load_logs()
    if not logs: return
    client_log_level = get_log_type_arg()
    log_levels_counts = count_logs_by_level(logs)
    display_log_counts(log_levels_counts)
    display_level_details(logs, client_log_level)

if __name__ == "__main__":
    main()