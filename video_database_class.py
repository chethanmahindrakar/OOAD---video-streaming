# OOAD PROJECT

import json
import shutil
import os
import video_class
from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove


class VideoDatabase:
    def __init__(self):
        self.database_path = "database/video.ndjson"

    def create_record(self, video):
        latest_id = 0

        with open(self.database_path,'r') as rp:
            for line in rp:
                line = json.loads(line)
                
                video_ID = line['ID']
                curr_title = line['title']

                # check if title already exists
                if(curr_title.lower() == video.title.lower()):
                    return False

                latest_id = video_ID

        video.ID = latest_id+1

        # copy the video to /videos dir
        #db_video_path=os.getcwd()+"\\"+'videos'+'\\'+ str(video.ID) + '.mp4'
        db_video_path='videos'+'\\'+ str(video.ID) + '.mp4'
        shutil.copyfile(video.url, db_video_path)

        video.url = db_video_path

        # create an entry in Video Database
        database=open(self.database_path,'a')

        entry ={"ID":video.ID, "user_ID":video.user_id,"title":video.title, "description":video.description, "url":video.url,"likes":video.likes,"comments":video.comments}
        database.write(json.dumps(entry))
        database.write("\n")
        database.close()

        return True


    def search_for_video(self,title):
        with open(self.database_path,'r') as rp:
            for line in rp:
                line = json.loads(line)
                
                curr_title = line['title']

                # check if title exists
                if(curr_title.lower() == title.lower()):
                    video = video_class.Video(title=line['title'],description=line['description'],user_ID=line['user_ID'],url=line['url'])
                    video.likes=line['likes']
                    video.comments=line['comments']
                    video.ID=line['ID']

                    return video
            
        return False


    def update_likes_record(self,video_id,user_id):
        fh, abs_path = mkstemp()
        with fdopen(fh,'w') as new_file:
            with open(self.database_path) as old_file:
                for line in old_file:

                    line = json.loads(line)
                    
                    curr_id = line['ID']

                    if(curr_id==video_id):
                        line['likes'].append(user_id)
                        line['likes']=list(set(line['likes']))
                        new_file.write(json.dumps(line))
                        new_file.write("\n")

                    else:
                        new_file.write(json.dumps(line))
                        new_file.write("\n")

        #Copy the file permissions from the old file to the new file
        copymode(self.database_path, abs_path)
        #Remove original file
        remove(self.database_path)
        #Move new file
        move(abs_path, self.database_path) 




    def update_comments_record(self,video_id,user_id,comment):
        fh, abs_path = mkstemp()
        with fdopen(fh,'w') as new_file:
            with open(self.database_path) as old_file:
                for line in old_file:
                    


                    line = json.loads(line)
                    
                    curr_id = line['ID']
                    

                    if(curr_id==video_id):
                        if(str(user_id) not in line['comments'].keys()):
                            line['comments'][str(user_id)]=[]

                        line['comments'][str(user_id)].append(comment)
                        
                        line['comments'][str(user_id)]=list(set(line['comments'][str(user_id)]))

                        #print(line['comments'][user_id])

                        


                        new_file.write(json.dumps(line))
                        new_file.write("\n")

                    else:
                        new_file.write(json.dumps(line))
                        new_file.write("\n")

        #Copy the file permissions from the old file to the new file
        copymode(self.database_path, abs_path)
        #Remove original file
        remove(self.database_path)
        #Move new file
        move(abs_path,self.database_path) 


            
        

        

    