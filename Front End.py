import tkinter as tk
import Back
from PIL import ImageTk,Image
from io import BytesIO

from Back import fetch_items, calculate, Item

ids = [453,440,442,444,447,449,451,2351,2355,2353,2357,2359,2361,2363]
items = fetch_items(ids)

root = tk.Tk()
root.geometry("300x400")

bars = tk.Frame(root, background="blue",width=100)
content = tk.Frame(root, background="red")
gp = tk.Frame(content, background="green", height=50)
info = tk.PanedWindow(content, background="yellow")


bars.pack(side = "left", fill = "both")
content.pack(side = "right", expand = True, fill = "both")
gp.pack(side="top", fill="x")
info.pack(side="bottom", fill="both", expand=True)

# class Display_Item(tk.Frame):
#     def __init__(self,parent,item):
#         tk.Frame.__init__(self,parent)
#         self.parent = parent
#         self.item_id = item.getIid()
#         self.widgets(item)
#     def widgets(self, item):
#         self.name = tk.Label(self,text = item.getName())
#         self.photo = ImageTk.PhotoImage(item.getIcon())
#         self.img = tk.Label(self,image = self.photo)
#         self.price = tk.Label(self,text = item.getPrice())
#
#         self.name.grid(row=2, column=1,sticky = "ew")
#         self.img.grid(row = 1,column = 1,sticky = "ew")
#         self.price.grid(row = 3,column = 1,sticky = "ew")
class BarButton(tk.Button):
    def __init__(self, parent, bar):
        tk.Button.__init__(self, parent)
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
        button.grid(row = counter, column = 0)



# counter=1
# for item in items:
#     id = Display_Item(root,item)
#     id.grid(row = 1,column = counter,padx = 10,pady = 10)
#     root.columnconfigure(counter,weight = 1)
#     counter+=1
# calculate(10000,items[1],items[0],1)

root.mainloop()