from driver.StackController import StackController
from driver.Transition import Transition
import time
import requests
from datetime import datetime
import json
import pandas as pd
INTERVAL_SECS = 60 * 5  # 5 minutes
URL = 'http://itame.pythonanywhere.com/CairnFORM/getEnergyUsageFromTo/'
HOUR_LT = 8
HOUR_GT = 17
TRANSITION_MODE = 'EASE_IN_OUT_QUINT'
DELAY = 0
DURATION = 7
DEBUG = True


class CairnFORM:

    def __init__(self):
        self.stack = StackController()

    def run(self):
        while True:
            startTime = datetime.now().replace(hour=HOUR_LT, minute=0, second=0)
            endTime = startTime.replace(hour=HOUR_GT, minute=0, second=0)
            try:
                r = requests.get(
                    URL + str(startTime.year) + '/' + str(startTime.month) + '/' + str(
                        startTime.day) + '/' + str(startTime.hour) + '/' + str(startTime.minute) + '/' + str(startTime.second)
                    + '/' + str(endTime.year) + '/' + str(endTime.month) + '/' + str(endTime.day) + '/' + str(endTime.hour) + '/' + str(endTime.minute) + '/' + str(endTime.second))
                rawJson = json.loads(r.content)
                ans = [item['fields'] for item in rawJson]
                for i in range(len(ans)):
                    ans[i]['timestamp'] = rawJson[i]['pk']
                df = pd.DataFrame.from_dict(ans).sort_values(by=['timestamp'])
                for index, row in df.iterrows():
                    if index >= self.stack.size():
                        break
                    # instruction format: [address<0:STACK_SIZE>, R<0:255>, G<0:255>, B<0:255>, POSITION<0:200>, DELAY<0:Inf>, DURATIONDELAY<0:Inf>, TRANSITION<String>])
                    self.stack.push([index, int(round(255*row.production*row.consumption)), int(round(255*row.production)),
                                     int(round(255*row.production*row.consumption)), int(round(200*row.production)), DELAY, DURATION, 'EASE_IN_OUT_QUINT'])
            except Exception as e:
                print('An error occured:', e) if DEBUG else 0
            time.sleep(INTERVAL_SECS)

CairnFORM().run()
