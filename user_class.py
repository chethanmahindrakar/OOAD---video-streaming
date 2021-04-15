# OOAD PROJECT
# USER CLASS

import json
import video_class
import video_database_class
import user_database_class

class User:
    def __init__(self,ID=0,firstName='',lastName='',age='',phoneNo='',email='',password=''):
        self.firstName = firstName
        self.lastName = lastName 
        self.age = age
        self.phoneNo = phoneNo
        self.email = email
        self.password = password
        self.ID = ID

    def login(self):
        with open(r"database/user.ndjson") as rp:
            for line in rp:
                line = json.loads(line)
                
                user_email = line['email']
                user_password = line['password']
                user_id = line['ID']

                if(self.email == user_email):
                    #check if password matches
                    if(self.password == user_password):
                        self.ID = user_id
                        self.firstName=line['firstName']
                        self.lastName=line['lastName']
                        return True

        return False

    def signUp(self):
        user_db = user_database_class.UserDatabase()
        ans=user_db.create_record(self)

        return ans


        # method to UPLOAD VIDEO
    def upload_video(self,title,description,url):
        video = video_class.Video(title=title,description=description,user_ID=self.ID,url=url)

        video_db = video_database_class.VideoDatabase()

        ans = video_db.create_record(video)

        return ans

        




                



        



        


        

        


