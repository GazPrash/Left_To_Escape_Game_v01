
# QUICK OVERVIEW // CODE PATTERN
# 1. IMPORTS
# 2. BOOLEANS AND DEFINED CONSTANTS
# 3. ALL THE COMMANDING FUNCTIONS & UTILITY FUNCTIONS
# 4. ROOT INITIALIZATION, GEOMETRY AND ALL THE IMAGE IMPORTS
# 5. DEFINING ALL THE WIDGETS AND LABELS IN BASE FRAMES


# ALL IMPORTS
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import random
import time


# DEFINING SOME BOOLEANS, VARIABLES AND CONSTANTS USED IN THE CODE
WIDTH = 440
HEIGHT = 710
money_now = 0
life_counter_now = 3
save_money = False
vendor_sel = False
giNa_sel = False
sKy_sel = False
label_to_be_destroyed = False
loop_i = 0
day_counter = 0
oncePurchased = False
dont_crt_again = False
quick_sel = False


#ENDING AND LORE TEXTS (BOTH)
intro_text = "You finally gain your consciousness, while looking and searching in the midst of dust clouds...\nSooner you realize that you've been crash-landed on an unknown planet, that you know nothing about.\n It takes you a not more than a few days to figure out that the planet is filled with dangerous and hostile factions.\n Ever the world is in a state of Watchful Peace...You never know what may follow next. "
help_text = "Use the 'Work' Button to work and skip to the next day.\nEvents are randomly generated scenarios, and you can use the 'New Evnet' to generate one, each per day.\n Each event is unique in it's own way, you will either swim in riches or get crushed by enemies.\n Check out the Store for some useful items."
ending1_text = "You finally manage to successfully assemble all the parts of your hyper-drive spaceship,\n with the belief in your heart that you will find your way home. After hours of hard work and\n a ton of luck, you prepare to take part from your home, your belongings, and the people of Alorix.\n As you board the cabin ,you take a alst glimpse of the beautiful planet\n...This Home is now behind you and the world ahead."
ending2_text = "You stare at the big human-sized capsule as you assemble the outeriors of the casket\n and make the final touches...the material looks very unique, the likes of which you've never seen,\n ensuring complete isolation from the outside world, built to withstand severe weather and damage.\n The cryptosleep casket is understood to freeze a person occupying them.\n You will not be aware of the time or the eras of the outside world,\n until someone finds this burial, the planet becomes hospitable again, and peace finds it's way back."




# ALL THE FUNCTIONS :-
# MAIN GAMEPLAY WINDOW INITIALIZING FUNCTION, ALSO SETS CHARACTER.
def newGame():
    global char_pop, char_1_img, char_2_img, char_3_img, label_to_be_destroyed, error_label_no_chara, dont_crt_again
    main_menu_frame.forget()
    if label_to_be_destroyed:
        error_label_no_chara.destroy()
    if label_to_be_destroyed and not dont_crt_again:
        quickSelect_chara_combobox.destroy()
        confirm_quickChara.destroy()

    main_game_frame.pack(padx = 20, pady=20, anchor=N)


    if vendor_sel:
        chara1_imageBox = Label(main_game_frame, image = char_1_img )
        chara1_imageBox.place(relx = 0.311, rely = 0.015)
    elif giNa_sel:
        chara2_imageBox = Label(main_game_frame, image = char_2_img )
        chara2_imageBox.place(relx = 0.311, rely = 0.015)
    elif sKy_sel:
        chara3_imageBox = Label(main_game_frame, image = char_3_img )
        chara3_imageBox.place(relx = 0.311, rely = 0.015)
    else:
        error_label_no_chara = Label(main_game_frame, text = "No Character selected, Select one to continue:", bg = "white", fg = "black",  borderwidth = 2, relief = SUNKEN)
        error_label_no_chara.place(relx = 0.11521, rely = 0.015)
        dont_crt_again = True
        label_to_be_destroyed = True


# FUNC BOUNDED FOR CHARACTERS TOP-LEVEL WINDOW
def char_info_pop():

    def chara_Sel():

        global giNa_sel, sKy_sel, vendor_sel

        if int(var_chara.get()) == 1:
            vendor_sel = True
            sKy_sel = False
            giNa_sel = False
            quickSelect_chara_combobox.destroy()

        elif int(var_chara.get()) == 2:
            giNa_sel = True
            vendor_sel = False
            sKy_sel = False
            quickSelect_chara_combobox.destroy()

        elif int(var_chara.get()) == 3:
            sKy_sel = True
            vendor_sel = False
            giNa_sel = False
            quickSelect_chara_combobox.destroy()

    def exit_chara():
        char_pop.destroy()     #JUST THE COMMANDING FUNCTION, WHICH CLOSES THE CHAR SELC WINDOW


    var_chara = IntVar()
    global char_pop, char_1_img ,char_2_img , char_3_img
    char_pop = Toplevel(root)
    char_pop.geometry("650x455")
    char_pop.title("Select A Character")

    frame_temp_pop = Frame(char_pop, bg = "#ECF0F1")
    frame_temp_pop.pack(expand = True, fill = BOTH)

    char_label = Label(frame_temp_pop, text = "3 characters to choose from!", font = "comicsans", bg = "#ECF0F1", fg = "#2E4053")
    char_label.grid(row = 0, column = 0, ipadx = 5)


    label_chara_1 = Label(frame_temp_pop, image = char_1_img, bg= "#ECF0F1")
    label_chara_1.grid(row =1, column = 0, ipadx = 14, ipady = 3, sticky = "w")
    label_chara_2 = Label(frame_temp_pop, image = char_2_img, bg= "#ECF0F1")
    label_chara_2.grid(row =2, column = 0, ipadx = 14, ipady = 1, sticky = "w")
    label_chara_3 = Label(frame_temp_pop, image = char_3_img, bg= "#ECF0F1")
    label_chara_3.grid(row =3, column = 0, ipadx = 14, ipady = 2, sticky = "w")


    # RADIO BUTTONS FOR CHARACTER SELECTION
    radio_1 = Radiobutton(frame_temp_pop, text = "Vendor, a mercenary from the Empire of Broken Shell,\n he is a extraordinary fighter amongst men", variable = var_chara, value = 1, command = chara_Sel, fg = "Black")
    radio_1.grid(row =1, column = 1)
    radio_2 = Radiobutton(frame_temp_pop, text = "Gina, a calculating defector, she lived a troubled\n childhood, and now is a troubling agent", variable = var_chara, value = 2, command = chara_Sel, fg = "Black")
    radio_2.grid(row=2, column=1)
    radio_3 = Radiobutton(frame_temp_pop, text = "Sky, is a multimillionare Genius, for all his life,\n he had someone to protect him, mkaing\n him less of a fighter", variable = var_chara, value = 3, command = chara_Sel, fg = "Black")
    radio_3.grid(row=3, column=1)


    exit_chara_frame = Button(frame_temp_pop, relief = GROOVE, text = "Go Back <<<", command = exit_chara)
    exit_chara_frame.grid(row =0, column =1, ipadx = 64)
    exit_chara_frame.config(width = 10)


#QUICK-CHARA SELECT FUNCTION
def quickCharaSel():
    global char_1_img, char_2_img, char_3_img, giNa_sel, sKy_sel, vendor_sel
    quickSelect_chara_combobox.destroy()
    confirm_quickChara.destroy()
    error_label_no_chara.destroy()
    chara_quicksel = combobox_string.get()

    if chara_quicksel.lower() == "vendor":
        chara1_imageBox = Label(main_game_frame, image = char_1_img )
        chara1_imageBox.place(relx = 0.311, rely = 0.015)
        vendor_sel = True
        sKy_sel = False
        giNa_sel = False
        quick_sel = True
    elif chara_quicksel.lower() == 'gina':
        chara2_imageBox = Label(main_game_frame, image = char_2_img )
        chara2_imageBox.place(relx = 0.311, rely = 0.015)
        giNa_sel = True
        vendor_sel = False
        sKy_sel = False
        quick_sel = True
    elif chara_quicksel.lower() == "sky":
        chara3_imageBox = Label(main_game_frame, image = char_3_img )
        chara3_imageBox.place(relx = 0.311, rely = 0.015)
        sKy_sel = True
        vendor_sel = False
        giNa_sel = False
        quick_sel = True


# STORE---> MASTER FUNCTION
def store():
    store_pop = Toplevel(root)
    store_pop.geometry("340x400")
    store_pop.title("What would you like to Purchase?")

    store_mainframe = Frame(store_pop, bg = "white")
    store_mainframe.pack(expand = True, fill = BOTH)


    store_label_img = PhotoImage(file = "icons/store.png")
    store_label = Label(store_mainframe, image = store_label_img, borderwidth=0)
    store_label.place(relx=0.2152, rely = 0.02)

    store_exit_btn = Button(store_mainframe, text = "Go Back", font = "tahoma 10", command = store_pop.destroy )
    store_exit_btn.place(relx=0.416, rely=0.815, relheight=0.07, relwidth=0.15)

    # STORE ITEMS
    label_i1 = Label(store_mainframe, text = "1. Small Cabin", fg = "black", font = "Avantgarde 10")
    label_i1.place(relx = 0.04, rely=0.32)
    label_i2 = Label(store_mainframe, text="2. Portable Spaceship", fg="black", font="Avantgarde 10")
    label_i2.place(relx=0.04, rely=0.4)
    label_i3 = Label(store_mainframe, text="3. Safehouse", fg="black", font="Avantgarde 10")
    label_i3.place(relx=0.04, rely=0.48)
    label_i4 = Label(store_mainframe, text="4. Protective Vest", fg="black", font="Avantgarde 10")
    label_i4.place(relx=0.04, rely=0.56)
    label_i5 = Label(store_mainframe, text="5. Hyper-Drive Warp Spaceship", fg="black", font="Avantgarde 10")
    label_i5.place(relx=0.04, rely=0.64)
    label_i6 = Label(store_mainframe, text="6. Cryocasket Sleeping Cell", fg="black", font="Avantgarde 10")
    label_i6.place(relx=0.04, rely=0.72)


    # NO PURCHASE FUNC // WHEN USER CANT AFFORD A SAID ITEM
    def no_purchase():
        label_cant_purchased = Label(store_mainframe, text="Can't purchase the given item; Not Enough Money!", fg="black", font="Avantgarde 10", bg="white")
        label_cant_purchased.place(relx=0.0562, rely=0.9)
        store_mainframe.update()
        time.sleep(1)
        label_cant_purchased.destroy()


    # PURCHASE FUNCTIONS, EACH FUNC IS BOUNDED TO A PARTICULAR BUTTON IN THE STORE WINDOW
    def item_purchased_1():
        global money_now, oncePurchased, life_counter_now
        if money_now >= 1000 and not oncePurchased:
            label_purchased = Label(store_mainframe, text="You Purchased the Item!", fg="black", font="Avantgarde 10", bg = "white")
            label_purchased.place(relx = 0.282, rely = 0.9)
            events_input("You a pruchased a cozy little cabin near the woods! [Life +1] \n\n")
            store_mainframe.update()
            time.sleep(1)
            label_purchased.destroy()
            button_i1.destroy()
            life_counter_now += 1
            life_counter_label.config(text=life_counter_now)
            life_counter_label.update()
            money_now -= 1000
            money_counter_label.config(text = money_now)
            money_counter_label.update()
            oncePurchased = True
        else:
            no_purchase()

    def item_purchased_2():
        global money_now
        if money_now >= 5000:
            label_purchased = Label(store_mainframe, text="You Purchased the Item!", fg="black", font="Avantgarde 10", bg = "white")
            label_purchased.place(relx = 0.282, rely = 0.9)
            events_input("You now own your very own 'Everyone can fly' Portable spaceship, Only operational within the planet's atmosphere. [Collectible]\n\n")
            store_mainframe.update()
            time.sleep(1)
            label_purchased.destroy()
            button_i2.destroy()
            money_now -= 5000
            money_counter_label.config(text=money_now)
            money_counter_label.update()
        else:
            no_purchase()

    def item_purchased_3():
        global money_now, life_counter_now
        if money_now >= 25000:
            label_purchased = Label(store_mainframe, text="You Purchased the Item!", fg="black", font="Avantgarde 10", bg = "white")
            label_purchased.place(relx = 0.282, rely = 0.9)
            events_input("You a pruchased a big house in a nearby City's Suburban area! [Life +1]\n\n" )
            store_mainframe.update()
            time.sleep(1)
            label_purchased.destroy()
            button_i3.destroy()
            life_counter_now += 2
            life_counter_label.config(text=life_counter_now)
            life_counter_label.update()
            money_now -= 25000
            money_counter_label.config(text=money_now)
            money_counter_label.update()
        else:
            no_purchase()

    def item_purchased_4():
        global life_counter_now, money_now
        if money_now >= 55000:
            label_purchased = Label(store_mainframe, text="You Purchased the Item!", fg="black", font="Avantgarde 10", bg = "white")
            label_purchased.place(relx = 0.282, rely = 0.9)
            events_input("You bought a Grade AA Protective Gear. [Life +2]\n\n")
            store_mainframe.update()
            time.sleep(1)
            label_purchased.destroy()
            button_i4.destroy()
            life_counter_now += 3
            life_counter_label.config(text=life_counter_now)
            life_counter_label.update()
            money_now -= 55000
            money_counter_label.config(text=money_now)
            money_counter_label.update()
        else:
            no_purchase()

    def item_purchased_5():
        global money_now
        if money_now >= 75000:
            label_purchased = Label(store_mainframe, text="You Purchased the Item!", fg="black", font="Avantgarde 10", bg = "white")
            label_purchased.place(relx = 0.282, rely = 0.9)
            events_input("Congratulations! You bought a Hyperdrive Warp-Speed Spaceship. Spaceship capable of running with in-built Hyperdrives can be used to travel b/w Planets!\n\n")
            store_mainframe.update()
            time.sleep(1)
            label_purchased.destroy()
            button_i5.destroy()
            money_now -= 75000
            money_counter_label.config(text=money_now)
            money_counter_label.update()
            spaceship_install.place(relx=0.3635, rely=0.805)
        else:
            no_purchase()

    def item_purchased_6():
        global money_now
        if money_now >= 95000:
            label_purchased = Label(store_mainframe, text="You Purchased the Item!", fg="black", font="Avantgarde 10", bg = "white")
            label_purchased.place(relx = 0.282, rely = 0.9)
            events_input("You managed to sucessfully assemble a cryocasket sleep module. A CSM can protect a human body for thousands of years, without making it age.\n\n")
            store_mainframe.update()
            time.sleep(1)
            label_purchased.destroy()
            button_i6.destroy()
            money_now -= 95000
            money_counter_label.config(text=money_now)
            money_counter_label.update()
            cryocasket_install.place(relx=0.5155, rely=0.81)
        else:
            no_purchase()


    #BUTTONS TO BUY ITEMS
    if not oncePurchased:
        button_i1 = Button(store_mainframe, text="1000 G", fg="black", font="helvetica 11", command = item_purchased_1)
        button_i1.place(relx=0.676, rely=0.32, relheight = 0.05, relwidth = 0.25)      # CABIN IS ONLY ONE TIME PURCHASE...
    button_i2 = Button(store_mainframe, text="5,000 G", fg="black", font="helvetica 12", command = item_purchased_2)
    button_i2.place(relx=0.676, rely=0.40, relheight=0.05, relwidth=0.25)
    button_i3 = Button(store_mainframe, text="25,000 G", fg="black", font="helvetica 12", command = item_purchased_3)
    button_i3.place(relx=0.676, rely=0.48, relheight=0.05, relwidth=0.25)
    button_i4 = Button(store_mainframe, text="55,000 G", fg="black", font="helvetica 12", command = item_purchased_4)
    button_i4.place(relx=0.676, rely=0.56, relheight=0.05, relwidth=0.25)
    button_i5 = Button(store_mainframe, text="75,000 G", fg="black", font="helvetica 12", command = item_purchased_5)
    button_i5.place(relx=0.676, rely=0.64, relheight=0.05, relwidth=0.25)
    button_i6 = Button(store_mainframe, text="95,000 G", fg="black", font="helvetica 12", command = item_purchased_6)
    button_i6.place(relx=0.676, rely=0.72, relheight=0.05, relwidth=0.25)

    store_pop.mainloop()


#THIS FUNCTION IS NOT BINDED TO ANY BUTTON BUT CAN BE SUMMONED TO PRINT TEXT IN THE EVENTS TAB AND THEN AUTOMATICALLY DISABLE IT, AFTER USE (TAKES 1 ARGUMENT AS STRING) [UTILITY FUNC]
def events_input(string):
    recent_events_tracker.config(state=NORMAL)
    recent_events_tracker.insert(END, string)
    recent_events_tracker.config(state=DISABLED)
    recent_events_tracker.see(END)


#FUNCTION THAT RANDOMLY GEN. RANDOM EVENT // BOUNDED TO 'NEW EVENT'
def event_vindaloop():
    global loop_i, money_now, life_counter_now, day_counter, oncePurchased
    day_counter += 1
    day_count_label.config(text=day_counter)
    day_count_label.update()

    with open("scripts/events.txt", "r") as f:
        spevents_list = f.readlines()
    loop_i = random.randint(0,34)
    rando_event_list = random.choices(spevents_list, weights= ([36, 36, 37, 44, 44, 33, 38, 42, 37, 35, 44, 36, 42, 43, 32, 45, 25, 25, 25, 25, 25, 25, 25, 25, 6, 6, 6, 6, 6, 6, 6, 4, 4, 4, 4]), k = 35)
    try:
        events_input(f"{rando_event_list[loop_i]}\n")
        event_num = spevents_list.index(rando_event_list[loop_i])
        actual_event_num = event_num + 1

        if actual_event_num <= 16:
            money_now += 237
            money_counter_label.config(text=money_now)
            money_counter_label.update()

        elif actual_event_num > 16 and actual_event_num <= 24:
            money_now += 500
            money_counter_label.config(text=money_now)
            money_counter_label.update()

        elif actual_event_num > 24 and actual_event_num <= 31:
            life_counter_now -= 1
            life_counter_label.config(text = life_counter_now)
            life_counter_label.update()

            if life_counter_now ==0:     # GAME RESET
                messagebox.showinfo("Game Over!", "You spent all your lives, Try again next time!")
                main_game_frame.forget()
                main_menu_frame.pack(padx=33, pady=133)
                # CLEANING EVENT TAB FOR RESET
                recent_events_tracker.config(state=NORMAL)
                recent_events_tracker.delete("1.0", END)
                recent_events_tracker.config(state=DISABLED)
                # MONEY COUNT RESET
                money_now = 0
                money_counter_label.config(text=money_now)
                money_counter_label.update()
                # LIVES COUNT RESET
                life_counter_now = 3
                life_counter_label.config(text=life_counter_now)
                life_counter_label.update()
                # DAY COUNT RESET
                day_counter = 0
                day_count_label.config(text=day_counter)
                day_count_label.update()
                oncePurchased = False

        elif actual_event_num > 31:
            money_now += 10000
            money_counter_label.config(text=money_now)
            money_counter_label.update()


    except Exception as e:
        print(e)
        # loop_i = 0
        # event_vindaloop()


# FUNCTION BOUNDED TO 'WORK'
def work_function():

    global money_now, day_counter
    money_now += 100
    day_counter += 1
    events_input("You wroked and earned 100 Gold!\n\n")

    money_counter_label.config(text=money_now)
    money_counter_label.update()

    day_count_label.config(text = day_counter)
    day_count_label.update()


# FRAME SWITCHER
def switch_to_frame_one():
    main_game_frame.forget()
    main_menu_frame.pack(padx=33, pady=153)


# HELP BOX WIDGET BOUNDED TO 'HELP'
def helpbox():
    helpbox_top = Toplevel(root)
    helpbox_top.geometry("730x300")
    helpbox_top.title("How to play the game")

    help_frame = Frame(helpbox_top, bg="#D0D3D4")
    help_frame.pack(expand = True, fill = BOTH)

    lore_label = Label(help_frame, text = intro_text, fg = "black", bg = "#D0D3D4")
    lore_label.place(relx = 0.043, rely = 0.15)

    help_label = Label(help_frame, text = help_text, fg = "black", bg = "#D0D3D4")
    help_label.place(relx = 0.065, rely = 0.5)

    back_btn = Button(help_frame, text = "Go Back", fg = "black", bg = "#D0D3D4", command = helpbox_top.destroy)
    back_btn.place(relx = 0.44, rely = 0.8)


# ENDING ENABLERS
def spaceship_ending():
    global day_counter
    spaceship_top = Toplevel(root)
    spaceship_top.geometry("685x200")
    spaceship_top.title("To the stars and beyond!")

    ending1_frame = Frame(spaceship_top, bg = "black")
    ending1_frame.pack(expand = True, fill = BOTH)


    days_finalcount = Label(ending1_frame, text = f"On the {day_counter}th Day, Since your arrival...", bg = "black", fg = "white")
    days_finalcount.place(relx = 0.35, rely = 0.1)

    ending1_label = Label(ending1_frame, text = ending1_text, fg = "white", bg= "black")
    ending1_label.place(relx = 0.06, rely = 0.24)

    theend_btn = Button(ending1_frame, text= "End The Journey.", command = root.destroy)
    theend_btn.place(relx = 0.42, rely = 0.8)

def cryocasket_ending():
    cryocasket_top = Toplevel(root)
    cryocasket_top.geometry("685x230")
    cryocasket_top.title("Unknown Future Awaits...")

    ending2_frame = Frame(cryocasket_top, bg = "black")
    ending2_frame.pack(expand = True, fill = BOTH)

    days_finalcount = Label(ending2_frame, text = f"On the {day_counter}th Day, Since your arrival...", bg = "black", fg = "white")
    days_finalcount.place(relx = 0.35, rely = 0.1)

    ending1_label = Label(ending2_frame, text = ending2_text, fg = "white", bg= "black")
    ending1_label.place(relx = 0.054, rely = 0.23)

    theend_btn = Button(ending2_frame, text= "End The Journey.", command = root.destroy)
    theend_btn.place(relx = 0.42, rely = 0.8)


# ROOT INFO
root = Tk()
root.geometry(f"{WIDTH}x{HEIGHT}")
root.maxsize(WIDTH, HEIGHT)
root.minsize(WIDTH, HEIGHT)
root.title("Left To Escape : Alorix")
root.iconbitmap('icons/game_icon.ico')


# ALL IMAGE IMPORTS
bg_img_main = PhotoImage(file = "icons/space_bg.png")
bg_gametitle = PhotoImage(file = "icons/bg_maintitle.png")
start_btn_im = PhotoImage(file = "icons/Start_exe.png")
chara_sel_bg = PhotoImage(file = "icons/chara_btn.png")
char_1_img = PhotoImage(file="icons/vendor.png")
char_2_img = PhotoImage(file="icons/gina.png")
char_3_img = PhotoImage(file="icons/sky.png")
exit_bg_btn = PhotoImage(file = 'icons/exit_bg.png')
money_gold = PhotoImage(file= "icons/gold_bg.png")
life_bg = PhotoImage(file = "icons/life_bg.png")
spaceship = PhotoImage(file = "icons/spaceship.png")
cryocasket = PhotoImage(file = "icons/cryo.png")
bg_2nd = PhotoImage(file = "icons/bg_alt.png")


# SETTING UP BASE GAME MENU, ICON AND BG
bg_label = Label(root, image = bg_img_main, bg = "black")
bg_label.place(relwidth =1, relheight = 1)


# THEME ADD-ON MADE BY RBENDE
style = ttk.Style(root)
root.tk.call("source", "sun-valley.tcl")
root.tk.call("set_theme", "light")


#PACKING MAIN MENU FRAME
main_menu_frame = Frame(root, width = 290,  height = 300, bg = "black")
main_menu_frame.pack(padx = 33, pady = 153)


# BUTTONS, TITLE @ MAIN MENU
maintitle_label = Label(root, image = bg_gametitle, bg = "black")
maintitle_label.place(relx = 0.211, rely = 0.087)

button_newGame = Button(main_menu_frame, image = start_btn_im, command = newGame, borderwidth = 0, bd = 0,  highlightthickness = 0, activebackground = "black", activeforeground="black")
chara_btn_selc = Button(main_menu_frame, image = chara_sel_bg, command = char_info_pop, borderwidth = 0, bd = 0,  highlightthickness = 0, activebackground = "black", activeforeground="black")
exit_btn = Button(main_menu_frame, image = exit_bg_btn, command = root.destroy, borderwidth = 0, bd = 0,  highlightthickness = 0, activebackground = "black", activeforeground="black")

button_newGame.place(relx = 0.243, rely = 0.25)
chara_btn_selc.place(relx = 0.0733, rely = 0.525)
exit_btn.place(relx = 0.273, rely = 0.7338)


# MY LABEL // MY OWN // MY PRECIOUS
my_label = Label(root, text = "Made by Emotional_Zebra, 2021", fg = "white", font = ("Avantgarde",8), bg = "black")
my_label.place(relx = 0.311, rely = 0.027)


# MAIN GAME FRAME // THE MAIN GAMEPLAY FRAME
main_game_frame = Frame(root, width = 360,  height = 680, bg= "#1B2631", highlightthickness = 1 )
main_game_frame.config(highlightbackground = "#979A9A", highlightcolor= "#979A9A")

bg_label = Label(main_game_frame, image = bg_2nd)
bg_label.place(relwidth =1, relheight = 1)


# BUTTONS
work_button = Button(main_game_frame, text = "WORK", command = work_function)
work_button.place(relx = 0.0480, rely = 0.89, relheight = 0.056, relwidth= 0.3)

help_button = Button(main_game_frame, text = "HELP", command = helpbox)
help_button.place(relx = 0.35, rely = 0.89, relheight = 0.056, relwidth= 0.3)

exit_main_game_button = Button(main_game_frame, text = "MAIN MENU", command = switch_to_frame_one)
exit_main_game_button.place(relx = 0.6515, rely = 0.89, relheight = 0.056, relwidth= 0.3)

new_event_btn = Button(main_game_frame, text ="New Event", command = event_vindaloop)
new_event_btn.place(relx = 0.06092, rely = 0.8, relheight = 0.05, relwidth = 0.24)

store_btn = Button(main_game_frame, text ="Store", command = store)
store_btn.place(relx = 0.695, rely = 0.8, relheight = 0.05, relwidth = 0.24)


# SCROLLBAR AND EVENTS DISPLAYING BOX
scroll_events = Scrollbar(main_game_frame, orient = VERTICAL)
scroll_events.place(relx = 0.8850, rely = 0.23, relheight = 0.54)  # ORIGINAL RELX = 8779, TO STICK IT WITH THE EVENTS TAB

recent_events_tracker = Text(main_game_frame, yscrollcommand = scroll_events.set, font = "tahoma 10", highlightthickness = 5)
recent_events_tracker.place(relx = 0.077, rely = 0.23, relheight = 0.54, relwidth = 0.8)
recent_events_tracker.config(highlightbackground = "#5D6D7E", highlightcolor= "#5D6D7E")
recent_events_tracker.config(state = DISABLED)
scroll_events.config(command = recent_events_tracker.yview)


# MONEY, DAYS AND LIFE COUNTER WIDGETS AND LABELS
money_counter_label = Label(main_game_frame, fg = "black", bg= "white")
money_counter_label.config(text=money_now)
money_counter_label.place(relx=0.11, rely=0.1, relheight = 0.031)

life_counter_label = Label(main_game_frame, fg = "black", bg= "white", font = "David 13")
life_counter_label.config(text = life_counter_now)
life_counter_label.place(relx = 0.9121, rely = 0.075, relheight = 0.03512)

day_label = Label(main_game_frame, text = "Day : ", fg = "black", bg= "white")
day_label.place(relx=0.815, rely=0.129)
day_count_label = Label(main_game_frame, fg = "black", bg= "white")
day_count_label.config(text = day_counter)
day_count_label.place(relx=0.905, rely=0.128)

money_gold_label = Label(main_game_frame, image = money_gold, bg = "white")
money_gold_label.place(relx=0.07, rely=0.101, relheight = 0.031)

life_label = Label(main_game_frame, image = life_bg, bg = "white", borderwidth = 2, relief = SUNKEN)
life_label.place(relx=0.82, rely=0.073)


# SPACESHIP AND CRYOCASKET SLEEP ENDING TRIGGERING BUTTONS
spaceship_install = Button(main_game_frame, image= spaceship, command = spaceship_ending)
cryocasket_install = Button(main_game_frame, image= cryocasket, command = cryocasket_ending)


# QUICK CHARACTER SELECTION WIDGETS, [IN MAIN GAME FRAME]
combobox_string = StringVar()
quickSelect_chara_combobox = ttk.Combobox(main_game_frame, textvariable = combobox_string )
quickSelect_chara_combobox["values"] = ("Vendor",
                                        "Gina",
                                        "Sky")
quickSelect_chara_combobox["state"] = "readonly"
quickSelect_chara_combobox.current()

confirm_quickChara = Button(main_game_frame, text = "Ok", borderwidth = 0, command = quickCharaSel)
quickSelect_chara_combobox.place(relx=0.25, rely=0.085, relheight=0.046, relwidth=0.48)
confirm_quickChara.place(relx=0.44, rely=0.15, relheight=0.036, relwidth=0.095)

root.mainloop()

# END~
# POV: YOU ARE ANGRY AT ME FOR NOT USING OOPS