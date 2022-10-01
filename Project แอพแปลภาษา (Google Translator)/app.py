# from tkinter import font
from cgitb  import text
from tkinter  import *
from tkinter  import font
from googletrans import Translator


# ขนาดหน้าจอ
root = Tk()
root.title("Google Translate (EN-TH)")
root.geometry("530x300")
root.maxsize(530,300) #ค่าสูงสุด
root.minsize(530,300)  #ค่าต่ำสุด

# widget
label = Label(text="English to Thailand",font=("Arial",25,"bold"))
label.place(x=150,y=20)

# กล่องข้อความภาษาไทย
text1 = Text(root,width=30,height=10)
text1.place(x=10,y=70)


# กล่องข้อความภาษาอังกฤ
text2 = Text(root,width=30,height=10)
text2.place(x=260,y=70)

def translate():
    message =text1.get("1.0","end-1c") #ดึงข้อความจาก text1 มาเก็บในตัวแปร 1c คือ ช่องว่าง
    translator = Translator()
    output = translator.translate(text=message,src="en",dest="th") # src ภาษาต้นทาง dest ภาษาปลายทาง
    text2.insert("end",output.text)

def reset():
    text1.delete(1.0,"end")
    text2.delete(1.0,"end")

# ปุ่ม
translateBtn = Button(root,text="แปลภาษา",command=translate)
translateBtn.place(x=180,y=250)

clearBtn = Button(root,text="ล้างข้อมูล",command=reset)
clearBtn.place(x=280,y=250)

root.mainloop()