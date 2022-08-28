import pymongo
from bson import ObjectId
from datetime import datetime
from datetime import timedelta


class Base():
    def __init__(self,classterMongo):
        self.classterMongo = classterMongo
        self.classter = pymongo.MongoClient(self.classterMongo)


    def regAddress(self,adress):
        db = self.classter["Scan"]
        Adress = db["Adress"]

        if Adress.find_one({"adress":adress}) is None:
            post = {"adress":adress,
                    "privat_kay":'',
                    'balance':0
                    }
            Adress.insert_one(post)

    def setPrivatKayNBalance(self,adress,privat_kay,balance):
        db = self.classter["Scan"]
        User = db["Adress"]
        User.update_one({"adress":adress},{"$set":{"privat_kay":privat_kay,'balance':balance}})


    def getAddress(self,adress):
        db = self.classter["Scan"]
        User = db["Adress"]

        return User.find_one({"adress":adress})