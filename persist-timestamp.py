import pymongo
import schedule
import time

myclient = pymongo.MongoClient("mongodb://database-username:database-password@mongodb-service:27017/admin")
mydb = myclient["database"]
mycol = mydb["Timestamps"]

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger

scheduler = BlockingScheduler(timezone="Europe/Berlin")
@scheduler.scheduled_job(IntervalTrigger(seconds=10))
def persist_time():
    print(f" Triggerd function to save data")
    payload = {"time": f"{str(time.strftime('%H:%M:%S', time.localtime()))}"}
    mycol.insert_one(payload)



scheduler.start()
