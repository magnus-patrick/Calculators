import tkinter as tk

window = tk.Tk()
window.geometry("700x400")
window.title("Tkinter Experiment")


widget = tk.Label(window, text = "Want to do derivatives?", font = ("Times New Roman", 20))
widget.pack(padx = 35, pady = 20)

def click():
    widget.config(text = "Okay!\n")


button = tk.Button(window,
                   text = "Press/Click here!",
                   command = click,
                   font = ("Times New Roman", 20))
button.pack(padx = 50, pady = 70)


window.mainloop()
