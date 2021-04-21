import pyrebase
import os



class FirebaseDB():

    def __init__(self):
        self.configuration = {}
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