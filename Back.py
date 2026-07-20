from io import BytesIO
import requests
import math
from PIL import ImageTk, Image

# - Converts the common strings used in OSRS to numbers - #
def gp_convert(string):
    if type(string) == str:
        if string[-1] == "k":
            string = string.translate(str.maketrans('', '', 'k'))
            string = string + "00"
        elif string[-1] == "m":
            string = string.translate(str.maketrans('', '', 'm'))
            string = string + "00000"
        if not any(c in "." for c in string):
            string = string + "0"
        string = string.translate(str.maketrans('', '', '.'))
    return string

class Item:
    def __init__(self, iid, icon, name, price):
        self.iid = iid
        self.icon = icon
        self.name = name
        self.price = price

    def getIid(self):
        return self.iid
    def getIcon(self):
        return self.icon
    def getName(self):
        return self.name
    def getPrice(self):
        return self.price

    def setIid(self, iid):
        self.iid = iid
    def setIcon(self, icon):
        self.icon = icon
    def setName(self, name):
        self.name = name
    def setPrice(self, price):
        self.price = price

def fetch_items(iids):
    items = []
    with requests.Session() as s:
        for iid in iids:
            grab = s.get("https://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item="+str(iid))
            data = grab.json()
            link = s.get(data['item']['icon'])
            parsed = Item(iid,Image.open(BytesIO(link.content)),data['item']['name'],data['item']['current']['price'])
            items.append(parsed)
    return items

# - Fetches the item price of a specified item id - #
def fetch_item_price(iid):
    grab = requests.get("https://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item="+str(iid))
    data = grab.json()

    # - Parsing data
    item_price = data['item']['current']['price']
    return gp_convert(item_price)

# - Fetches the item name of a specified item id - #
def fetch_item_name(iid):
    grab = requests.get("https://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item="+str(iid))
    data = grab.json()
    # - Parsing data
    item_name = data['item']['name']
    return item_name

def fetch_item_pic(iid):
    grab = requests.get("https://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item="+str(iid))
    data = grab.json()
    link = requests.get(data['item']['icon'])# - Parse for icon link
    img = Image.open(BytesIO(link.content)) # - Open image from link
    return img


# - Calculates the sum of current item value and outputs helpful info - #
def calculate(str_amount, ore, coal, coal_ratio):
    amount = gp_convert(str_amount)
    amount = int(amount)
    one_total = math.floor(coal.getPrice()*coal_ratio + ore.getPrice())
    r_amount = math.floor(amount/one_total)
    c_amount = r_amount*coal_ratio
    print(r_amount)
    print(c_amount)
    # print("With", str_amount, "gp, you can make", str(r_amount), ore.getName(), "bars.")
    # print("Runite ore:", str(r_amount))
    # print("Coal:", str(c_amount))

def run():
    print("#################################")
    print("#                               #")
    print("#    Blast Furnace Calculator   #")
    print("#                               #")
    print("#          =＾● ⋏ ●＾=          #")
    print("#                               #")
    print("#################################")
    while True:
        amount = input("How much gp do you have fella: ")
        calculate(amount)
        print("")
        print("")
        print("")

if __name__ == "__main__":
    run()