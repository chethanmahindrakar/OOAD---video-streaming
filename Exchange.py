
user = ""
playlist1 = ""

def exchange_user_credentials(current_user):
    global user
    user = current_user
    #print(user)

def obtain_user_credentials():
    return user[0].ID

def exchange_playlist_info(playlist_info):
    global playlist1

    playlist1 = playlist_info

def obtain_playlist_info():

    return playlist1

