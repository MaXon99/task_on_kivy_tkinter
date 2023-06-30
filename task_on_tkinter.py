from tkinter import*

def eternal():
    x.config(text = int(void.get()) + int(void2.get()))


mod = Tk()
mod.title("Сложение двух чисел")
mod.geometry("500x500")
mod["bg"] = "Grey"
void = Entry(mod, width = 40, bg = "cyan", fg= "Black", font = "Consolas")
void.pack()
void.place(x = 440,  y = 80)

void2 = Entry(mod, width = 40, bg = "cyan", fg = "Black", font = "Consolas")
void2.pack()
void2.place( x = 440, y = 120)

But = Button(mod, text = "Сложить", width = 30, height = 7, command = eternal, activebackground = "red" )
But.pack()
But.place(x = 550,  y = 180)

x = Label(mod, text="", width = 40, height = 3, bg = "Black", fg = "white")
x.pack()
x.place( x = 530, y = 350)


mod.mainloop()




