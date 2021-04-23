#!/usr/bin/env python3
#author : Tegar Dev
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

root = tk.Tk()
root.title("Catatan Ku")
root.geometry("640x480")

def baru():
    text_area.delete(1.0,tk.END)

def bukaFile():
    pilih = filedialog.askopenfilename()
    file = open(pilih)
    teks = file.read()
    baru()
    text_area.insert(1.0,teks)

def simpanFile():
    pilih = filedialog.asksaveasfile(mode="w",defaultextension=".txt")
    teks2save = text_area.get(1.0,tk.END)
    pilih.write(teks2save)
    pilih.close()

def end():
    root.destroy()

frame = tk.Frame(root)
frame.grid(row=0,column=0)

new_button = ttk.Button(frame,
        text="New",
        command=baru)
new_button.grid(row=0,column=1)

open_button = ttk.Button(frame,
        text="Open",
        command=bukaFile)
open_button.grid(row=0,column=2)

save_button = ttk.Button(frame,
        text="Save",
        command=simpanFile)
save_button.grid(row=0,column=3)

exit_button = ttk.Button(frame,
        text="Exit",
        command=end)
exit_button.grid(row=0,column=5)

text_area = tk.Text(root,
        height=27)
text_area.grid(row=1,column=0)

status = tk.Label(root,
        text="Catatan Ku",)
status.grid(row=2,column=0)

root.mainloop()
