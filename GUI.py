#GUI
import tkinter as tk
import functions

window = tk.Tk()
window.title('Code generator')

var1 = tk.StringVar()
var1.set(functions.get_codigo())

def anterior():
	functions.anterior()
	var1.set(functions.get_codigo())

def siguiente():
	functions.siguiente()
	var1.set(functions.get_codigo())

def copy_button():
    clip = tk.Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(functions.get_codigo())
    clip.destroy()

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

btn_decrease = tk.Button(master=window, text="anterior", command= lambda: anterior(), bg="blue", fg="green")
btn_decrease.grid(row=0, column=0, sticky="nsew")

btn_increase = tk.Button(master=window, text="siguiente", command= lambda: siguiente(), bg="blue", fg="green")
btn_increase.grid(row=0, column=2, sticky="nsew")

lbl_value = tk.Label(master=window, textvariable=var1)
lbl_value.grid(row=0, column=1)

btn_copy = tk.Button(master=window, text="copiar", command= lambda: copy_button(), bg="blue", fg="green")
btn_copy.grid(row=0, column=3, sticky="nsew")

window.mainloop()