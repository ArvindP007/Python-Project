from tkinter import *
from tkinter import filedialog
import os
import pygame.mixer as mixer

mixer.init()
playlist=""
def load(listbox):
    os.chdir(filedialog.askdirectory(title='Open a songs directory'))
    tracks = os.listdir()
    for track in tracks:
        listbox.insert(END, track)

def play_song():
    #more to be written
    mixer.music.play()
    status.set("Song PLAYING")

def stop_song():
    mixer.music.stop()
    status.set("Song STOPPED")
    
def pause_song():
    mixer.music.pause()
    status.set("Song PAUSED")
    
def resume_song():
    mixer.music.unpause()
    status.set("Song RESUMED")

root = Tk()
root.title("Music Player")
root.geometry("1000x200")

trackframe = LabelFrame(root,text="Song Track",font=("times new roman",15,"bold"),bg="Navyblue",fg="white",bd=5,relief=GROOVE)
# trackframe.place(x=0,y=0,width=600,height=100)
trackframe.grid(row=1)
btn_pause = Button(root, text="Pause", command= pause_song, font=("Arial",24), bg='LightBlue')
btn_pause.grid(row=2, column =1)
btn_stop = Button(root, text="Stop", command= stop_song, font=("Arial",24), bg='LightBlue')
btn_stop.grid(row=2, column =2)
btn_play = Button(root, text="Play", command= play_song, font=("Arial",24), bg='LightBlue')
btn_play.grid(row=2, column =3)
btn_resume = Button(root, text="Resume", command= resume_song, font=("Arial",24), bg='LightBlue')
btn_resume.grid(row=2, column =4)
btn_load = Button(root, text="Load Directory", command= lambda: load(playlist), font=("Arial",24), bg='LightBlue')
btn_load.grid(row=3, column=1, columnspan=4)
root.mainloop()
