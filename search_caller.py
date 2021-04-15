import video_database_class

def search_video(title):
    video_db = video_database_class.VideoDatabase()
    ans = video_db.search_for_video(title)

    return ans