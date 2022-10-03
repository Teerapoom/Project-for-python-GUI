# from curses import window
from tkinter  import *
from tkinter.tix import ButtonBox
root = Tk()
root.title("QRCode Generator")
canvas = Canvas(root,width=400,height=500)
canvas.pack()

# ชื่อโปรเเกรม

app_label =Label(root,text="QRCode Generator",font=("Arial",20,"bold"))
canvas.create_window(200,50,window=app_label)

# ระบุชื่อพร้อมกับลิงค์ - >
name_label = Label(root,text="ชื่อคิวอาร์โค้ด")
canvas.create_window(200,100,window=name_label)

name_entry = Entry(root)
canvas.create_window(200,130,window=name_entry)


link_label = Label(root,text="URL")
canvas.create_window(200,160,window=link_label)

link_entry = Entry(root)
canvas.create_window(200,180,window=link_entry )

# ปุ่ม
button = Button(text="สร้างคิวอาร์โค้ด")
canvas.create_window(200,230,window=button  )



root.mainloop()