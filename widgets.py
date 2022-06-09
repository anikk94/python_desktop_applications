import tkinter as tk

window = tk.Tk()
window.title("tkinter widgets")
window.geometry("800x640")

w1 = tk.Entry(window, width=25)
w1.grid(column=0, row=0)

w2 = tk.Button(window, text="click me")
w2.grid(column=0, row=1)
w3 = tk.Checkbutton(window, text="checkbutton", variable=tk.IntVar())
w3.grid(column=0, row=2)

w4 = tk.Label(window, text="label widget")
w4.grid(column=0, row=3)


window.mainloop()