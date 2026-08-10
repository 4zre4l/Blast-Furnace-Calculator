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

def switchContent(bar):
    match bar.getName():
        case "Iron bar":
            print(bar.getName())
            content.configure(bg="purple")

        case "Silver bar":
            print(bar.getName())

        case "Steel bar":
            print(bar.getName())

        case "Gold bar":
            print(bar.getName())

        case "Mithril bar":
            print(bar.getName())

        case "Adamantite bar":
            print(bar.getName())

        case "Runite bar":
            print(bar.getName())


counter = 0
for item in items:
    counter += 1
    if "bar" in item.getName():
        button = BarButton(bars,item)
        button.grid(row = counter, column = 0, sticky="nesw")
        bars.rowconfigure(counter, weight=1)

# - Entry bar
amount = ""
gpEntry = tk.Entry(entry,textvariable=amount)

gpEntry.grid(row=0, column=0, sticky="nesw", padx=30, pady=30)
entry.columnconfigure(0, weight=1)

root.mainloop()