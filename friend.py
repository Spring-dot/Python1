from tkinter import *
import tkinter as tk
import psycopg2

root = Tk()
root.title('FRIENDS!')

def get_data(name, nickname, phone):
    conn  = psycopg2.connect(dbname ="postgres", user="postgres", password="letscreate7#", host="localhost", port="5432")
    cur = conn.cursor()
    query = '''INSERT INTO friendship(name, nickname, phone) VALUES(%s, %s, %s);'''
    cur.execute(query, (name, nickname, phone))
    print("data inserted")
    conn.commit()
    conn.close()

canvas = Canvas(root, height=480, width=900)
canvas.pack()

frame = Frame()
frame.place(relx=0.3, rely=0.1, relwidth=0.8, relheight=0.8)

label =Label(frame, text="feed your info!")
label.grid(row=0,column= 1)

label =Label(frame, text="NAME")
label.grid(row=1,column= 0)

entry_name = Entry(frame)
entry_name.grid(row=1, column=1)

label =Label(frame, text="NICKNAME")
label.grid(row=2,column= 0)

entry_nickname = Entry(frame)
entry_nickname.grid(row=2, column=1)

label =Label(frame, text="PHONE NUM")
label.grid(row=3,column= 0)

entry_phone = Entry(frame)
entry_phone.grid(row=3, column=1)

button = Button(frame, text="add", command=lambda: get_data(entry_name.get(), entry_nickname.get(), entry_phone.get()))
button.grid(row=4, column=1)












root.mainloop()