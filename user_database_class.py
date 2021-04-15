# OOAD PROJECT

import json
import shutil
import os
import video_class

class UserDatabase:
    def __init__(self):
        self.database_path = "database/user.ndjson"

    def create_record(self, user):
        latest_id = 0

        with open(self.database_path,'r') as rp:
            for line in rp:
                line = json.loads(line)
                
                user_ID = line['ID']
                email_ID = line['email']

                # check if email already exists
                if(email_ID == user.email):
                    return False

                latest_id = user_ID
        
        user.ID = latest_id+1


        # create an entry in User Database
        database=open(self.database_path,'a')

        entry ={"ID":user.ID, "email":user.email,"password":user.password, "firstName":user.firstName, "lastName":user.lastName,"age":user.age,"phoneNo":user.phoneNo}
        database.write(json.dumps(entry))
        database.write("\n")
        database.close()

        return True



    def search_for_user(self,user_id):
        with open(self.database_path,'r') as rp:
            for line in rp:
                line = json.loads(line)
                
                id = line['ID']

                # check if title exists
                if(user_id == id):
                    return line['firstName'] + " " + line['lastName']
                  
        return False

    
    
                

        


