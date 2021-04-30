import pyrebase
import os
from dotenv import load_dotenv

load_dotenv()


class FirebaseDB():

    def __init__(self):
        self.configuration = {
            "apiKey" : os.getenv("APIKEY"),
            "authDomain" : os.getenv("AUTHDOMAIN"),
            "databaseURL": os.getenv("DATABASEURL"),
            "projectId" : os.getenv("PROJECTID"),
            "storageBUcket" : os.getenv("STORAGEBUCKET")
        }
        self.initialize()

    def initialize(self):

        try:
            self.firebase = pyrebase.initialize_app(self.configuration)
            self.database = self.firebase.database()
        except Exception as e:
            print(str(e))
            return False

if __name__ == '__main__':
    obj = FirebaseDB()