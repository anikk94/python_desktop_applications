import tkinter as tk

window = tk.Tk()
window.title("tkinter widgets")
window.geometry("800x640")

w1 = tk.Entry(window, width=25)
w1.grid(column=0, row=0)

w2 = tk.Button(window, text="click me")
w2.grid(column=0, row=1)


window.mainloop()