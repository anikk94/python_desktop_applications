import tkinter as tk

def button_callback(event):
    print("button clicked")

window = tk.Tk()
window.title("test app")
window.geometry("600x400")

new_label = tk.Label(text="some sample text for my window")
new_label.grid(column=0, row=0)

mybut = tk.Button(window, text="big red button")
mybut.grid(column=1, row=0)

mybut.bind("<Button-1>", button_callback)

window.mainloop()