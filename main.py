import time
from datetime import datetime

# 9 утра, 18 вечера
start_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 9)
finish_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 18)
print(start_time)
print(finish_time)

# C:\Windows\System32\drivers\etc\hosts - файл с адресами сайтов и именами

# hosts = r'C:\Windows\System32\drivers\etc\hosts'
hosts = 'hosts.txt'
redirect_url = '127.0.0.1'

blocked_sites = ['www.youtube.com', 'youtube.com', 'www.linkedin.com', 'linkedin.com']

while True:
    if start_time < datetime.now() < finish_time:
        print(f'Access is failed! between {start_time}-{finish_time}!')

        with open(hosts, 'r+') as f:
            src = f.read()

            for site in blocked_sites:
                if site in src:
                    pass
                else:
                    f.write(f'{redirect_url} {site}\n')
    else:
        with open(hosts, 'r+') as f:
            src = f.readlines()
            f.seek(0)

            for line in src:
                if not any(site in line for site in blocked_sites):
                    f.write(line)
            f.truncate()
        print('Access is success!')
        time.sleep(3)
