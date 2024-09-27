from tkinter import messagebox
from tkinter import filedialog
import random
import json
import os

try:
    from customtkinter import *
    from PIL import Image, ImageTk
except:
    os.system("pip install customtkinter")
    os.system("pip install pillow")




user = os.getlogin()

try:
    image_settings = Image.open("image/settings.png")
except:
    pass


path = None
def image_user():
    global path
    filetypes = [("image files", "*.png;*.jpg;*.jpeg;*.gif*.bmp"),
                ("ALL files", "*.*")]
    path = filedialog.askopenfilename(filetypes=filetypes)
    if path:
        change_settings()
        img = Image.open(path)
        img = img.resize((w, h))
        photo = ImageTk.PhotoImage(img)
        btn_img.configure(image=photo)
    else:
        pass
    os.system("cls || clear")
    print("Runner...")

settings_file = "settings.json"

def load_settings():
    try:
        with open(settings_file, "r") as file:
            settings = json.load(file)
    except FileNotFoundError:
        settings = {
            "user" : user,
            "lvl" : 0,
            "index_color" : 0,
            "index_level_up" : 0,
            "gems" : 500,
            "coin" : 50000,
            "win" : 0,
            "los" : 0,
            "theme": "dark",
            "light": False,
            "dark": True,
            "system": False,
            "type_line": "bold",
            "image" : path,
            "premo" : []
        }

    return settings


def save_settings(settings):
    with open(settings_file, "w") as file:
        json.dump(settings, file, indent=4)

settings = load_settings()

def change_settings():
    global settings
    settings["user"] = user
    settings["lvl"] = lvl
    settings["index_color"] = index_color
    settings["index_level_up"] = index_level_up
    settings["gems"] = gems
    settings["coin"] = num
    settings["win"] = win
    settings["los"] = los
    settings["theme"] = theme
    settings["type_line"] = type_line
    settings["image"] = path
    settings["premo"] = premo

    save_settings(settings)

username = settings["user"]
lvl = settings["lvl"]
index_color = settings["index_color"]
index_level_up = settings["index_level_up"]
gems = settings["gems"]
num = settings["coin"]
win = settings["win"]
los = settings["los"]
theme = settings["theme"]
light = settings["light"]
dark = settings["dark"]
system = settings["system"]
type_line = settings["type_line"]
path = settings["image"]
premo = settings["premo"]


# def premo_random():
#     global random_pre
#     # char = "GAFCB0123456798MPOBKJ"
#     char = "GA"
#     random_pre = ''.join(random.choice(char)for _ in range(1))

# def check_premo():
#     global num, gems, random_pre
#     premo_random()
#     if random_pre in premo:
#         messagebox.showinfo("error", "the premo code false")
#         return
#     elif ent_premo.get() == random_pre:
#         premo.append(random_pre)
#         num += 3000
#         gems += 20
#         lbl_gems.configure(text=f"JEWELS: {gems}")
#         lbl_coin.configure(text=f"COIN: {num}")

#     change_settings()



def color_():
    global color_choose, index_color
    color_choose = ""
    if index_color == 0:
        color_choose = "yellow"
        index_color += 1
        return color_choose
    elif index_color == 1:
        color_choose = "orange"
        index_color = 0
        return color_choose
    else:
        index_color = 0
        return

color_choose = color_()

mota = 0
def cazeno():
    global num, win, los, mota, gems, index_level_up, lvl, color_choose


    if num <= 0:
        messagebox.showinfo("Game Over", "Your coin balance is zero. Game over.")
        return

    rehan = ent_one_to.get()
    coin = ent_rehan.get()

    try:
        rehan = int(rehan)
        coin = int(coin)
    except ValueError:
        messagebox.showerror("Error", "The entries contain errors.")
        return

    if rehan <= 0 or rehan > 9:
        messagebox.showinfo("Info", "value must be between 1 and 9.")
        return
    

    if int(coin) < 500:
        num = 500
        lbl_coin.configure(text=f"COIN: {num}")
        messagebox.showerror("Error", "Enter an amount starting from 500")
        return 
    

    if not (1 <= coin <= num):
        messagebox.showerror("Error", f"Coin value must be between 500 and {num}.")
        return

    ran = random.randint(1, 9)
    mota = num / coin


    if rehan == ran:
        num += coin
        win += 1
        gems += 3
        lbl_gems.configure(text=f"JEWELS: {gems}")
        lbl_coin.configure(text=f"COIN: {num}")
        lbl_win.configure(text=f"WIN: {win}")
        lbl_mta.configure(text=f"REMAINING: {int(mota)}")
        if index_level_up < 144:
            btn = CTkButton(frm_lvl, text="", width=5, height=9,
                            fg_color=color_choose, hover=False, corner_radius=4)
            btn.place(x=index_level_up, y=1)
            index_level_up += 4
        elif index_level_up == 144:
            lvl += 1
            lbl_lvl.configure(text=f"LV {lvl}")
            index_level_up = 0
            color_choose = color_()
            gems += 100
            # lbl_gems.configure(text=f"JEWELS: {gems}")
            gaways_frm.place(x=180, y=15)
            lbl_gems.configure(text=f"JEWELS: {gems}")
            lbl_gaways.configure(text="YOU GOT 100 GEMS")


    else:
        num -= coin
        los += 1
        lbl_coin.configure(text=f"COIN: {num}")
        lbl_los.configure(text=f"LOSS: {los}")
        lbl_mta.configure(text=f"REMAINING: {int(mota)}")

    if num <= 0:
        messagebox.showinfo("Game Over", "Your coin balance is zero. Game over.")

    win_list = [10, 20, 30,
                40, 50, 60,
                70, 80, 90,
                100, 110, 120,
                130, 140, 150,
                160, 170, 180,
                190, 200, 250,
                300, 400, 500,
                650, 800, 1000]

    if win in win_list:
        win += 1
        gems += 50
        gaways_frm.place(x=180, y=15)
        lbl_gems.configure(text=f"JEWELS: {gems}")
        lbl_gaways.configure(text="YOU GOT 50 GEMS")


    change_settings()

def shop(price):
    global num, gems

    if price == 25 and gems >= 25:
        gems -= 25
        num += 2500
        lbl_gems.configure(text=f"JEWELS: {gems}")
        lbl_coin.configure(text=f"COIN: {num}")
        frm_done_s.place(x=175, y=15)
        lbl_done_s.configure(text=f"PURCHASE COMPLETED SUCCESSFULLY {price}")

    elif price == 50 and gems >= 50:
        gems -= 50
        num += 6500
        lbl_gems.configure(text=f"JEWELS: {gems}")
        lbl_coin.configure(text=f"COIN: {num}")
        frm_done_s.place(x=175, y=15)
        lbl_done_s.configure(text=f"PURCHASE COMPLETED SUCCESSFULLY {price}")

    elif price == 100 and gems >= 100:
        gems -= 100
        num += 15000
        lbl_gems.configure(text=f"JEWELS: {gems}")
        lbl_coin.configure(text=f"COIN: {num}")
        frm_done_s.place(x=175, y=15)
        lbl_done_s.configure(text=f"PURCHASE COMPLETED SUCCESSFULLY {price}")

    else:
        messagebox.showinfo("Not enough", "Your gems are not enough")

    change_settings()


def save_settings_frm():

    global theme, type_line

    if light_mode.get():
        settings["theme"] = "light"
        theme = settings["theme"]
        set_appearance_mode(theme)
        settings["light"] = True
        settings["dark"] = False
        settings["system"] = False

    elif dark_mode.get():
        settings["theme"] = "dark"
        theme = settings["theme"]
        set_appearance_mode(theme)
        settings["light"] = False
        settings["dark"] = True
        settings["system"] = False

    elif system_mode.get():
        settings["theme"] = "system"
        theme = settings["theme"]
        set_appearance_mode(theme)
        settings["light"] = False
        settings["dark"] = False
        settings["system"] = True

    else:
        settings["theme"] = "dark"
        theme = settings["theme"]
        set_appearance_mode(theme)
        settings["light"] = False
        settings["dark"] = True
        settings["system"] = False


    if type_bold.get():
        settings["type_line"] = "bold"
        type_line = settings["type_line"]

    elif type_normal.get():
        settings["type_line"] = "normal"
        type_line = settings["type_line"]

    else:
        settings["type_line"] = "bold"
        type_line = settings["type_line"]

    change_settings()


root = ctk_tk.CTk()
root.geometry("650x430+550+200")
root.title("Guess the number game")
root.resizable(False, False)
root.configure(bg="black")

set_appearance_mode(theme)

try:
    img = Image.open(path)
    w = 50
    h = 55
    img = img.resize((w, h))
    photo = ImageTk.PhotoImage(img)
    btn_img = CTkButton(root, text="", 
                        width=50, height=50, 
                        fg_color="transparent", 
                        border_width=3, hover=False,
                        image=photo,
                        command=image_user)
    os.system("cls || clear")
except:
    btn_img = CTkButton(root, text="", 
                        width=50, height=50, 
                        fg_color="transparent", 
                        border_width=3, hover=False,
                        command=image_user)
btn_img.place(x=10, y=20)

lbl_user = CTkLabel(root, text=username, font=CTkFont("sans-serif", 10, type_line, "italic"))
lbl_user.place(x=74, y=17)

lbl_lvl = CTkLabel(root, text=f"LV {lvl}", fg_color="transparent", font=CTkFont("sans-serif", 10, type_line, "italic"))
lbl_lvl.place(x=74, y=34)

frm_lvl = CTkFrame(root, width=147, height=10, corner_radius=5, border_width=2)
frm_lvl.place(x=72, y=60)

for _ in range(0, index_level_up, 4):
    btn = CTkButton(frm_lvl, text="", width=5, height=9, fg_color=color_choose, hover=False, corner_radius=4)
    btn.place(x=_, y=1)

lbl_gems = CTkLabel(root, text=f"JEWELS: {gems}", font=CTkFont("sans-serif", 14, type_line, "italic"))
lbl_gems.place(x=25, y=90)


lbl_name_g = CTkLabel(root, text="LUCK GAME", font=CTkFont("sans-serif", 30, type_line, "italic"))
lbl_name_g.place(x=250, y=50)

lbl_coin = CTkLabel(root, text=f"COIN: {num}", font=CTkFont("sans-serif", 17, type_line, "italic"))
lbl_coin.place(x=270, y=120)

lbl_win = CTkLabel(root, text=f"WIN: {win}", font=CTkFont("sans-serif", 17, type_line, "italic"))
lbl_win.place(x=270, y=160)


lbl_los = CTkLabel(root, text=f"LOSS: {los}", font=CTkFont("sans-serif", 17, type_line, "italic"))
lbl_los.place(x=270, y=200)


lbl_mta = CTkLabel(root, text=f"REMAINING: {mota}", font=CTkFont("sans-serif", 17, type_line, "italic"))
lbl_mta.place(x=255, y=240)

ent_one_to = CTkEntry(root, width=170,
                height=30, corner_radius=5,
                border_width=2.5, border_color="black", placeholder_text="Enter Num From 1 To 9")
ent_one_to.place(x=230, y=280)

ent_rehan = CTkEntry(root, width=170,
                height=30, corner_radius=5,
                border_width=2.5, border_color="black", placeholder_text="Enter Number From Coin")
ent_rehan.place(x=230, y=320)

btn_result = CTkButton(root, text="PLAY", width=100,
                height=30, corner_radius=5,
                fg_color="black", hover_color="#303030", 
                command=cazeno)
btn_result.place(x=265, y=360)

btn_shop = CTkButton(root, text="SHOP", width=100,
                height=30, corner_radius=5,
                fg_color="black", hover_color="#303030", 
                command=lambda : frm_shop.place(x=75, y=105))
btn_shop.place(x=22, y=130)


frm_shop = CTkFrame(root, width=500,
                    height=200, border_width=4)
frm_shop.place(x=-1000, y=80)

btn_close_frm = CTkButton(frm_shop, text="X", width=30,
                height=30, corner_radius=5, text_color="blue",
                fg_color="transparent", hover_color="#303030", 
                command=lambda : frm_shop.place(x=-1000, y=70))
btn_close_frm.place(x=10, y=10)


lbl_shop_one = CTkLabel(frm_shop, text="JEWELS: 25\nCOIN: 2500", font=CTkFont("sans-serif", 14, type_line, "italic"))
lbl_shop_one.place(x=50, y=65)


btn_shop_one = CTkButton(frm_shop, text="BUY NOW", width=80,
                height=30, corner_radius=5,
                fg_color="black", hover_color="#303030", 
                command=lambda : shop(25))
btn_shop_one.place(x=50, y=115)


lbl_shop_two = CTkLabel(frm_shop, text="JEWELS: 50\nCOIN: 6500", font=CTkFont("sans-serif", 14, type_line, "italic"))
lbl_shop_two.place(x=200, y=65)


btn_shop_two = CTkButton(frm_shop, text="BUY NOW", width=80,
                height=30, corner_radius=5,
                fg_color="black", hover_color="#303030", 
                command=lambda : shop(50))
btn_shop_two.place(x=200, y=115)

lbl_shop_three = CTkLabel(frm_shop, text="JEWELS: 100\nCOIN: 15000", font=CTkFont("sans-serif", 14, type_line, "italic"))
lbl_shop_three.place(x=350, y=65)


btn_shop_three = CTkButton(frm_shop, text="BUY NOW", width=80,
                height=30, corner_radius=5,
                fg_color="black", hover_color="#303030", 
                command=lambda : shop(100))
btn_shop_three.place(x=350, y=115)


frm_done_s = CTkFrame(root, width=300,
                            height=50, border_width=4,
                            )
frm_done_s.place(x=-1000, y=80)


btn_close_done_s = CTkButton(frm_done_s, text="X", width=30,
                height=30, corner_radius=5, text_color="blue",
                fg_color="transparent", hover_color="#303030", 
                command=lambda : frm_done_s.place(x=-1000, y=70))
btn_close_done_s.place(x=10, y=10)

lbl_done_s = CTkLabel(frm_done_s, text="", font=CTkFont("sans-serif", 11, type_line, "italic"))
lbl_done_s.place(x=40, y=10)


gaways_frm = CTkFrame(root, width=300,
                            height=50, border_width=4,
                            )
gaways_frm.place(x=-1000, y=80)


btn_close_frm_g = CTkButton(gaways_frm, text="X", width=30,
                height=30, corner_radius=5,text_color="blue",
                fg_color="transparent", hover_color="#303030", 
                command=lambda : gaways_frm.place(x=-1000, y=70))
btn_close_frm_g.place(x=10, y=10)

lbl_gaways = CTkLabel(gaways_frm, text="", font=CTkFont("sans-serif", 14, type_line, "italic"))
lbl_gaways.place(x=80, y=10)

try:
    btn_settings = CTkButton(root, text="", width=30,
                    height=30, corner_radius=5,
                    fg_color="transparent", hover_color="#303030",
                    image=CTkImage(image_settings),
                    command=lambda : frm_settings.place(x=480, y=0))
    btn_settings.place(x=605, y=10)
except:
    btn_settings = CTkButton(root, text="SETTINGS", width=30,
                    height=30, corner_radius=5,
                    fg_color="black", hover_color="#303030",
                    command=lambda : frm_settings.place(x=480, y=0))
    btn_settings.place(x=560, y=10)


frm_settings = CTkFrame(root, width=170,
                            height=430, border_width=4,
                            )
frm_settings.place(x=-1000, y=70)


btn_close_frm_setting = CTkButton(frm_settings, text="X", width=30,
                height=30, corner_radius=5,text_color="blue",
                fg_color="transparent", hover_color="#303030", 
                command=lambda : frm_settings.place(x=-1000, y=70))
btn_close_frm_setting.place(x=10, y=10)


lbl_setting = CTkLabel(frm_settings, text="SETTINGS", font=CTkFont("sans-serif", 14, type_line, "italic"))
lbl_setting.place(x=50, y=35)

lbl_theme = CTkLabel(frm_settings, text="THEME", font=CTkFont("sans-serif", 12, type_line, "italic"))
lbl_theme.place(x=30, y=70)


Boolean_light_mode = BooleanVar()
Boolean_dark_mode = BooleanVar()
Boolean_system_mode = BooleanVar()

if light:
    Boolean_light_mode = BooleanVar(value=True)
elif dark:
    Boolean_dark_mode = BooleanVar(value=True)
elif system:
    Boolean_system_mode = BooleanVar(value=True)


light_mode = CTkCheckBox(frm_settings, text="LIGHT", 
                            corner_radius=20,
                            checkbox_height=17, checkbox_width=17, 
                            variable=Boolean_light_mode, 
                            font=CTkFont("sans-serif", 10, type_line, "italic"))
light_mode.place(x=40, y=105)


dark_mode = CTkCheckBox(frm_settings, text="DARK", 
                            corner_radius=20,
                            checkbox_height=17, checkbox_width=17, 
                            variable=Boolean_dark_mode, 
                            font=CTkFont("sans-serif", 10, type_line, "italic"))
dark_mode.place(x=40, y=135)


system_mode = CTkCheckBox(frm_settings, text="SYSTEM", 
                            corner_radius=20,
                            checkbox_height=17, checkbox_width=17, 
                            variable=Boolean_system_mode, 
                            font=CTkFont("sans-serif", 10, type_line, "italic"))
system_mode.place(x=40, y=165)



lbl_type_line = CTkLabel(frm_settings, text="FONT TYPE", font=CTkFont("sans-serif", 12, type_line, "italic"))
lbl_type_line.place(x=30, y=200)


Boolean_type_bold = BooleanVar()
Boolean_type_normal = BooleanVar()

if type_line == "bold":
    Boolean_type_bold = BooleanVar(value=True)
elif type_line == "normal":
    Boolean_type_normal = BooleanVar(value=True)

type_bold = CTkCheckBox(frm_settings, text="BOLD", 
                            corner_radius=20,
                            checkbox_height=17, checkbox_width=17, 
                            variable=Boolean_type_bold, 
                            font=CTkFont("sans-serif", 10, type_line, "italic"))
type_bold.place(x=40, y=235)


type_normal = CTkCheckBox(frm_settings, text="NORMAL", 
                            corner_radius=20,
                            checkbox_height=17, checkbox_width=17, 
                            variable=Boolean_type_normal, 
                            font=CTkFont("sans-serif", 10, type_line, "italic"))
type_normal.place(x=40, y=265)


btn_save_setting = CTkButton(frm_settings, text="SAVE", width=80,
                height=30, corner_radius=5,
                fg_color="black", hover_color="#303030", 
                command=save_settings_frm)
btn_save_setting.place(x=45, y=350)


# btn_premo = CTkButton(root, text="PREMO CODE", width=80,
#                 height=30, corner_radius=5,
#                 fg_color="black", hover_color="#303030", 
#                 command=lambda : frm_premo.place(x=460, y=300))
# btn_premo.place(x=550, y=395)

# frm_premo = CTkFrame(root, width=190,
#                             height=130, border_width=4,
#                             )
# frm_premo.place(x=-1000, y=80)

# btn_close_frm_pre = CTkButton(frm_premo, text="X", width=30,
#                 height=30, corner_radius=5, text_color="blue",
#                 fg_color="transparent", hover_color="#303030", 
#                 command=lambda : frm_premo.place(x=-1000, y=70))
# btn_close_frm_pre.place(x=10, y=10)

# ent_premo = CTkEntry(frm_premo, width=128,
#                 height=30, corner_radius=5,
#                 border_width=2.5, border_color="black", placeholder_text="Enter A Premo Code")
# ent_premo.place(x=30, y=45)

# btn_check_premo = CTkButton(frm_premo, text="CHECK", width=70,
#                 height=30, corner_radius=5,
#                 fg_color="black", hover_color="#303030", 
#                 command=check_premo)
# btn_check_premo.place(x=60, y=80)






lbl_dev = CTkLabel(root, text="MUHANNED_AMGED", font=CTkFont("sans-serif", 14, type_line, "italic"))
lbl_dev.place(x=20, y=400)


print("Runner...")

root.mainloop()

