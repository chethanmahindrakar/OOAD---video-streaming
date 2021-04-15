# OOAD PROJECT -- ALL FRAMES
import csv
import tkinter as tk
import login_caller
import signup_caller
#import easygui
#from tkinter.filedialog import askopenfilename 
import tkfilebrowser
import video_database_class
import search_caller
import watch_caller
import Playlist
import Exchange
from PIL import Image,ImageTk
from reccengine import *



from os import startfile,getcwd




current_user = []
video_path=[]
current_video =[]


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        
        self._frame = new_frame
        self._frame.pack()
        #self._frame.pack(side = "top", fill = "both", expand = True)
        #self._frame.grid_rowconfigure(4, weight = 1)
        #self._frame.grid_columnconfigure(4, weight = 1)



class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # WELCOME MESSAGE
        tk.Label(self, text="Welcome to Video Streaming Site!\n Please Login or Signup", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", padx=20,pady=20)

        # LOGIN button
        tk.Button(self, text="Login",
                  command=lambda: master.switch_frame(PageOne)).pack()

        # SIGN UP button 
        tk.Button(self, text="Signup",
                  command=lambda: master.switch_frame(PageTwo)).pack()

# LOGIN page
class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Login Page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=7)

        #username label
        name_var=tk.StringVar()
        tk.Label(self, text = 'Email', font=('calibre',10, 'bold')).pack(side="top", fill="x", pady=7)
        tk.Entry(self,textvariable = name_var, font=('calibre',10,'normal')).pack(side="top", fill="x", pady=7)

        # password label
        passw_var=tk.StringVar()
        tk.Label(self, text = 'Password', font=('calibre',10, 'bold')).pack(side="top", fill="x", pady=7)
        tk.Entry(self, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*').pack(side="top", fill="x", pady=7)


        
        def attempt_login():
            name=name_var.get()
            password=passw_var.get()
            global current_user
            current_user=[]

            #print(name,password)

            if(len(name.replace(" ",""))==0 or len(password)==0):
                label = tk.Label( self, text="Enter ALL fields",bg='red', relief=tk.RAISED)
                label.pack()

            else:
                ans=login_caller.user_login(name,password)

                if(ans==False):
                    label = tk.Label( self, text="Invalid Login",bg='red', relief=tk.RAISED)
                    label.pack()
                else:
                    current_user.append(ans)
                    master.switch_frame(PageThree)
                    #print(current_user[0].firstName)


            name_var.set("")
            passw_var.set("")

            
            

        
        tk.Button(self, text="LOGIN", command=attempt_login).pack(side="top", fill="x", pady=7)
        
        tk.Button(self, text="Go back to Welcome Page",command=lambda: master.switch_frame(StartPage)).pack(side="top", fill="x", pady=7)



# SIGNUP page
class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        tk.Label(self, text="Sign Up Page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=7)

        #username label
        name_var=tk.StringVar()
        tk.Label(self, text = 'Email', font=('calibre',10, 'bold')).pack(side="top", fill="x", pady=7)
        tk.Entry(self,textvariable = name_var, font=('calibre',10,'normal')).pack(side="top", fill="x", pady=7)

        # password label
        passw_var=tk.StringVar()
        tk.Label(self, text = 'Password', font=('calibre',10, 'bold')).pack(side="top", fill="x", pady=7)
        tk.Entry(self, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*').pack(side="top", fill="x", pady=7)

        # firstName label
        firstname_var=tk.StringVar()
        tk.Label(self, text = 'First Name', font=('calibre',10, 'bold')).pack(side="top", fill="x", pady=7)
        tk.Entry(self,textvariable = firstname_var, font=('calibre',10,'normal')).pack(side="top", fill="x", pady=7)

        # lastname label
        lastname_var=tk.StringVar()
        tk.Label(self, text = 'Last Name', font=('calibre',10, 'bold')).pack(side="top", fill="x", pady=7)
        tk.Entry(self, textvariable = lastname_var, font = ('calibre',10,'normal')).pack(side="top", fill="x", pady=7)

        # age label
        age_var=tk.StringVar()
        tk.Label(self, text = 'Age', font=('calibre',10, 'bold')).pack(side="top", fill="x", pady=7)
        tk.Entry(self,textvariable = age_var, font=('calibre',10,'normal')).pack(side="top", fill="x", pady=7)

        # phone no label
        phone_var=tk.StringVar()
        tk.Label(self, text = 'Phone Number', font=('calibre',10, 'bold')).pack(side="top", fill="x", pady=7)
        tk.Entry(self, textvariable = phone_var, font = ('calibre',10,'normal')).pack(side="top", fill="x", pady=7)



        def attempt_signup():
            name=name_var.get()
            password=passw_var.get()
            firstname = firstname_var.get()
            lastname= lastname_var.get()
            age = age_var.get()
            phone = phone_var.get()

            if(len(name.replace(" ",""))==0 or len(password)==0 or len(firstname.replace(" ",""))==0 or len(lastname.replace(" ",""))==0 or len(age.replace(" ",""))==0 or len(phone.replace(" ",""))==0 ):
                label = tk.Label( self, text="Enter ALL fields",bg='red', relief=tk.RAISED)
                label.pack()
          
            else:
                #print(name,password)
                ans=signup_caller.user_signup(name,password,firstname,lastname,age,phone)

                if(ans==False):
                    label = tk.Label( self, text="A user with the same email address exists!",bg='red', relief=tk.RAISED)
                    label.pack()
                else:
                    label = tk.Label( self, text="Account successfully created. Login to use the application!",bg='green', relief=tk.RAISED)
                    label.pack()
            

            name_var.set("")
            passw_var.set("")
            firstname_var.set("")
            lastname_var.set("")
            age_var.set("")
            phone_var.set("")

            
        tk.Button(self, text="SIGN UP", command=attempt_signup).pack(side="top", fill="x", pady=7)

        tk.Button(self, text="Go back to Welcome Page",command=lambda: master.switch_frame(StartPage)).pack(side="top", fill="x", pady=7)



# HOME page
class PageThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        tk.Label(self, text="Home Page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=7)

        # atmiks reccomedation engine
        #tk.Button(self, text="Recommended videos").pack(side="top", fill="x", pady=7)

        tk.Button(self, text="Search videos",command=lambda: master.switch_frame(PageSix)).pack(side="top", fill="x", pady=7)

        tk.Button(self, text="Get personalized recommendations",command=lambda: master.switch_frame(PageEight)).pack(side="top", fill="x", pady=7)

        tk.Button(self, text="View User Dashboard",command=lambda: master.switch_frame(PageFour)).pack(side="top", fill="x", pady=7)

        tk.Button(self, text="LOGOUT", command=lambda: master.switch_frame(StartPage)).pack()


        def tile_0():
            global current_video
            current_title = disp_thumbnails[0][1]
            #print("current title",current_title)
            ans = search_caller.search_video(current_title)
            current_video.append(ans)
            master.switch_frame(PageSeven)

        def tile_1():
            global current_video
            current_title = disp_thumbnails[1][1]
            #print("current title",current_title)
            ans = search_caller.search_video(current_title)
            current_video.append(ans)
            master.switch_frame(PageSeven)

        def tile_2():
            global current_video
            current_title = disp_thumbnails[2][1]
            #print("current title",current_title)
            ans = search_caller.search_video(current_title)
            current_video.append(ans)
            master.switch_frame(PageSeven)

        def tile_3():
            global current_video
            current_title = disp_thumbnails[3][1]
            #print("current title",current_title)
            ans = search_caller.search_video(current_title)
            current_video.append(ans)
            master.switch_frame(PageSeven)



        recc = reccengine()
        disp_thumbnails = recc.reccomendations()

        self.photo = ImageTk.PhotoImage(Image.open(disp_thumbnails[0][0]).resize((400,300),Image.ANTIALIAS), master = master)
        tk.Button(self, image = self.photo,command=tile_0).pack(side='left',pady=5)

        self.photo1 = ImageTk.PhotoImage(Image.open(disp_thumbnails[1][0]).resize((400,300),Image.ANTIALIAS), master = master)
        tk.Button(self, image = self.photo1,command=tile_1).pack(side="right", pady=5)

        self.photo2 = ImageTk.PhotoImage(Image.open(disp_thumbnails[2][0]).resize((400,300),Image.ANTIALIAS), master = master)
        tk.Button(self, image = self.photo2,command=tile_2).pack(side="top", pady=5)

        self.photo3 = ImageTk.PhotoImage(Image.open(disp_thumbnails[3][0]).resize((400,300),Image.ANTIALIAS), master = master)
        tk.Button(self, image = self.photo3,command=tile_3).pack(side="bottom", pady=5)


# USER DASHBOARD page
class PageFour(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        tk.Label(self, text="User Dashboard", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=7)

        tk.Button(self, text="Upload Video",command=lambda: master.switch_frame(PageFive)).pack(side="top", fill="x", pady=7)

        # chethans playlists

        Exchange.exchange_user_credentials(current_user)
        tk.Button(self, text="Playlists", command=lambda: master.switch_frame(Playlist.ManagePlaylist)).pack(side="top",fill="x",pady=7)

        tk.Button(self, text="Go back to Home Page", command=lambda: master.switch_frame(PageThree)).pack(side="top", fill="x", pady=7)

        tk.Button(self, text="LOGOUT", command=lambda: master.switch_frame(StartPage)).pack(side="top", fill="x", pady=7)


# UPLOAD VIDEO Page
class PageFive(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        tk.Label(self, text="Upload Video", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=7)

        
        def open_file():
            global video_path
            rep = tkfilebrowser.askopenfilename(initialdir='/', initialfile='tmp',filetypes=[("Videos", "*.mp4")])
            video_path.append(rep)


        # title label
        title_var=tk.StringVar()
        tk.Label(self, text = 'Title', font=('calibre',10, 'bold')).pack(side="top", fill="x", pady=7)
        tk.Entry(self,textvariable = title_var, font=('calibre',10,'normal')).pack(side="top", fill="x", pady=7)

        # description label
        description_var=tk.StringVar()
        tk.Label(self, text = 'Description', font=('calibre',10, 'bold')).pack(side="top", fill="x", pady=7)
        tk.Entry(self,textvariable = description_var, font=('calibre',10,'normal')).pack(side="top", fill="x", pady=7)

        # video file label
        tk.Label(self, text = 'Select Video File', font=('calibre',10, 'bold')).pack(side="top", fill="x", pady=7)
        tk.Button(self, text="Choose File", command=open_file).pack(side="top", fill="x", pady=7)

    


        def attempt_upload():
            title=title_var.get()
            description = description_var.get()
            global current_user
            global video_path
                

            if(len(title.replace(" ",""))==0 or len(description.replace(" ",""))==0):
                label = tk.Label( self, text="Please enter ALL fields",bg='red', relief=tk.RAISED)
                label.pack()

            if(len(video_path)==0):
                label = tk.Label( self, text="Please upload a video file",bg='red', relief=tk.RAISED)
                label.pack()


            else:
                ans = current_user[0].upload_video(title=title,description=description,url=video_path[0])

            
                if(ans==False):
                    label = tk.Label( self, text="A video with the same title exists",bg='red', relief=tk.RAISED)
                    label.pack()
                elif(ans==True):
                    label = tk.Label( self, text="Video successfully uploaded",bg='green', relief=tk.RAISED)
                    label.pack()
            
            video_path=[]
            title_var.set("")
            description_var.set("")
            
        
        tk.Button(self, text="Upload", command=attempt_upload).pack(side="top", fill="x", pady=7)

        tk.Button(self, text="Go back to Home Page",command=lambda: master.switch_frame(PageThree)).pack(side="top", fill="x", pady=7)





# SEARCH VIDEO page

class PageSix(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        tk.Label(self, text="Search Video", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=7)

        # search label
        title_var=tk.StringVar()
        tk.Label(self, text = 'Enter video title', font=('calibre',10, 'bold')).pack(side="top", fill="x", pady=7)
        tk.Entry(self,textvariable = title_var, font=('calibre',10,'normal')).pack(side="top", fill="x", pady=7)


        def attempt_search():
            title=title_var.get()
            global current_video
            current_video=[]
            #print(name,password)


            if(len(title.replace(" ",""))==0):
                label = tk.Label( self, text="Enter the search field",bg='red', relief=tk.RAISED)
                label.pack()

            else:
                ans = search_caller.search_video(title)

                if(ans==False):
                    label = tk.Label( self, text="No video by this title",bg='red', relief=tk.RAISED)
                    label.pack()
                else:
                    current_video.append(ans)
                    master.switch_frame(PageSeven)
                    


            title_var.set("")
            
            

        
        tk.Button(self, text="Search", command=attempt_search).pack(side="top", fill="x", pady=7)
        
        tk.Button(self, text="Go back to Home Page",command=lambda: master.switch_frame(PageThree)).pack(side="top", fill="x", pady=7)



# DISPLAY/WATCH VIDEO page
class PageSeven(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Watch Video", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=7)

        global current_video

        # TITLE label
        tk.Label(self, text = 'Title:' + current_video[0].title, font=('calibre',10, 'bold')).pack(side="top", fill="x", pady=7)

        # DESCRIPTION label
        tk.Label(self, text = 'Description: ' + current_video[0].description, font=('calibre',10, 'bold')).pack(side="top", fill="x", pady=7)

        # USER label
        channel = watch_caller.find_channel(current_video[0].user_id)
        tk.Label(self, text = 'Channel: ' + channel, font=('calibre',10, 'bold')).pack(side="top", fill="x", pady=7)

        # PLAY VIDEO button
        def play_video():
            startfile(getcwd()+"\\"+current_video[0].url)
        
        tk.Button(self, text="Play Video",command=play_video).pack(side="top", fill="x", pady=7)

        #Add or remove from Playlist button
        tk.Button(self, text="Add to Playlist" , command = lambda: master.switch_frame(ModifyPlaylist)).pack(side="top", fill="x", pady=7)



        #LIKES label 
        tk.Label(self, text = 'No. of Likes: ' + str(len(current_video[0].likes)), font=('calibre',10, 'bold')).pack(side="top", fill="x", pady=7)
        
        def attempt_like():
            if(current_user[0].ID in current_video[0].likes):
                return 
            else:
                curr_user_id = current_user[0].ID
                current_video[0].likes.append(curr_user_id)
                watch_caller.update_likes(current_video[0].ID, curr_user_id)
                master.switch_frame(PageSeven)
        
        tk.Button(self, text="LIKE", command=attempt_like).pack(side="top", fill="x", pady=7)

        
        #COMMENTS label

        tk.Label(self, text = 'Comments: ' , font=('calibre',10, 'bold')).pack(side="top", fill="x", pady=7)
        
        for key in current_video[0].comments:
            comment_user = watch_caller.find_channel(int(key))
            tk.Label(self, text = comment_user, font=('calibre',9, 'bold')).pack(side="top", fill="x", pady=7)

            for c in current_video[0].comments[str(key)]:
                tk.Label(self, text = c, font=('calibre',9)).pack(side="top", fill="x", pady=5)

        #ADD COMMENT label
        comment_var=tk.StringVar()
        tk.Label(self, text = 'Enter your comment:', font=('calibre',10, 'bold')).pack(side="top", fill="x", pady=7)
        tk.Entry(self,textvariable = comment_var, font=('calibre',10,'normal')).pack(side="top", fill="x", pady=7)


        def attempt_comment():
            comment = comment_var.get()
            
            #print(len(comment.replace(" ","")))

            if(len(comment.replace(" ",""))==0):
                label = tk.Label( self, text="Enter the comment field",bg='red', relief=tk.RAISED)
                label.pack()
    
            else:  
                curr_user_id = current_user[0].ID
                if(str(curr_user_id) not in current_video[0].comments):
                    current_video[0].comments[str(curr_user_id)]=[]

                current_video[0].comments[str(curr_user_id)].append(comment)
                watch_caller.update_comments(current_video[0].ID, curr_user_id,comment)
                master.switch_frame(PageSeven)

            comment_var.set("")


        tk.Button(self, text="ADD COMMENT", command=attempt_comment).pack(side="top", fill="x", pady=7)

        

    
        
        def end_watch():
            global current_video
            current_video=[]
            master.switch_frame(PageThree)
            
        
        tk.Button(self, text="Go back to Home Page",command=end_watch).pack(side="top", fill="x", pady=7)

class ModifyPlaylist(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        def get_playlist():
            data = pd.read_csv("database/Playlist.csv")
            user_playlist = data.loc[data['user_details'] == current_user[0].ID]
            #print(user_playlist)
            return user_playlist

        def delete_in_playlist(playlist):
            video = current_video[0].title
            video = video.lower()
            #print(video)
            #print(playlist)
            temp = playlist[2]
            temp = temp.split(";")
            for i in temp:
                i.lower()

            if video in temp:
                temp.remove(video)
            video_string = ""
            for i in range(0,len(temp)):
                if i<len(temp)-1:
                    video_string = video_string + temp[i] + ";"
                else:
                    video_string = video_string + temp[i]
            #print(video_string)

            data = pd.read_csv("database/Playlist.csv")
            data = data.values.tolist()
            with open('database/Playlist.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["user_details", "playlist_name", "playlist_videos"])
                for i in data:
                    if i[0] == current_user[0].ID and i[1] ==playlist[1]:
                        i[2] = video_string
                        writer.writerow(i)
                    else:
                        writer.writerow(i)
                label = tk.Label(self, text="Video successfully deleted ", bg='green', relief=tk.RAISED)
                label.pack()


        def write_into_playlist(video_string,playlist):
            #print(playlist)
            data = pd.read_csv("database/Playlist.csv")
            data = data.values.tolist()
            with open('database/Playlist.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["user_details", "playlist_name", "playlist_videos"])
                #print(data)
                for i in data:
                    #print(i)
                    if i[0] == current_user[0].ID and i[1] ==playlist[1]:
                        i[2] = video_string
                        writer.writerow(i)


                    else:
                        writer.writerow(i)


        def check_playlist(playlist):
            video = current_video[0].title
            video = video.lower()
            current_video_info = playlist[2]
            current_video_info = current_video_info.split(";")
            only_video_titles = []

            for i in range(0,len(current_video_info)):
                temp = current_video_info[i]

                only_video_titles.append(temp.lower())

            cond = False
            if video in only_video_titles:
                cond = True
            if cond == True:
                label = tk.Label(self, text="Video already in playlist", bg='red', relief=tk.RAISED)
                label.pack()
                tk.Button(self, text="Delete from Playlist", command = lambda : delete_in_playlist(playlist)).pack(
                    side="top",
                    fill="x", pady=7)
            else:
                only_video_titles.append(video)

                video_string = ""
                for i in range(0,len(only_video_titles)):
                    if i<len(only_video_titles)-1:
                        video_string = video_string + only_video_titles[i] + ";"
                    else:
                        video_string = video_string + only_video_titles[i]

                write_into_playlist(video_string,playlist)
                label = tk.Label(self, text="Video has been successfully added", bg='green', relief=tk.RAISED)
                label.pack()


        tk.Label(self, text="Which Playlist would you like to add to?", font=('Helvetica', 18, "bold")).pack(
            side="top", fill="x", pady=7)

        playlist_info = get_playlist()
        playlist_count = len(playlist_info)

        info = playlist_info.values.tolist()

        for i in range(0,playlist_count):
            playlists = playlist_info['playlist_name'].values.tolist()
            tk.Button(self, text = info[i][1],command = lambda j=i :[check_playlist(info[j])]).pack(side="top", fill="x", pady=7)

        tk.Button(self, text="Go back to Video", command=lambda: master.switch_frame(PageSeven)).pack(side="top",
                                                                                                      fill="x", pady=7)



class PageEight(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        tk.Label(self, text="Choose tags for Personalized recommendations", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=7)

        # atmiks reccomedation engine
        tags_var = tk.StringVar()
        tk.Label(self, text = 'Please enter of of the following tags (any 2, seperated by ,comma):\n animals \n astronomy \n automobile \n big \n boat \n car \n city \n cute \n food \n funny \n life \n lol \n pets \n planet \n popular \n science \n ship \n smart \n trendy \n trndy \n universe \n warm \n wholesome \n world \n yummy', font=('calibre',10, 'bold')).pack(side="top", fill="x", pady=7)
        tk.Entry(self, textvariable = tags_var, font = ('calibre',10,'normal')).pack(side="top", fill="x", pady=7)

        def get_tags():
            tags=tags_var.get()
            if(tags):
                reccs = reccengine(tags)
                disp_thumbnail = reccs.personalized_reccs()
                def tile_4():
                    global current_video
                    current_title = disp_thumbnail[0][1]
                    #print("current title",current_title)
                    ans = search_caller.search_video(current_title)
                    current_video.append(ans)
                    master.switch_frame(PageSeven)
                def tile_5():
                    global current_video
                    current_title = disp_thumbnail[1][1]
                    #print("current title",current_title)
                    ans = search_caller.search_video(current_title)
                    current_video.append(ans)
                    master.switch_frame(PageSeven)

                self.photo = ImageTk.PhotoImage(Image.open(disp_thumbnail[0][0]).resize((400,300),Image.ANTIALIAS), master = master)
                tk.Button(self, image = self.photo,command = tile_4).pack(side='left',pady=5)
                self.photo1 = ImageTk.PhotoImage(Image.open(disp_thumbnail[1][0]).resize((400,300),Image.ANTIALIAS), master = master)
                tk.Button(self, image = self.photo1, command = tile_5).pack(side="right", pady=5)

            else: master.switch_frame(PageEight)

        tk.Button(self, text="Get Recommedations!", command=get_tags).pack(side="top", fill="x", pady=7)

        tk.Button(self,text='Go back to HomePage', command = lambda:master.switch_frame(PageThree)).pack(fill='x',pady=7)


    





if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()  