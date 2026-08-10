import tkinter as tk
from unittest import case

import Back
from PIL import ImageTk,Image
from io import BytesIO

from Back import fetch_items, calculate, Item

ids = [453,440,442,444,447,449,451,2351,2355,2353,2357,2359,2361,2363]
items = fetch_items(ids)

root = tk.Tk()
root.geometry("600x500")
root.title("Blast Furnace Calculator V1")

bars = tk.Frame(root)
entry = tk.Frame(root, height=40, borderwidth=5, relief="groove")
content = tk.Frame(root)

bars.grid(row=0, column=0, sticky="nesw", rowspan=2)
entry.grid(row=0, column=1, sticky="nesw")
content.grid(row=1, column=1, sticky="nesw")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=5)

root.rowconfigure(1, weight=1)

content.grid_propagate(0)

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

# - Content - Yes it's bad alright, i'll maybe refactor it at some point
# - Ore
oreImage = tk.Label(content, text="Img",font=14)
oreName = tk.Label(content, text="Ore",font=14)
orePrice = tk.Label(content, text="Price",font=14)
oreQuantity = tk.Label(content, text="Quantity",font=14)
oreTotal = tk.Label(content, text="Total",font=14)

# - Coal
coalImage = tk.Label(content, text="Img",font=14)
coalName = tk.Label(content, text="Ore",font=14)
coalPrice = tk.Label(content, text="Price",font=14)
coalQuantity = tk.Label(content, text="Quantity",font=14)
coalTotal = tk.Label(content, text="Total",font=14)

# - Bar
barImage = tk.Label(content, text="Img",font=14)
barName = tk.Label(content, text="Ore",font=14)
barPrice = tk.Label(content, text="Price",font=14)
barQuantity = tk.Label(content, text="Quantity",font=14)
barProfit = tk.Label(content, text="Profit",font=14)

# - Grid
oreImage.grid(row=0, column=0, sticky="nesw", padx=20, pady=20)
oreName.grid(row=1, column=0, sticky="nesw", padx=20, pady=20)
orePrice.grid(row=2, column=0, sticky="nesw", padx=20, pady=20)
oreQuantity.grid(row=3, column=0, sticky="nesw", padx=20, pady=20)
oreTotal.grid(row=4, column=0, sticky="nesw", padx=20, pady=20)

coalImage.grid(row=0, column=1, sticky="nesw", padx=20, pady=20)
coalName.grid(row=1, column=1, sticky="nesw", padx=20, pady=20)
coalPrice.grid(row=2, column=1, sticky="nesw", padx=20, pady=20)
coalQuantity.grid(row=3, column=1, sticky="nesw", padx=20, pady=20)
coalTotal.grid(row=4, column=1, sticky="nesw", padx=20, pady=20)

barImage.grid(row=0, column=2, sticky="nesw", padx=20, pady=20)
barName.grid(row=1, column=2, sticky="nesw", padx=20, pady=20)
barPrice.grid(row=2, column=2, sticky="nesw", padx=20, pady=20)
barQuantity.grid(row=3, column=2, sticky="nesw", padx=20, pady=20)
barProfit.grid(row=4, column=2, sticky="nesw", padx=20, pady=20)

content.columnconfigure(0, weight=1)
content.columnconfigure(1, weight=1)
content.columnconfigure(2, weight=1)

content.rowconfigure(0, weight=5)
content.rowconfigure(1, weight=1)
content.rowconfigure(2, weight=1)
content.rowconfigure(3, weight=1)
content.rowconfigure(4, weight=1)

# - Garbage prevention
images = []

def switchContent(bar):
    match bar.getName():
        case "Iron bar":
            images.clear()
            values = calculate(gpEntry, items[1], items[0], 0, items[7])
            print(gpEntry.get())
            ore = ImageTk.PhotoImage(items[1].getIcon().resize((60,60)))
            coal = ImageTk.PhotoImage(items[0].getIcon().resize((60,60)))
            bar = ImageTk.PhotoImage(items[7].getIcon().resize((60,60)))
            images.append(ore)
            images.append(coal)
            images.append(bar)
            oreImage.configure(image=ore)
            coalImage.configure(image=coal)
            barImage.configure(image=bar)

            oreName.configure(text=values["oreName"])
            orePrice.configure(text=values["orePrice"])
            oreQuantity.configure(text=values["oreQuantity"])
            oreTotal.configure(text=values["oreTotal"])

            coalName.configure(text=values["coalName"])
            coalPrice.configure(text=values["coalPrice"])
            coalQuantity.configure(text=values["coalQuantity"])
            coalTotal.configure(text=values["coalTotal"])

            barName.configure(text=values["barName"])
            barPrice.configure(text=values["barPrice"])
            barQuantity.configure(text=values["barQuantity"])
            barProfit.configure(text=values["barProfit"])

        case "Silver bar":
            images.clear()
            values = calculate(gpEntry, items[2], items[0], 0, items[8])
            ore = ImageTk.PhotoImage(items[2].getIcon().resize((60, 60)))
            coal = ImageTk.PhotoImage(items[0].getIcon().resize((60, 60)))
            bar = ImageTk.PhotoImage(items[8].getIcon().resize((60, 60)))
            images.append(ore)
            images.append(coal)
            images.append(bar)
            oreImage.configure(image=ore)
            coalImage.configure(image=coal)
            barImage.configure(image=bar)

            oreName.configure(text=values["oreName"])
            orePrice.configure(text=values["orePrice"])
            oreQuantity.configure(text=values["oreQuantity"])
            oreTotal.configure(text=values["oreTotal"])

            coalName.configure(text=values["coalName"])
            coalPrice.configure(text=values["coalPrice"])
            coalQuantity.configure(text=values["coalQuantity"])
            coalTotal.configure(text=values["coalTotal"])

            barName.configure(text=values["barName"])
            barPrice.configure(text=values["barPrice"])
            barQuantity.configure(text=values["barQuantity"])
            barProfit.configure(text=values["barProfit"])

        case "Steel bar":
            images.clear()
            values = calculate(gpEntry, items[1], items[0], 1, items[9])
            ore = ImageTk.PhotoImage(items[1].getIcon().resize((60, 60)))
            coal = ImageTk.PhotoImage(items[0].getIcon().resize((60, 60)))
            bar = ImageTk.PhotoImage(items[9].getIcon().resize((60, 60)))
            images.append(ore)
            images.append(coal)
            images.append(bar)
            oreImage.configure(image=ore)
            coalImage.configure(image=coal)
            barImage.configure(image=bar)

            oreName.configure(text=values["oreName"])
            orePrice.configure(text=values["orePrice"])
            oreQuantity.configure(text=values["oreQuantity"])
            oreTotal.configure(text=values["oreTotal"])

            coalName.configure(text=values["coalName"])
            coalPrice.configure(text=values["coalPrice"])
            coalQuantity.configure(text=values["coalQuantity"])
            coalTotal.configure(text=values["coalTotal"])

            barName.configure(text=values["barName"])
            barPrice.configure(text=values["barPrice"])
            barQuantity.configure(text=values["barQuantity"])
            barProfit.configure(text=values["barProfit"])

        case "Gold bar":
            images.clear()
            values = calculate(gpEntry, items[3], items[0], 0, items[10])
            ore = ImageTk.PhotoImage(items[3].getIcon().resize((60, 60)))
            coal = ImageTk.PhotoImage(items[0].getIcon().resize((60, 60)))
            bar = ImageTk.PhotoImage(items[10].getIcon().resize((60, 60)))
            images.append(ore)
            images.append(coal)
            images.append(bar)
            oreImage.configure(image=ore)
            coalImage.configure(image=coal)
            barImage.configure(image=bar)

            oreName.configure(text=values["oreName"])
            orePrice.configure(text=values["orePrice"])
            oreQuantity.configure(text=values["oreQuantity"])
            oreTotal.configure(text=values["oreTotal"])

            coalName.configure(text=values["coalName"])
            coalPrice.configure(text=values["coalPrice"])
            coalQuantity.configure(text=values["coalQuantity"])
            coalTotal.configure(text=values["coalTotal"])

            barName.configure(text=values["barName"])
            barPrice.configure(text=values["barPrice"])
            barQuantity.configure(text=values["barQuantity"])
            barProfit.configure(text=values["barProfit"])

        case "Mithril bar":
            images.clear()
            values = calculate(gpEntry, items[4], items[0], 2, items[11])
            ore = ImageTk.PhotoImage(items[4].getIcon().resize((60, 60)))
            coal = ImageTk.PhotoImage(items[0].getIcon().resize((60, 60)))
            bar = ImageTk.PhotoImage(items[11].getIcon().resize((60, 60)))
            images.append(ore)
            images.append(coal)
            images.append(bar)
            oreImage.configure(image=ore)
            coalImage.configure(image=coal)
            barImage.configure(image=bar)

            oreName.configure(text=values["oreName"])
            orePrice.configure(text=values["orePrice"])
            oreQuantity.configure(text=values["oreQuantity"])
            oreTotal.configure(text=values["oreTotal"])

            coalName.configure(text=values["coalName"])
            coalPrice.configure(text=values["coalPrice"])
            coalQuantity.configure(text=values["coalQuantity"])
            coalTotal.configure(text=values["coalTotal"])

            barName.configure(text=values["barName"])
            barPrice.configure(text=values["barPrice"])
            barQuantity.configure(text=values["barQuantity"])
            barProfit.configure(text=values["barProfit"])

        case "Adamantite bar":
            images.clear()
            values = calculate(gpEntry, items[5], items[0], 3, items[12])
            ore = ImageTk.PhotoImage(items[5].getIcon().resize((60, 60)))
            coal = ImageTk.PhotoImage(items[0].getIcon().resize((60, 60)))
            bar = ImageTk.PhotoImage(items[12].getIcon().resize((60, 60)))
            images.append(ore)
            images.append(coal)
            images.append(bar)
            oreImage.configure(image=ore)
            coalImage.configure(image=coal)
            barImage.configure(image=bar)

            oreName.configure(text=values["oreName"])
            orePrice.configure(text=values["orePrice"])
            oreQuantity.configure(text=values["oreQuantity"])
            oreTotal.configure(text=values["oreTotal"])

            coalName.configure(text=values["coalName"])
            coalPrice.configure(text=values["coalPrice"])
            coalQuantity.configure(text=values["coalQuantity"])
            coalTotal.configure(text=values["coalTotal"])

            barName.configure(text=values["barName"])
            barPrice.configure(text=values["barPrice"])
            barQuantity.configure(text=values["barQuantity"])
            barProfit.configure(text=values["barProfit"])

        case "Runite bar":
            images.clear()
            values = calculate(gpEntry, items[6], items[0], 4, items[13])
            ore = ImageTk.PhotoImage(items[6].getIcon().resize((60, 60)))
            coal = ImageTk.PhotoImage(items[0].getIcon().resize((60, 60)))
            bar = ImageTk.PhotoImage(items[13].getIcon().resize((60, 60)))
            images.append(ore)
            images.append(coal)
            images.append(bar)
            oreImage.configure(image=ore)
            coalImage.configure(image=coal)
            barImage.configure(image=bar)

            oreName.configure(text=values["oreName"])
            orePrice.configure(text=values["orePrice"])
            oreQuantity.configure(text=values["oreQuantity"])
            oreTotal.configure(text=values["oreTotal"])

            coalName.configure(text=values["coalName"])
            coalPrice.configure(text=values["coalPrice"])
            coalQuantity.configure(text=values["coalQuantity"])
            coalTotal.configure(text=values["coalTotal"])

            barName.configure(text=values["barName"])
            barPrice.configure(text=values["barPrice"])
            barQuantity.configure(text=values["barQuantity"])
            barProfit.configure(text=values["barProfit"])

# - Entry bar
amount = ""
gpEntry = tk.Entry(entry,textvariable=amount, font=20)

gpEntry.grid(row=0, column=0, sticky="nesw", padx=20, pady=20)
entry.columnconfigure(0, weight=1)

root.mainloop()