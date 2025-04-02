import getpass
from datetime import date, datetime
import pandas as pd
import os


def log(func):
    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)
        
        user_name = getpass.getuser()
        func_name = func.__name__
        formatted_date = date.today().strftime("%d-%m-%Y")
        formatted_time = datetime.now().time()

        if os.path.isfile("logs.csv"):
            print("Файл существует")
            file_df = pd.read_csv("logs.csv")
            df = pd.DataFrame([len(file_df),user_name, func_name,formatted_date, formatted_time],
            columns=['id','user_name', 'func_name', 'formatted_date', 'data_time'])
            df.to_csv('logs.csv', mode='a', index=False)

        else:
            print("Файл не существует")
            df = pd.DataFrame([0 ,user_name, func_name,formatted_date, formatted_time],
            columns=['id','user_name', 'func_name', 'formatted_date', 'data_time'])
            df.to_csv('logs.csv')


        return original_result
    return wrapper