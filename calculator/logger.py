from datetime import datetime as dt
from time import time

def sum_logger(data):
    time = dt.now().strftime('%D %H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}; sum; {}\n'
                    .format(time, data))

