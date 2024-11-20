# frame for GUI elements - load in physical things.
# text elements go in seperate method so reload only changes text - not the Gui
#from main import data  # for bringing in specific vars later
import tkinter as tk
from PIL import ImageTk, Image
from controller import *

def reload(event=None):
    count = reloadContent()
    i=0
    for element in count:
        print(count[i])
        i=i+1
    #canvas4.pack_forget()

def reloadElements(event):
    frame2.destroy()  # destroy works but pack doesn't
    reload()
    createNewFrame()
    # reload with new image - don't think image is actually updating

def settingsClick(event=None):

    
    def updateAPIkey():
        input = inputtxt.get("1.0", "end-1c")
        print(input)
        print("test")
    # open new frame with settings GUI and info
    print("settings clicked")
    newWindow = tk.Tk()
    newWindow.title("Settings")
    newWindow.configure(background="#1c5669", borderwidth=19) # renshuu color
    newWindow.minsize(300,200)
    newWindow.maxsize(300,200)
    newWindow.geometry("500x500+1000+300")
    inputtxt = tk.Text(newWindow, height=5, width=20)
    inputtxt.pack()
    UpdateButton = tk.Button(newWindow, text="Update",  command=updateAPIkey)
    UpdateButton.pack()

def toggleView(event):
    print("toggle view clicked")

def createNewFrame(): # only reload counts - graph doesn't change fast enough to be relavent  FIXME
    frame5 =tk.Frame(window, bg="yellow", borderwidth=5, highlightthickness=0, width=480, height=400)
    frame5.place(relx=0.5, rely=0.56, anchor=tk.CENTER) # kissing my dreams of rounded corners goodbye

#create the window
reload()
window = tk.Tk()
window.title("Renshuu GUI")
window.configure(background="#1c5669", borderwidth=19) # renshuu color
window.minsize(600,620)
window.maxsize(600,620)
window.geometry("500x500+1000+300")

frame =tk.Frame(window, bg="#1c5669", borderwidth=0, highlightthickness=0)
frame.grid()

canvas = tk.Canvas(frame, bg="#1c5669", width=100, height=100, borderwidth=0, highlightthickness=0)
canvas.grid(row=0, column=0)


character = tk.PhotoImage(file="myKao.png")
imagetest = (Image.open("myKao.png"))
img = imagetest.resize((100,100), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(img)
canvas.create_image(50,50,image=img)  # potential change, image is squashed. Acceptable the way it is but could look better

#title
l = tk.Label(window, bg="#1c5669", text = "renshuu dashboard \n 毎日がんばってね!", width=15, height=0, font="UD_Digi_Kyokasho", fg="white", anchor="nw")
l.config(font=("UD_Digi_Kyokasho", 20, "bold")) # to bold or not to bold?
l.grid(row=0,column=1)

# settings button
frame =tk.Frame(window, bg="#1c5669", borderwidth=0, highlightthickness=0, width=50, height =50)
frame.place(relx=0.9, rely=0.0)

canvas2 = tk.Canvas(frame, bg="#1c5669", borderwidth=0, highlightthickness=0, width=50, height=50)
#canvas2.grid()

img2 = tk.PhotoImage(file="settings.png")
imagetest2 = (Image.open("settings.png"))
img2 = imagetest2.resize((30,30), Image.Resampling.LANCZOS)
img2 = ImageTk.PhotoImage(img2)
canvas2.create_image(30,30, image=img2)
canvas2.grid()
canvas2.bind('<Button-1>', settingsClick) #activate settingsClick when clicked
canvas2.config(cursor="hand2") # make different cursor on hover

    # frame for content

frame4 =tk.Frame(window, bg="#201c1c", borderwidth=5, highlightthickness=0, width=480, height=400)
frame4.place(relx=0.5, rely=0.56, anchor=tk.CENTER)


frame2 =tk.Frame(window, bg="#201c1c", borderwidth=5, highlightthickness=0, width=480, height=400)
frame2.place(relx=0.5, rely=0.56, anchor=tk.CENTER) # kissing my dreams of rounded corners goodbye


    # create condition for this to show later: dispalys graph on frame
imagetest2 = (Image.open("my_plot.png"))
img3 = imagetest2.resize((480,400), Image.Resampling.LANCZOS) # cannot resize eps
img3 = ImageTk.PhotoImage(img3)
image_label2 = tk.Label(frame2, image =img3, borderwidth=0, highlightthickness=0)
image_label2.pack()

    # button on bottom of frame to change view
canvas3 = tk.Canvas(window, bg="#1c5669", borderwidth=0, highlightthickness=0, width=300, height=50)
canvas3.place(relx=0.6, rely=0.92)
text = canvas3.create_text(120, 30, text="View JLPT Progress Graph >>", fill="white", width="300", font=("UD_Digi_Kyokasho", 12, "bold"), anchor="center")
canvas3.tag_bind(text, "<Button-1>", toggleView)
canvas3.config(cursor="hand2")
    #View JLPT Progress Graph >>
    #View Daily Goals >>

canvas4 = tk.Canvas(window, bg="#1c5669", borderwidth=0, highlightthickness=0, width=60, height=60)
canvas4.place(relx=0.7, rely=0.03)
text2 = canvas4.create_text(30, 20, text="Reload Stats", fill="white", width="60", font=("UD_Digi_Kyokasho", 12, "bold"), anchor="center")
canvas4.tag_bind(text2, "<Button-1>", reloadElements)
canvas4.config(cursor="hand2")

window.mainloop()

    # if view is jlpt progress
        # display that stuff

    # if view is word of the day  # do i want to keep word of the day?
        # display that stuff

    # if view is schedules
        # display that stuff

    # for each view either have to create a new file that this can read from, or pass it from controller

# add buttons for each view


# now alter here depending on what view is selected

# daily review, daily word, jlpt progress


