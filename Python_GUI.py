import tkinter
import tkinter as tk

r=tkinter.Tk()

# Widgets

r.title("GUI using Python")
# b1=tkinter.Button(text="Submit",bg="green",fg="#fff",width="20",height="2")
# b1.place(x=30,y=30)

l1=tkinter.Label(text="Name")
l1.place(x=10,y=60)
tf1=tkinter.Entry()
tf1.place(x=80,y=60)

l2=tkinter.Label(text="Mobile No.")
l2.place(x=10,y=100)
tf2=tkinter.Entry()
tf2.place(x=80,y=100)

rd1=tkinter.Radiobutton(text="Male",value="1")
rd1.place(x=10,y=140)

rd2=tkinter.Radiobutton(text="Female",value="2")
rd2.place(x=70,y=140)

cb1=tkinter.Checkbutton(text="Python")
cb1.place(x=10,y=170)

cb2=tkinter.Checkbutton(text="Java")
cb2.place(x=70,y=170)

r.mainloop()
