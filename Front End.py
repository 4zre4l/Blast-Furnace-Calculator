import tkinter as tk
from unittest import case

import Back
from PIL import ImageTk,Image
from io import BytesIO

from Back import fetch_items, calculate, Item

ids = [453,440,442,444,447,449,451,2351,2355,2353,2357,2359,2361,2363]
items = fetch_items(ids)

root = tk.Tk()
root.geometry("500x500")
root.title("Blast Furnace Calculator")

bars = tk.Frame(root)
entry = tk.Frame(root, height=40)
content = tk.Frame(root,bg="yellow")

bars.grid(row=0, column=0, sticky="nesw", rowspan=2)
entry.grid(row=0, column=1, sticky="nesw")
content.grid(row=1, column=1, sticky="nesw")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=5)

root.rowconfigure(1, weight=1)

# - Side Bar
bars.columnconfigure(0, weight=1)

class BarButton(tk.Button):
    def __init__(self, parent, bar):
        tk.Button.__init__(self, parent, text=bar.getName(), image=ImageTk.PhotoImage(bar.getIcon()),
                           command=lambda: switchContent(bar), padx=10, pady=5)
        self.parent = parent
        self.bar = bar
        self.text = bar.getName()
        self.image = ImageTk.PhotoImage(bar.getIcon())
        self.configure(image=self.image)

counter = 0
for item in items:
    counter += 1
    if "bar" in item.getName():
        button = BarButton(bars,item)
        button.grid(row = counter, column = 0, sticky="nesw")
        bars.rowconfigure(counter, weight=1)

# - Content
# Build out frame with no data then config inside each case


def switchContent(bar):
    match bar.getName():
        case "Iron bar":
            calculate(gpEntry, items[1], items[0], 0, items[7])
            print(bar.getName())
            content.configure(bg="purple")

        case "Silver bar":
            print(bar.getName())

        case "Steel bar":
            calculate(gpEntry, items[1], items[0], 1, items[9])
            print(bar.getName())

        case "Gold bar":
            print(bar.getName())

        case "Mithril bar":
            print(bar.getName())

        case "Adamantite bar":
            print(bar.getName())

        case "Runite bar":
            print(bar.getName())

# - Entry bar
amount = ""
gpEntry = tk.Entry(entry,textvariable=amount, font=20)

gpEntry.grid(row=0, column=0, sticky="nesw", padx=20, pady=20)
entry.columnconfigure(0, weight=1)

root.mainloop()