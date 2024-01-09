from PIL import ImageTk,Image
import tkinter

r=tkinter.Tk()
r.geometry("900x600")

img=Image.open("fruits.png")
rimg=img.resize((60,60),Image.ANTIALIAS)

pimg=ImageTk.PhotoImage(rimg)

l=tkinter.Label(image=pimg)
l.place(x=70,y=30)

r.mainloop()

