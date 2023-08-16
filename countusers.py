import sched, time, subprocess, json
from datetime import datetime
s = sched.scheduler(time.time, time.sleep)

print('Starting')
def countUsers(sc): 
    print("Counting users")
    
    users = subprocess.run(['who|cut -f 1 -d " "|sort -u | wc -l'], capture_output=True, shell=True)
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    data = {}
    data['datatime'] = dt_string
    data['count'] = str(users.stdout, encoding='utf-8').strip()
    json_data = json.dumps(data)
    print(json_data)

    sc.enter(60, 1, countUsers, (sc,))
    
s.enter(60, 1, countUsers, (s,))
s.run()
