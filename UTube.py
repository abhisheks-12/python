from tkinter import*
class Utube_app:
    def __init__(self,root):
        self.root = root
        self.root.title("UTube Downloader| Developed By Abhishek")
        self.root.geometry("500x420+300+50")
        self.root.resizable(True,True)
        self.root.config(bg = "white")

        title = Label(self.root,text='UTube Downloader| Developed By Abhishek',font=("times new roman",15),bg="#262626",fg="white").pack(side = TOP,fill = X)

        lbl_url = Label(self.root,text="Video URL ",font=("times new roman",15,"bold"),bg = "white").place(x=10,y=50)
        lbl_url = Entry(self.root,text="Video URL ",font=("times new roman",15),bg = "lightyellow").place(x=120,y=50,width=260)
        lbl_filetype = Label(self.root,text="File Type ",font=("times new roman",15,"bold"),bg = "white").place(x=10,y=90)

        self.var_fileType = StringVar()
        self.var_fileType.set("Video")
        video_radio = Radiobutton(self.root,text="Video ",variable=self.var_fileType,value = "video",font=("times new roman",13),bg = "white",activebackground="white",).place(x=120,y=90)
        audio_radio = Radiobutton(self.root,text="audio ",variable=self.var_fileType,value="audio",font=("times new roman",13),bg = "white",activebackground="white",).place(x=220,y=90)

        
        btn_search = Button(self.root,text="serach",font=("times new roman",15),bg="lightblue").place(x=350,y=90,height=35)

        frame1 = Frame(self.root,bd=2,relief=RIDGE,bg="lightyellow")
        frame1.place(x=10,y=130,width=470,height=150)

        self.video_title = Label(frame1,text='Video Title Here',font=("times new roman",15),bg="lightgray",anchor="w")
        self.video_title.place(x=0,y=0,relwidth=1)

        
        self.video_image = Label(frame1,text='Video \nImage',font=("times new roman",15),bg="lightgray",anchor="w")
        self.video_image.place(x=5,y=33,width=180,height=140)



root = Tk()
obj = Utube_app(root)
root.mainloop()

