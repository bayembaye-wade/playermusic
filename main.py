import tkinter as tk
import os
import fnmatch
from PIL import Image, ImageTk

from pygame import mixer


canvas=tk.Tk()
canvas.title("charlylink player")
canvas.geometry("500x500")
canvas.config(bg='white')



rootpath ="C:\\Users\D E L L\Music\demo"
pattern="*.mp3"


mixer.init

prec_img = ImageTk.PhotoImage(Image.open("prec.jpg")) 
stop_img = ImageTk.PhotoImage(Image.open("stop.jpeg"))
play_img = ImageTk.PhotoImage(Image.open("play.png"))
pause_img = ImageTk.PhotoImage(Image.open("pause.jpeg"))
suiv_img = ImageTk.PhotoImage(Image.open("next.jpeg"))

def select():
    label.config(text=listbox.get("anchor"))
    mixer.music.load(rootpath +"\\"+ listbox.get("anchor"))
    mixer.misic.play()


def stop():
    mixer.music.stop()
    listbox.select_clear('active')


def suiv():
    next_song = listbox.curselection
    next_song=next_song[0]+1
    next_song_name=listbox.get(next_song)
    
    
    label.config(text=next_song_name)
    mixer.music.load(rootpath +"\\"+ next_song_name)
    mixer.misic.play()
    
    
    listbox.select_clear(0,'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)
    
    
    
    
    
def prec():
        
    prec_song = listbox.curselection
    prec_song=prec_song[0]-1
    prec_song_song_name=listbox.get(prec_song)
    
    
    label.config(text= prec_song_song_name)
    mixer.music.load(rootpath +"\\"+ prec_song_song_name)
    mixer.misic.play()
    
    listbox.select_clear(0,'end')
    listbox.activate(prec_song)
    listbox.select_set(next)



def pause ():
    if pauseButton["text"]== "pause":
        mixer.music.pause()
        playButton["text"]== "pay"
        
    else:
        mixer.music.unpause()
        pauseButton["text"]= "pause"
            


listbox=tk.Listbox(canvas, fg="cyan", bg="black", width=100, font=('poppin',14))
listbox.pack(padx=15, pady=15)


label= tk.Label(canvas , text="", bg='white', fg='black', font=('poppin', 18))
label.pack(pady=15)

top=tk.Frame(canvas, bg="white")
top.pack (padx= 10, pady=5, anchor='center')

precButton = tk.Button(canvas, text="prec", image=prec_img, bg= 'white', borderwidth=0, command=prec)
precButton.pack(pady=15, in_=top, side="left")
stopButton = tk.Button(canvas, text="stop", image=stop_img, bg= 'white', borderwidth=0, command = stop)
stopButton.pack(pady=15, in_=top, side="left")
playButton = tk.Button(canvas, text="play", image=play_img, bg= 'white', borderwidth=0, command=select)
playButton.pack(pady=15, in_=top, side="left")
pauseButton = tk.Button(canvas, text="pause", image=pause_img, bg= 'white', borderwidth=0, command=pause)
pauseButton.pack(pady=15, in_=top, side="left")
suivButton = tk.Button(canvas, text="suiv", image=suiv_img, bg= 'white', borderwidth=0, command=suiv)
suivButton.pack(pady=15, in_=top, side="left")



for root, dirs,files in os.walk(rootpath):
    
 for filename in fnmatch.filter(files,pattern):
    
  listbox.insert('end', filename)
   
   
canvas.mainloop()