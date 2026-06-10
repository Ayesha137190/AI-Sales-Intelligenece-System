import schedule
import time
from models.retrain import retrain

schedule.every().day.at(
    "01:00"
).do(retrain)

while True:

    schedule.run_pending()

    time.sleep(60)