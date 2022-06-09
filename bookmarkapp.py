import tkinter as tk
import webbrowser
def linkedin(event):
    webbrowser.open_new_tab("https://www.linkedin.com/in/anirudh-krishnan-komaralingam-a47b43112/")
def facebook(event):
    webbrowser.open_new_tab("https://www.facebook.com/anirudh.krishnan.77/")

window = tk.Tk()
window.geometry("400x200")
window.title("tkinter bookmark app")

label = tk.Label(text="My Social Media")
label.grid(column=0, row=0)

linkedin_button = tk.Button(window, text="Linkedin", bg="orange")
linkedin_button.grid(column=2, row=1)
facebook_button = tk.Button(window, text="Facebook", bg="blue")
facebook_button.grid(column=3, row=1)

linkedin_button.bind("<Button-1>", linkedin)
facebook_button.bind("<Button-1>", facebook)

window.mainloop()