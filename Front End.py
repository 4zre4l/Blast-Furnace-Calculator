import tkinter as tk
import Back
from PIL import ImageTk,Image
from io import BytesIO

from Back import fetch_items, calculate, Item

ids = [453,440,442,444,447,449,451,2351,2355,2353,2357,2359,2361,2363]
items = fetch_items(ids)

root = tk.Tk()
root.geometry("500x500")

bars = tk.Frame(root,bg="red")
entry = tk.Frame(root,bg="blue")
content = tk.Frame(root,bg="yellow")

bars.grid(row=0, column=0, sticky="nesw", rowspan=2)
entry.grid(row=0, column=1, sticky="nesw")
content.grid(row=1, column=1, sticky="nesw")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=5)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=5)

# - Side Bar
bars.columnconfigure(0, weight=1)

class BarButton(tk.Button):
    def __init__(self, parent, bar):
        tk.Button.__init__(self, parent, text=bar.getName())
        self.bar = bar
        self.text = bar.getName()
        self.photos = ImageTk.PhotoImage(bar.getIcon())
        self.image = self.photos

counter = 0
for item in items:
    counter += 1
    if "bar" in item.getName():
        print(item.getName())
        button = BarButton(bars,item)
        button.grid(row = counter, column = 0, sticky="nesw")
        bars.rowconfigure(counter, weight=1)

# - Entry bar
amount = ""
gpEntry = tk.Entry(entry,textvariable=amount)

gpEntry.grid(row=0, column=0, sticky="nesw")

root.mainloop()