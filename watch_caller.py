import user_database_class
import video_database_class

def find_channel(user_id):
    user_db = user_database_class.UserDatabase()
    
    channel = user_db.search_for_user(user_id)

    return channel


def update_likes(video_id,user_id):
    video_db = video_database_class.VideoDatabase()
    video_db.update_likes_record(video_id,user_id)


def update_comments(video_id,user_id,comment):
    video_db = video_database_class.VideoDatabase()
    video_db.update_comments_record(video_id,user_id,comment)

