import tkinter as tk
import Back
from PIL import ImageTk,Image
from io import BytesIO

root = tk.Tk()
root.geometry("300x300")

logo = ImageTk.PhotoImage(Back.fetch_item_pic(453))

label = tk.Label(root, image = logo)
label.pack()

button = tk.Button (root, text = "Convert", command = print(Back.fetch_item_price(453)))
button.pack()

root.mainloop()