# decorators.py
import os
import pandas as pd
from datetime import datetime
import uuid
from functools import wraps

def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        log_id = str(uuid.uuid4())
        username = os.getlogin()
        function_name = func.__name__
        current_time = datetime.now()
        date_str = current_time.strftime("%d.%m.%Y")
        time_str = current_time.strftime("%H:%M:%S")

        new_entry = pd.DataFrame({
            "id": [log_id],
            "pc username": [username],
            "function name": [function_name],
            'Date in "date.month.year"': [date_str],
            "Time": [time_str]
        })

        try:
            existing_log = pd.read_csv("logs.csv")
            updated_log = pd.concat([existing_log, new_entry], ignore_index=True)
        except FileNotFoundError:
            updated_log = new_entry

        updated_log.to_csv("logs.csv", index=False)
        return func(*args, **kwargs)
    return wrapper