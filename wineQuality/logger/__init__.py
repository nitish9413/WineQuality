import imp
import logging
from datetime import datetime
import os
import pandas as pd
from wineQuality.constant import get_current_time_stamp

LOG_DIR = "logs"

def get_log_file_name():
    return f"log_{get_current_time_stamp()}.log"

LOG_FILE_NAME = get_log_file_name()

os.makedirs(LOG_DIR,exist_ok=True)

LOG_FILE_PATH =os.paht.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH,
filemode="w",
format='[%(asctime)s]^;%(levelname)s^;%(lineno)d^;%(filename)s^;%(funcName)s()^;%(message)s',
level=logging.INFO
)

def get_log_dataframe(filepath):
    data=[]
    with open(filepath) as log_file:
        for line in log_file.readlines():
            data.append(line.split("^;"))

        log_df = pd.DataFrame(data)
        columns = ["Time stamp","Log Level","line number","file name","function name","message"]
        log_df.columns = columns
        log_df['log_message'] = log_df['Time stamp'].astype(Str) + ":$" + log_df["message"]

        return log_df[['log_message']]