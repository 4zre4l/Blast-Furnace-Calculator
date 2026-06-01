import tkinter as tk
import Back
from PIL import ImageTk,Image
from io import BytesIO

ids = [453,440,444,447,449,451]

root = tk.Tk()
root.geometry("500x300")

class Display_Item(tk.Frame):
    def __init__(self,parent,item_id):
        tk.Frame.__init__(self,parent)
        self.parent = parent
        self.item_id = item_id
        self.widgets()
    def widgets(self):
        self.name = tk.Label(self,text = Back.fetch_item_name(self.item_id))
        self.photo = ImageTk.PhotoImage(Back.fetch_item_pic(self.item_id))
        self.img = tk.Label(self,image = self.photo)
        self.price = tk.Label(self,text = Back.fetch_item_price(self.item_id))

        self.name.grid(row=1, column=1,sticky = "ew")
        self.img.grid(row = 2,column = 1,sticky = "ew")
        self.price.grid(row = 3,column = 1,sticky = "ew")



counter=1
for id in ids:
    id = Display_Item(root,id)
    id.grid(row = 1,column = counter,padx = 10,pady = 10)
    root.columnconfigure(counter,weight = 1)
    counter+=1

root.mainloop()