import tkinter as tk
 
def key_pressed(event):
    key = event.char
    if key:
        text_display.insert(tk.END, key)

root = tk.Tk()
root.title("Keyboard Typing App")

text_display = tk.Text(root, height=10, width=50)
text_display.pack()

root.bind('<KeyPress>', key_pressed)

root.mainloop()