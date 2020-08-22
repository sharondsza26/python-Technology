from tkinter import *

# Main Window
root = Tk()
root.geometry("415x415")
root.title("Chat Client")

#Text area added to the Main Window
ta = Text(root)
ta.pack()

#Creating Panel and adding it to the MainWindow
p1 = Frame(root)

#Creating TextBox,Button and Adding it to the Panel
tf = Entry(p1)
send = Button(p1,text="Send")
tf.pack(side="left")
send.pack(side="left")

p1.pack()

root.mainloop()