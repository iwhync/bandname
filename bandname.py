from tkinter import *
import tkinter as tk
import random
import tkinter.scrolledtext as tkst

window = Tk()

window.geometry("250x200")

window.title("Band/Songs/Album names Generator")
window.configure(background='yellow')
lbl = Label(window, text="Band Names", font=("Arial Bold", 30)) 
lbl.grid(column=0, row=0)
lbl.configure(background="yellow")

lbl.grid(column=0, row=1) 

adjective = []
noun = []
rude = []

def rude():
    
    wind = tk.Tk()
    wind.title("Here's your fucking names") # title bar
    frame1 = tk.Frame(master = wind,bg = '#805000')
    frame1.pack(fill='both', expand='yes')
    editArea = tkst.ScrolledText(master = frame1,wrap = tk.WORD,width  = 50,height = 30)
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    


    a = 0
    b = random.randint(1,2873)
    c = random.randint(1,3634)
    f = random.randint(1,451)

    with open("adjectives.txt", "r") as a_file:
        while a < 2872:
            for line in a_file:
                x = line.strip()
                x.replace("/n","")
                adjective.append(x)
            a = a + 1

    a = 0

    with open("noun.txt", "r") as a_file:
        while a < 3633:
            for line in a_file:
                x = line.strip()
                x.replace("/n","")
                noun.append(x)
            a = a + 1

    a = 0

    with open("rude.txt", "r") as a_file:
        while a < 450:
            for line in a_file:
                x = line.strip()
                x.replace("/n","")
                ruder.append(x)
            a = a + 1

    d = 50
    while d > 0:
        final = random.randint(1,3)
        if final == 1:
            editArea.insert(tk.INSERT,f"{ruder[f]} {adjective[b]} {noun[c]}\n")
            b = random.randint(1,2873)
            c = random.randint(1,3634)
            f = random.randint(1,450)
            d = d - 1
        if final == 2:
            editArea.insert(tk.INSERT,f"{adjective[b]} {ruder[f]} {noun[c]}\n")
            b = random.randint(1,2873)
            c = random.randint(1,3634)
            f = random.randint(1,450)
            d = d - 1
        if final == 3:
            editArea.insert(tk.INSERT,f"{noun[c]} {adjective[b]} {ruder[f]}\n")
            b = random.randint(1,2873)
            c = random.randint(1,3634)
            f = random.randint(1,450)
            d = d - 1
        
def notrude():
    
    wind = tk.Tk()
    wind.title("Here's the names") # title bar
    frame1 = tk.Frame(master = wind,bg = '#805000')
    frame1.pack(fill='both', expand='yes')
    editArea = tkst.ScrolledText(master = frame1,wrap = tk.WORD,width  = 40,height = 30)
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)


    a = 0
    b = random.randint(1,2873)
    c = random.randint(1,3634)
    f = random.randint(1,451)

    with open("adjectives.txt", "r") as a_file:
        while a < 2872:
            for line in a_file:
                x = line.strip()
                x.replace("/n","")
                adjective.append(x)
            a = a + 1

    a = 0
    with open("noun.txt", "r") as a_file:
        while a < 3633:
            for line in a_file:
                x = line.strip()
                x.replace("/n","")
                noun.append(x)
            a = a + 1

    d = 50
    while d >= 0:
        editArea.insert(tk.INSERT,f"{adjective[b]} {noun[c]}\n")
        b = random.randint(1,2873)
        c = random.randint(1,3634)
        d = d - 1
        
btn0 = Button(window, text="Rude Names", bg="white", fg="black",command=rude)
btn1 = Button(window, text="Normal Names", bg="white", fg="black",command=notrude)

btn0.place(x=30, y=100) 
btn1.place(x=120, y=100)
        
window.mainloop()
