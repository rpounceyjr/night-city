import random
from tkinter import *
from PIL import ImageTk, Image
#create root widget
root = Tk()
#background color
root.configure(background = 'black')
#sets root widget size
root.geometry('365x1020')
#creates a title label
root.title("Cyberpunk 2020 NPC Creator")
#sets path for image
path = "/Users/rogerpouncey/Desktop/coding/cyberpunk/cyberpunk_image.png"
#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = Label(image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.grid(row= 0, column = 3)

#create label widget
#my_label = Label(root, text = "Cyberpunk 2020 NPC Creator", bg= 'black', fg= 'chartreuse')
#place label widget in root widget
#my_label.grid(row= 1, column = 3)



#create name generator
first_names = ['Kyle', 'Chemtrail', 'Petra', 'Mack']
last_names = ['13', 'Jones', 'The Fork', 'Pain']

def name_generator():
    name = random.choice(first_names) + ' ' + random.choice(last_names)
    #THIS IS HOW YOU POPULATE ENTRY FIELDS!
    name_entry.delete(0, END)
    name_entry.insert(0,name)



#create name entry field
name_entry = Entry(root, width = 20, borderwidth= 5, bg = 'black', fg ='chartreuse')
name_entry.grid(row= 2, column = 3, pady = 10)
name_entry.delete(0, END)
name_entry.insert(0, "Enter Your Name")

#name button
name_button = Button(root, text = "OR Generate a Name", highlightbackground= 'black', foreground= 'chartreuse', command= name_generator)
name_button.grid(row= 3, column = 3)

#dropdown menu
#This is a tkvariable
clicked = StringVar()
clicked.set('Choose Your Role')
role_options = ['Rockerboy', 'Solo', 'Netrunner', 'Techie', 'Medtechie', 'Media', 'Cop', 'Corporate', 'Fixer', 'Nomad']
#have to put a * in front of role_options because using list
drop = OptionMenu(root, clicked, *role_options)
drop.grid(row= 4, column = 3)  
drop.configure(background = 'black', foreground = 'chartreuse', width = 20)

#int entry
int_entry = Entry(root, width = 20, borderwidth= 5, bg = 'black', fg ='chartreuse')
int_entry.grid(row= 5, column = 3)
int_entry.insert(0, "Enter Int Stat")
#int button
def get_int():
    intelligence = random.randint(1,10)
    int_entry.delete(0, END)
    int_entry.insert(0, intelligence)

int_button = Button(root, text = "OR Generate Int Stat", highlightbackground= 'black', foreground= 'chartreuse', command= get_int)

int_button.grid(row= 7, column = 3)

#ref entry
ref_entry = Entry(root, width = 20, borderwidth= 5, bg = 'black', fg ='chartreuse')
ref_entry.grid(row= 8, column = 3)
ref_entry.insert(0, "Enter Ref Stat")
#ref button
def get_ref():
    reflex = random.randint(1,10)
    ref_entry.delete(0, END)
    ref_entry.insert(0, reflex)

ref_button = Button(root, text = "OR Generate Ref Stat", highlightbackground= 'black', foreground= 'chartreuse', command= get_ref)
ref_button.grid(row= 10, column = 3)
#tech entry
tech_entry = Entry(root, width = 20, borderwidth= 5, bg = 'black', fg ='chartreuse')
tech_entry.grid(row= 11, column = 3)
tech_entry.insert(0, "Enter Tech Stat")
#tech button
def get_tech():
    tech = random.randint(1,10)
    tech_entry.delete(0, END)
    tech_entry.insert(0, tech)

tech_button = Button(root, text = "OR Generate Tech Stat", highlightbackground= 'black', foreground= 'chartreuse', command= get_tech)

tech_button.grid(row= 13, column = 3)
#cool entry
cool_entry = Entry(root, width = 20, borderwidth= 5, bg = 'black', fg ='chartreuse')
cool_entry.grid(row= 14, column = 3)
cool_entry.insert(0, "Enter Cool Stat")
#cool button
def get_cool():
    cool = random.randint(1,10)
    cool_entry.delete(0, END)
    cool_entry.insert(0, cool)
cool_button = Button(root, text = "OR Generate Cool Stat", highlightbackground= 'black', foreground= 'chartreuse', command= get_cool)

cool_button.grid(row= 16, column = 3)
#attr entry 
attr_entry = Entry(root, width = 20, borderwidth= 5, bg = 'black', fg ='chartreuse')
attr_entry.grid(row= 17, column = 3)
attr_entry.insert(0, "Enter Attr Stat")
#attr button
def get_attr():
    attr = random.randint(1,10)
    attr_entry.delete(0, END)
    attr_entry.insert(0, attr)
attr_button = Button(root, text = "OR Generate Attr Stat", highlightbackground= 'black', foreground= 'chartreuse', command= get_attr)

attr_button.grid(row= 19, column = 3)
#luck entry
luck_entry = Entry(root, width = 20, borderwidth= 5, bg = 'black', fg ='chartreuse')
luck_entry.grid(row= 20, column = 3)
luck_entry.insert(0, "Enter Luck Stat")
#luck button
def get_luck():
    luck = random.randint(1,10)
    luck_entry.delete(0, END)
    luck_entry.insert(0, luck)
luck_button = Button(root, text = "OR Generate Luck Stat", highlightbackground= 'black', foreground= 'chartreuse', command= get_luck)

luck_button.grid(row= 22, column = 3)
#ma entry
ma_entry = Entry(root, width = 20, borderwidth= 5, bg = 'black', fg ='chartreuse')
ma_entry.grid(row= 23, column = 3)
ma_entry.insert(0, "Enter MA Stat")
#ma button
def get_ma():
    ma = random.randint(1,10)
    ma_entry.delete(0, END)
    ma_entry.insert(0, ma)
ma_button = Button(root, text = "OR Generate MA Stat", highlightbackground= 'black', foreground= 'chartreuse', command= get_ma)

ma_button.grid(row= 25, column = 3)
#body entry
body_entry = Entry(root, width = 20, borderwidth= 5, bg = 'black', fg ='chartreuse')
body_entry.grid(row= 26, column = 3)
body_entry.insert(0, "Enter Body Stat")
#body button
def get_body():
    body = random.randint(1,10)
    body_entry.delete(0, END)
    body_entry.insert(0, body)
body_button = Button(root, text = "OR Generate Body Stat", highlightbackground= 'black', foreground= 'chartreuse', command= get_body)

body_button.grid(row= 28, column = 3)

#function to generate all stats
def get_all():
    return get_int(), get_ref(), get_tech(), get_cool(), get_attr(), get_body(), get_luck(), get_ma() 

#button to generate all stats

all_stats_button = Button(root, text = "OR GENERATE ALL STATS", command= get_all, highlightbackground = 'black', foreground = 'chartreuse', width = 20)
all_stats_button.grid(row= 29, column= 3)
#get cyberware
def get_cyberware():
    cyber_roll = random.randint(1,10)
    cyberwarez = ''
    if cyber_roll == 1:
        another_roll = random.randint(1,6)
        if another_roll == 1:
            cyberwarez = 'Infrared'
            cyberware_entry.delete(0, END)
            cyberware_entry.insert(0, cyberwarez)
        elif another_roll == 2:
            cyberwarez = 'Lowlight'
            cyberware_entry.delete(0, END)
            cyberware_entry.insert(0, cyberwarez)
        elif another_roll == 3:
            cyberwarez = 'Camera'
            cyberware_entry.delete(0, END)
            cyberware_entry.insert(0, cyberwarez)
        elif another_roll == 4:
            cyberwarez = 'Dartgun'
            cyberware_entry.delete(0, END)
            cyberware_entry.insert(0, cyberwarez)
        elif another_roll == 5:
            cyberwarez = 'Antidazzle'
            cyberware_entry.delete(0, END)
            cyberware_entry.insert(0, cyberwarez)
        else:
            cyberwarez = 'Targeting Scope'
            cyberware_entry.delete(0, END)
            cyberware_entry.insert(0, cyberwarez)
    elif cyber_roll == 2:
        yet_another_roll = random.randint(1,6)
        cyberware_entry.insert(0, cyberwarez)
        if yet_another_roll == 1:
            cyberwarez = 'Medium Pistol'
            cyberware_entry.delete(0, END)
            cyberware_entry.insert(0, cyberwarez)
        elif yet_another_roll == 2:
            cyberwarez = 'Light Pistol'
            cyberware_entry.delete(0, END)
            cyberware_entry.insert(0, cyberwarez)
        elif yet_another_roll == 3:
            cyberwarez = 'Medium Pistol'
            cyberware_entry.delete(0, END)
            cyberware_entry.insert(0, cyberwarez)
        elif yet_another_roll == 4:
            cyberwarez = 'Light Submachine Gun'
            cyberware_entry.delete(0, END)
            cyberware_entry.insert(0, cyberwarez)
        elif yet_another_roll == 5:
            cyberwarez = 'Very Heavy Pistol' 
            cyberware_entry.delete(0, END)
            cyberware_entry.insert(0, cyberwarez)
        else:
            cyberwarez = 'Heavy Pistol'
            cyberware_entry.delete(0, END)
            cyberware_entry.insert(0, cyberwarez)
    elif cyber_roll == 3:
        rolling_again = random.randint(1,6)
        if rolling_again == 1:
            cyberwarez = 'Wearman'
            cyberware_entry.delete(0, END)
            cyberware_entry.insert(0, cyberwarez)
        elif rolling_again == 2:
            cyberwarez = 'Radio Splice'
            cyberware_entry.delete(0, END)
            cyberware_entry.insert(0, cyberwarez)
        elif rolling_again == 3:
            cyberwarez = 'Phone Link'
            cyberware_entry.delete(0, END)
            cyberware_entry.insert(0, cyberwarez)
        elif rolling_again == 4:
            cyberwarez = 'Amplified Hearing'
            cyberware_entry.delete(0, END)
            cyberware_entry.insert(0, cyberwarez)
        elif rolling_again == 5:
            cyberwarez = 'Sound Editing'
            cyberware_entry.delete(0, END)
            cyberware_entry.insert(0, cyberwarez)
        else:
            cyberwarez = 'Digital Recording Link'
            cyberware_entry.delete(0, END)
            cyberware_entry.insert(0, cyberwarez)
    elif cyber_roll == 4:
        cyberwarez = 'Big Knucks'
        cyberware_entry.delete(0, END)
        cyberware_entry.insert(0, cyberwarez)
    elif cyber_roll == 5:
        cyberwarez = 'Rippers'
        cyberware_entry.delete(0, END)
        cyberware_entry.insert(0, cyberwarez)
    elif cyber_roll == 6:
        cyberwarez = 'Vampires'
        cyberware_entry.delete(0, END)
        cyberware_entry.insert(0, cyberwarez)
    elif cyber_roll == 7:
        cyberwarez = "Slice 'n' dice"
        cyberware_entry.delete(0, END)
        cyberware_entry.insert(0, cyberwarez)
    elif cyber_roll == 8:
        cyberwarez = 'Reflex Boost (Kerenzikov)'
        cyberware_entry.delete(0, END)
        cyberware_entry.insert(0, cyberwarez)
    elif cyber_roll == 9:
        cyberwarez = 'Reflex Boost (Sandevistan)'
        cyberware_entry.delete(0, END)
        cyberware_entry.insert(0, cyberwarez)
    else:
        cyberwarez ='Nothing'
        cyberware_entry.delete(0, END)
        cyberware_entry.insert(0, cyberwarez)
        

#cyberware entry field 
cyberware_entry = Entry(root, width = 20, borderwidth= 5, bg = 'black', fg ='chartreuse')
cyberware_entry.grid(row = 30, column = 3)
cyberware_entry.delete(0, END)
cyberware_entry.insert(0, "Enter Cyberware")
#cyberware button
cyberware_button = Button(root, text = "OR Generate Cyberware", command = get_cyberware, highlightbackground = 'black', foreground = 'chartreuse')
cyberware_button.grid(row = 31, column = 3)
#input skillz
#skillz
skillz = Entry(root, width = 20, borderwidth= 5, bg = 'black', fg ='chartreuse')
skillz.grid(row= 32, column = 3)
skillz.delete(0, END)
skillz.insert(0, "Enter Your Skills")


#creates event loop

root.mainloop()