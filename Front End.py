import tkinter as tk
import Back
from PIL import ImageTk,Image
from io import BytesIO

from Back import fetch_items

ids = [453,440,444,447,449,451,952]
items = fetch_items(ids)

root = tk.Tk()
root.geometry("500x300")

class Display_Item(tk.Frame):
    def __init__(self,parent,item):
        tk.Frame.__init__(self,parent)
        self.parent = parent
        self.item_id = item.getIid()
        self.widgets(item)
    def widgets(self, item):
        self.name = tk.Label(self,text = item.getName())
        self.photo = ImageTk.PhotoImage(item.getIcon())
        self.img = tk.Label(self,image = self.photo)
        self.price = tk.Label(self,text = item.getPrice())

        self.name.grid(row=1, column=1,sticky = "ew")
        self.img.grid(row = 2,column = 1,sticky = "ew")
        self.price.grid(row = 3,column = 1,sticky = "ew")



counter=1
for item in items:
    id = Display_Item(root,item)
    id.grid(row = 1,column = counter,padx = 10,pady = 10)
    root.columnconfigure(counter,weight = 1)
    counter+=1

root.mainloop()