import pymongo
import schedule
import time

myclient = pymongo.MongoClient("mongodb://database-username:database-password@mongo:27017", minPoolSize=50,
                               uuidRepresentation="standard")
mydb = myclient["Database"]
mycol = mydb["Timestamps"]


def persist_time():
    print(f" Triggerd function to save data")
    payload = {"time": f"{str(time.strftime('%H:%M:%S', time.localtime()))}"}
    mycol.insert_one(payload)


schedule.every(10).seconds.do(persist_time)
