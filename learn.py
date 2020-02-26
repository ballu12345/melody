from tkinter import *




#make a object root of class Tk()
root=Tk()



playPhoto=PhotoImage(file='play.png')    
playBtn=Button(root,image=playPhoto)
playBtn.grid(row=0,column=0)

stopPhoto=PhotoImage(file='stop.png')    
stopBtn=Button(root,image=stopPhoto)
stopBtn.grid(row=0,column=1)

pausePhoto=PhotoImage(file='pause.png')    
pauseBtn=Button(root,image=pausePhoto)
pauseBtn.grid(row=2,column=0)




root.mainloop()

