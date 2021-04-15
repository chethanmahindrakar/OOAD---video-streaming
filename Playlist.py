import tkinter as tk
import tkfilebrowser
import gui
from csv import writer
from Exchange import *
import pandas as pd
import search_caller
import json
from os import startfile,getcwd
from gui import current_video



def read_database(current_user):
    data = pd.read_csv("database/Playlist.csv")
    user_playlist = data.loc[data['user_details'] == current_user]
    #print(user_playlist)
    return user_playlist


class ManagePlaylist(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        global current_user
        current_user = obtain_user_credentials()
        #print(current_user)
        tk.Label(self, text="Manage Playlists", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=7)

        tk.Button(self, text="View Playlist",command = lambda : master.switch_frame(ViewPlaylist)).pack(side="top", fill="x", pady=7)
        tk.Button(self, text="Create Playlist", command= lambda: master.switch_frame(CreatePlaylist)).pack(side="top", fill="x", pady=7)

        tk.Button(self, text="Go back to dashboard", command= lambda: master.switch_frame(gui.PageFour)).pack(side="top", fill="x", pady=7)
        tk.Button(self, text="Go back to Home Page", command=lambda: master.switch_frame(gui.PageThree)).pack(side="top",fill="x",pady=7)

class CreatePlaylist(tk.Frame):
        def __init__(self, master):
            tk.Frame.__init__(self, master)

            global current_user
            current_user = obtain_user_credentials()

            def get_playlist():
                data = pd.read_csv("database/Playlist.csv")
                user_playlist = data.loc[data['user_details'] == current_user]
                return user_playlist

            def playlist_exist():
                playlist_name = new_playlist_name.get()
                playlist_name = playlist_name.lower()
                all_user_playlist = get_playlist()
                all_user_playlist = all_user_playlist.values.tolist()

                temp1 =[]
                for i in all_user_playlist:
                    temp = i[1]
                    temp = temp.lower()
                    temp1.append(temp)

                if playlist_name in temp1:
                    label = tk.Label(self, text="That playlist already exists", bg='red', relief=tk.RAISED)
                    label.pack()
                else:
                    row = [current_user,playlist_name,' ']
                    #print(row)
                    with open('database/Playlist.csv', 'a') as f:
                        writer_object = writer(f)
                        writer_object.writerow(row)
                        label = tk.Label(self, text="Playlist added", bg='green', relief=tk.RAISED)
                        label.pack()
                        f.close()

            tk.Label(self, text="Creating new playlist", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=7)
            new_playlist_name= tk.StringVar()
            tk.Label(self, text = 'Enter Playlist name', font=('calibre',10, 'bold')).pack(side="top", fill="x", pady=7)
            tk.Entry(self, textvariable = new_playlist_name, font = ('calibre',10,'normal')).pack(side="top", fill="x", pady=7)
            tk.Button(self, text="Create Playlist", command=lambda: playlist_exist()).pack(
                side="top", fill="x", pady=7)
            tk.Button(self, text="Go back to dashboard", command=lambda: master.switch_frame(gui.PageFour)).pack(
                side="top", fill="x", pady=7)



class ViewSpecificPlaylist(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        current_playlist_info = obtain_playlist_info()

        current_playlist_info = current_playlist_info.values.tolist()
        #print(current_playlist_info)

        tk.Label(self, text=current_playlist_info[1], font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=7)

        #Reading the video information from the csv ifle and splitting it
        videos = current_playlist_info[2].split(";")
        for i in range(0,len(videos)):
            videos[i] = videos[i].split(",")
            #videos[i] = videos[i].split(" ")c

            def generic_tile(title):
                global current_video
                current_title = title
                ans = search_caller.search_video(current_title)
                current_video.append(ans)
                master.switch_frame(gui.PageSeven)

            def play_video(video):
                video = video[0]
                video = video.lower()
                data = ""
                with open("database/video.ndjson", 'r') as rp:
                    for line in rp:
                        line = json.loads(line)

                        curr_title = line['title']
                        path = line['url']

                        # check if title already exists
                        if (curr_title.lower() == video.lower()):
                            data = path
                startfile(data)


        for i in range(0,len(videos)):
            tk.Button(self, text=videos[i][0], command = lambda j = i : play_video(videos[j])).pack(side="top", fill="x", pady=7)

        tk.Button(self, text="View Playlist", command=lambda: master.switch_frame(ViewPlaylist)).pack(side="top",
                                                                                                      fill="x", pady=7)

class ViewPlaylist(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)


        tk.Label(self, text="All Playlists", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=7)

        #Reading the playlists of the specific user in the databse
        global playlist_info
        playlist_info = read_database(current_user)
        playlist_count = len(playlist_info)

        for i in range(0,playlist_count):
            playlists = playlist_info['playlist_name'].values.tolist()

            tk.Button(self, text = playlists[i] , command = lambda j =i:[  exchange_playlist_info(playlist_info.iloc[j]) ,master.switch_frame(ViewSpecificPlaylist)
                                                                    ]).pack(side="top", fill="x", pady=7)

        tk.Button(self, text="Go back to dashboard", command=lambda: master.switch_frame(gui.PageFour)).pack(side="top",
                                                                                                             fill="x",
                                                                                                             pady=7)
        tk.Button(self, text="Go back to Home Page", command=lambda: master.switch_frame(gui.PageThree)).pack(
            side="top", fill="x", pady=7)


