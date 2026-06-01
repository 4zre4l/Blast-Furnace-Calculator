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

# - Fetches the item price of a specified item id - #
def fetch_item_price(iid):
    grab = requests.get("https://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item="+str(iid))
    data = grab.json()

    # - Parsing data
    item_price = data['item']['current']['price']
    return gp_convert(item_price)

def fetch_item_pic(iid):
    grab = requests.get("https://secure.runescape.com/m=itemdb_oldschool/1779877772236_obj_sprite.gif?id="+str(iid))
    #takes the data grabbed and turns it into bytes
    data = Image.open(BytesIO(grab.content))

    # - Parsing data
    return data


# - Calculates the sum of current item value and outputs helpful info - #
def calculate(str_amount):
    amount = gp_convert(str_amount)
    amount = int(amount)
    coal = int(fetch_item_price(453))
    runite = int(fetch_item_price(451))
    one_total = math.floor(coal*4 + runite)
    r_amount = math.floor(amount/one_total)
    c_amount = r_amount*4
    print("With", str_amount, "gp, you can make", str(r_amount), "runite bars.")
    print("Runite ore:", str(r_amount))
    print("Coal:", str(c_amount))

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