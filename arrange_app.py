from tkinter import*
import os, shutil, time
from tkinter import ttk, filedialog, messagebox #using filedialog we can get popup we we can read the self.directory.
class Sorting_App:
    def __init__(self, root):
        self.root = root
        self.root.title("File Arrangement Application | Developed by Vivek Maurya")
        self.root.geometry("1350x700+0+0")
        self.root.resizable(0,0)
        self.root.config(bg="white")
        self.logo_icon=PhotoImage(file="E:\\PythonProject\\Arrange_File_Application\\res\\appiconre.png")
        title = Label(self.root, text="File Arrangement Application",padx=15,image=self.logo_icon, compound=LEFT, font=("impact", 40), bg="maroon", fg="white", anchor="w").place(x=0, y=0, relwidth=1)


        #======Section 1=======
        self.var_foldername=StringVar()
        lbl_select_folder=Label(self.root, text="Select Folder", font=("times new roman", 20, "bold"), bg="white").place(x=50, y=100,)
        txt_folder_name = Entry(self.root, textvariable=self.var_foldername, font=("times new roman", 15),state="readonly", bg="maroon").place(x=250, y=100, height=40, width=600)
        btn_browse = Button(self.root, text="BROWSE", command=self.browse, bd=2, relief=RAISED, font=("times new roman", 15, "bold"), cursor="hand2", bg="gray", fg="white", activebackground="gray", activeforeground="white").place(x=900, y=100, height=40, width=200)
        hr = Label(self.root, bg="lightgrey").place(x=50, y=160, height=2, width=1250)

        #======Section 2=======
        #======All Extensions=======
        self.image_extensions=["Image Extensions", '.jpg','.png', '.jpeg', '.JPG']
        self.audio_extensions=["Audio Extensions", '.wav','.mp3', '.m4a']
        self.video_extensions=["Video Extension", '.mp4', '.mkv']
        self.doc_extensions=["Documnet Extensions", '.doc', '.xlsx', '.xls', '.xml', '.csv', '.pdf', '.doc', '.docx', '.pptx', '.ppt', '.zip', '.rar']

        self.folders={
            'videos':self.video_extensions,
            'audios':self.audio_extensions,
            'images':self.image_extensions,
            'documents':self.doc_extensions
        }

        lbl_support_ext=Label(self.root, text="Various Supported Extensions", font=("times new roman", 20, "bold"), bg="white").place(x=50, y=170,)
        self.image_box = ttk.Combobox(self.root,state="readonly", values=self.image_extensions, font=("times new roman", 15), justify="center")
        self.image_box.place(x=60, y=230, width=270, height=35)
        self.image_box.current(0)

        self.video_box = ttk.Combobox(self.root,state="readonly", values=self.video_extensions, font=("times new roman", 15), justify="center")
        self.video_box.place(x=380, y=230, width=270, height=35)
        self.video_box.current(0)

        self.audio_box = ttk.Combobox(self.root,state="readonly", values=self.audio_extensions, font=("times new roman", 15), justify="center")
        self.audio_box.place(x=700, y=230, width=270, height=35)
        self.audio_box.current(0)

        self.doc_box = ttk.Combobox(self.root,state="readonly", values=self.doc_extensions, font=("times new roman", 15), justify="center")
        self.doc_box.place(x=1020, y=230, width=270, height=35)
        self.doc_box.current(0)

        #======Section 3=======
        #======All Image icons=======
        self.image_icon=PhotoImage(file="E:\\PythonProject\\Arrange_File_Application\\res\\imgre.png")
        self.audio_icon=PhotoImage(file="E:\\PythonProject\\Arrange_File_Application\\res\\audiore.png")
        self.video_icon=PhotoImage(file="E:\\PythonProject\\Arrange_File_Application\\res\\videore.png")
        self.docum_icon=PhotoImage(file="E:\\PythonProject\\Arrange_File_Application\\res\\docre.png")
        self.other_icon=PhotoImage(file="E:\\PythonProject\\Arrange_File_Application\\res\\unknownbgre.png")

        Frame1 = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        Frame1.place(x=50, y=300, width=1250, height=300)

        self.lbl_total_files=Label(Frame1, text="Total Files: 0", font=("times new roman", 17), bg="white")
        self.lbl_total_files.place(x=10,y=10)

        self.lbl_total_image = Label(Frame1, bd=2, relief=RAISED,pady=10, text="", image=self.image_icon, compound=TOP, font=("times new roman", 17, "bold"), bg="#008EA4", fg="white")
        self.lbl_total_image.place(x=16.66, y=60, width=230, height=200)

        self.lbl_total_audio = Label(Frame1, bd=2, relief=RAISED, text="", image=self.audio_icon, compound=TOP, font=("times new roman", 17, "bold"), bg="#008EA4", fg="white")
        self.lbl_total_audio.place(x=263.32, y=60, width=230, height=200)

        self.lbl_total_video = Label(Frame1, bd=2, relief=RAISED, pady=10, text="", image=self.video_icon, compound=TOP, font=("times new roman", 17, "bold"), bg="#008EA4", fg="white")
        self.lbl_total_video.place(x=509.98, y=60, width=230, height=200)

        self.lbl_total_docum = Label(Frame1, bd=2, relief=RAISED, text="", image=self.docum_icon, compound=TOP, font=("times new roman", 17, "bold"), bg="#008EA4", fg="white")
        self.lbl_total_docum.place(x=756.64, y=60, width=230, height=200)

        self.lbl_total_other = Label(Frame1, bd=2, relief=RAISED, text="", image=self.other_icon, compound=TOP, font=("times new roman", 17, "bold"), bg="#008EA4", fg="white")
        self.lbl_total_other.place(x=1003.3, y=60, width=230, height=200)


        #======Section 4=======
        #======All Image icons=======
        lbl_status=Label(self.root, text="STATUS", font=("times new roman", 20), bg="white").place(x=50, y=620)
        self.lbl_total=Label(self.root, text="", font=("times new roman", 17), bg="white", fg="Blue")
        self.lbl_total.place(x=300, y=620)
        self.lbl_moved=Label(self.root, text="", font=("times new roman", 17), bg="white", fg="Green")
        self.lbl_moved.place(x=500, y=620)
        self.lbl_left=Label(self.root, text="", font=("times new roman", 17), bg="white", fg ="red")
        self.lbl_left.place(x=700, y=620)
        
        self.btn_clear = Button(self.root, text="CLEAR", state=NORMAL, command=self.clear_fxn, bd=2, relief=RAISED, font=("times new roman", 15, "bold"), cursor="hand2", bg="#607d8b", fg="white", activebackground="#607d8b", activeforeground="white")
        self.btn_clear.place(x=880, y=615, height=40, width=200)
        self.btn_start = Button(self.root, text="START", state=DISABLED, command=self.start_fxn, bd=2, relief=RAISED, font=("times new roman", 15, "bold"), cursor="hand2", bg="#ff5722", fg="white", activebackground="#ff5722", activeforeground="white")
        self.btn_start.place(x=1100, y=615, height=40, width=200)

    
        
    
    def total_count(self):
        images=0
        audios=0
        videos=0
        documents=0
        others=0
        self.ttl=0
        
        for i in self.all_files:
            if os.path.isfile(os.path.join(self.directory,i))==True: #can also use (self.directory+"\\"+i) to join the path
                self.ttl+=1
                ext = "."+i.split(".")[-1]
                for folder_name in self.folders.items():  
                    # print(folder_name)
                    if ext.lower() in folder_name[1] and folder_name[0]=="images":
                        images+=1
                    elif ext.lower() in folder_name[1] and folder_name[0]=="audios":
                        audios+=1
                    elif ext.lower() in folder_name[1] and folder_name[0]=="videos":
                        videos+=1
                    elif ext.lower() in folder_name[1] and folder_name[0]=="documents":
                        documents+=1
                    
        others = self.ttl-(images+audios+videos+documents)
        self.lbl_total_image.config(text="Total Images\n"+str(images))
        self.lbl_total_audio.config(text="Total Audios\n"+str(audios))
        self.lbl_total_video.config(text="Total Videos\n"+str(videos))
        self.lbl_total_docum.config(text="Total Documents\n"+str(documents))
        self.lbl_total_other.config(text="Others\n"+str(others))
        self.lbl_total_files.config(text="Total Files: "+str(self.ttl))

        self.lbl_total.config(text="TOTAL : "+str(self.ttl))
        self.lbl_moved.config(text="MOVED : "+str(0))
        self.lbl_left.config(text="LEFT : "+str(self.ttl))

        
  

    def browse(self):
        op=filedialog.askdirectory(title="Select Folder for Arranging")
        if op!=None:
            self.var_foldername.set(str(op))
            self.directory =  self.var_foldername.get()
            self.other_name = "others"
            self.all_files = os.listdir(self.directory)
            self.rename_folder()
            #os.listdir will put all the files and folder present inside the given self.directory into the list
            #os.path.isfile() return true for all the files only not folder

            total_files = len(self.all_files)
            self.total_count()
            self.btn_start.config(state=NORMAL)

    def clear_fxn(self):
        self.btn_start.config(state=DISABLED)
        self.var_foldername.set("")
        self.lbl_total.config(text="")
        self.lbl_moved.config(text="")
        self.lbl_left.config(text="")
        
        self.lbl_total_image.config(text="")
        self.lbl_total_audio.config(text="")
        self.lbl_total_video.config(text="")
        self.lbl_total_docum.config(text="")
        self.lbl_total_other.config(text="")
        self.lbl_total_files.config(text="Total Files: 0")
        

    def start_fxn(self):
        # main code
        if self.var_foldername.get()!="":
            self.btn_clear.config(state=DISABLED)
            c=1
            for i in self.all_files:
                if os.path.isfile(os.path.join(self.directory,i))==True: #can also use (self.directory+"\\"+i) to join the path
                    ex = i.split(".")       #spliting the file name into name and extension
                    self.create_move(ex[-1],i)   # passing extension and full name
                    self.lbl_total.config(text="TOTAL : "+str(self.ttl))
                    self.lbl_moved.config(text="MOVED : "+str(c))
                    self.lbl_left.config(text="LEFT : "+str(self.ttl - c))

                      
                    self.lbl_total.update()
                    self.lbl_moved.update()
                    self.lbl_left.update()
                    
                                        
                    #print(f"Total files: {total_files} | Done: {count} | Left: {total_files - c}")
                    c+=1

            messagebox.showinfo("Success", "All files has moved successfully")
            self.btn_start.config(state=DISABLED)
            self.btn_clear.config(state=NORMAL)
        else:
            messagebox.showinfo("Error","Please select a folder")
            



    def rename_folder(self):
        for folder in os.listdir(self.directory):  #list the all files present inside the folder
            if os.path.isdir(os.path.join(self.directory,folder))==True:   # true if folder found, isdir() return boolean for given path
                # if folder.lower() in self.folders:
                os.rename(os.path.join(self.directory,folder), os.path.join(self.directory, folder.lower()))



    def create_move(self, ext, file_name):  #this function move the files to the designsted folder
        for folder_name in self.folders:
            flag=False
            if "."+ext in self.folders[folder_name]:
                if folder_name not in os.listdir(self.directory):
                    os.mkdir(os.path.join(self.directory, folder_name))   #mkdir(<dir>) used to make self.directory at specified location
                shutil.move(os.path.join(self.directory,file_name), os.path.join(self.directory,folder_name))  
                #shutil.move(<from_dir>, <to_dir>) used to move file to specified loaction

                flag=True
                break

        if flag != True: 
            # rename_other_folder()
            if self.other_name not in os.listdir(self.directory):
                os.mkdir(os.path.join(self.directory, self.other_name))
            shutil.move(os.path.join(self.directory,file_name), os.path.join(self.directory,self.other_name))


root = Tk()
obj = Sorting_App(root)
root.iconbitmap("E:\\PythonProject\\Arrange_File_Application\\res\\appicon.ico")
root.mainloop()