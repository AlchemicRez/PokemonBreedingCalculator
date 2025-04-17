# Generated with tkedit (tkedit.glitch.me)

import tkinter as tk
from tkinter import *
from tkinter.scrolledtext import *
import random

# Globals
BESTCOLOR = "#17ff00" # the color (GREEN) for a perfect IV
DEFAULTCOLOR = "#F0F8FF"
FAVORITE_FONT = ('courier', 10, 'normal')
CSV_DELIM = ", "
TAB_DELIM = "\t"
gdelim = CSV_DELIM
include_parent_stats = True

def on_load():
    """ as soon as everything is loaded

    intializes the spinboxes with 16 in each stat """
    for mon in mons:
        for stat in mon:
            stat.delete(0,END)
            stat.insert(0,16)
            
def update_spinBoxGeneric(sb):
    """ the spingbox sp has been updated

    this method catches all the parent stat spinboxes

    ARGS: sp - spinbox pointer to the spinbox that was updated"""
    
    recolorSpinbox(sb)
    
def recolorSpinbox(theSpinBox):
    """ checks the value of the spinbox and colors it green if it's MAX

    Also sets include_parent_stats because they have changed in some way"""
    
    global include_parent_stats
    include_parent_stats = True
    if int(theSpinBox.get()) == 31:
        theSpinBox.config(bg=BESTCOLOR)
    else:
        theSpinBox.config(bg=DEFAULTCOLOR)

def btnClickFunction():
    # for i in range(1, 800):
    #     generate1set()
    generate1set()
    
def generate1set():
    """ Generate stats for one child based on the parents stats

    Also includes the parents stats if they have changed since our last generation"""
    
    global include_parent_stats

    # pick the slot that will not be inherited
    stat_to_omit = random.randint(0,5)
    
    child_stats = []

    # run through all 6 stat slots
    for i in range(6):
        if i == stat_to_omit:
            # fill this stat with random value
            child_stats.append(random.randint(0,31))
        else:
            # grab a stat from either parent 1 or parent 2
            selected_parent = random.randint(0,1)
            child_stats.append(
                int( #spinboxes are returning strings -> convert to int
                    mons[selected_parent][i].get() # get stat value from random parent for that slot
                )
            )

    # construct an output string from the child's stats
    outstring = ""
    for stat in child_stats:
        # only insert a delimiter after the first stat
        if len(outstring) > 0:
            outstring = outstring + gdelim

        outstring = outstring + str(stat)

    # if this is the first time generating with this set of parents then include the parent stats
    if include_parent_stats:
        text_area.insert(
            END,
            "Prnt: HP" + gdelim + "AT" + gdelim + "DF" + gdelim + "SA" + gdelim + "SD" + gdelim + "SP\n")
        
        text_area.insert(END,getParentStats(0) + "\n")
        text_area.insert(END,getParentStats(1) + "\n")
        
        text_area.insert(
            END,
            "Chld: HP" + gdelim + "AT" + gdelim + "DF" + gdelim + "SA" + gdelim + "SD" + gdelim + "SP\n")
        # we just included the parents info so don't do it again
        include_parent_stats = False
        
    text_area.insert(END,outstring+"\n")
    text_area.see(tk.END)
  
def getParentStats(p):
    """ returns a string with the stats of the specified parent p

    ARGS: p - an int either 0 or 1 for first or second parent"""
    retStr = ""
    for stat in mons[p]:
        if len(retStr) > 0:
            retStr = retStr + gdelim
        
        retStr = retStr + str(stat.get())
    
    return retStr
    
def btnRNDClickFunction():
    """ Randomizes each stat for each parent.

    Also sets include_parent_stats because they have changed"""
    
    global include_parent_stats
    include_parent_stats = True

    newStat = -1
    for mon in mons:
        for stat in mon:
            stat.delete(0,END)
            newStat = random.randint(0,31)
            stat.insert(0,newStat)
            if newStat == 31:
                stat.config(bg=BESTCOLOR)
            else:
                stat.config(bg=DEFAULTCOLOR)
            

def btnMAXClickFunction():
    """ Maximize each stat for both parents with the best IVs

    Also sets include_parent_stats because they changed in some way"""
    global include_parent_stats
    include_parent_stats = True
    for mon in mons:
        for stat in mon:
            stat.delete(0,END)
            stat.insert(0,31)
            stat.config(bg=BESTCOLOR)

def changeDelim():
    """Observes the chosen delimiter (from a radio button) and sets it appropriately. 

    The chosen delimiter will be reflected in the output window for results that have
    already been generated.  This function will be called every time the user clicks
    the radio button widget and therefore a call might not indicate a change.
    Example: if the user repeatedly clicks the "CSV" option.
    This function checks to make sure the delimiter has changed before
    performing a find/replace on the output window.
    """

    global gdelim
    changed = False
    
    if rbVariable.get() == 0:  #CSV was selected
        if gdelim == TAB_DELIM:
            gdelim = CSV_DELIM
            fulltext = text_area.get("1.0",END).replace(TAB_DELIM,CSV_DELIM)
            changed = True
    else: #TAB was selected
        if gdelim == CSV_DELIM:
            gdelim = TAB_DELIM
            fulltext = text_area.get("1.0",END).replace(CSV_DELIM,TAB_DELIM)
            changed = True
            
    if changed:
        text_area.delete("1.0",END)
        # the previous find/replace seems to insert extra whitespace.  so
        # we'll strip the beginning and end and re-add the \n to the end.
        text_area.insert(END,fulltext.strip() + "\n")
        text_area.see(END)
            
##############################    
root = Tk()

# Declaration of variables associated with the radio button group
rbVariable = tk.IntVar()

root.geometry('300x390')
root.configure(background=DEFAULTCOLOR)
root.title('B Calc')

# i got two parents
mon1 = []
mon2 = []
mons = [mon1,mon2]

# Create a spin box
spinBox1HP = Spinbox(root, from_=0, to=31, font=FAVORITE_FONT,
                     bg = DEFAULTCOLOR, width=4, command = lambda: update_spinBoxGeneric(spinBox1HP))
spinBox1HP.place(x=15, y=30)
mon1.append(spinBox1HP)

# Create a spin box
spinBox1Atk = Spinbox(root, from_=0, to=31, font=FAVORITE_FONT,
                      bg = DEFAULTCOLOR, width=4, command = lambda:  update_spinBoxGeneric(spinBox1Atk))
spinBox1Atk.place(x=15, y=50)
mon1.append(spinBox1Atk)

# Create a spin box
spinBox1Def = Spinbox(root, from_=0, to=31, font=FAVORITE_FONT,
                      bg = DEFAULTCOLOR, width=4, command = lambda: update_spinBoxGeneric(spinBox1Def))
spinBox1Def.place(x=15, y=70)
mon1.append(spinBox1Def)
    
# Create a spin box
spinBox1SpAtk = Spinbox(root, from_=0, to=31, font=FAVORITE_FONT,
                        bg = DEFAULTCOLOR, width=4, command = lambda: update_spinBoxGeneric(spinBox1SpAtk))
spinBox1SpAtk.place(x=15, y=90)
mon1.append(spinBox1SpAtk)
    
# Create a spin box
spinBox1SpDef = Spinbox(root, from_=0, to=31, font=FAVORITE_FONT,
                        bg = DEFAULTCOLOR, width=4, command = lambda: update_spinBoxGeneric(spinBox1SpDef))
spinBox1SpDef.place(x=15, y=110)
mon1.append(spinBox1SpDef)
    
# Create a spin box
spinBox1Spd = Spinbox(root, from_=0, to=31, font=FAVORITE_FONT,
                      bg = DEFAULTCOLOR, width=4, command = lambda: update_spinBoxGeneric(spinBox1Spd))
spinBox1Spd.place(x=15, y=130)
mon1.append(spinBox1Spd)
    
################

# Create a spin box
spinBox2HP = Spinbox(root, from_=0, to=31, font=FAVORITE_FONT,
                     bg = DEFAULTCOLOR, width=4, command = lambda: update_spinBoxGeneric(spinBox2HP))
spinBox2HP.place(x=85, y=30)
mon2.append(spinBox2HP)

# Create a spin box
spinBox2Atk = Spinbox(root, from_=0, to=31, font=FAVORITE_FONT,
                      bg = DEFAULTCOLOR, width=4, command = lambda: update_spinBoxGeneric(spinBox2Atk))
spinBox2Atk.place(x=85, y=50)
mon2.append(spinBox2Atk)
    
# Create a spin box
spinBox2Def = Spinbox(root, from_=0, to=31, font=FAVORITE_FONT,
                      bg = DEFAULTCOLOR, width=4, command = lambda: update_spinBoxGeneric(spinBox2Def))
spinBox2Def.place(x=85, y=70)
mon2.append(spinBox2Def)
    
# Create a spin box
spinBox2SpAtk = Spinbox(root, from_=0, to=31, font=FAVORITE_FONT,
                        bg = DEFAULTCOLOR, width=4, command = lambda: update_spinBoxGeneric(spinBox2SpAtk))
spinBox2SpAtk.place(x=85, y=90)
mon2.append(spinBox2SpAtk)
    
# Create a spin box
spinBox2SpDef = Spinbox(root, from_=0, to=31, font=FAVORITE_FONT,
                        bg = DEFAULTCOLOR, width=4, command = lambda: update_spinBoxGeneric(spinBox2SpDef))
spinBox2SpDef.place(x=85, y=110)
mon2.append(spinBox2SpDef)
    
# Create a spin box
spinBox2Spd = Spinbox(root, from_=0, to=31, font=FAVORITE_FONT,
                      bg = DEFAULTCOLOR, width=4, command = lambda: update_spinBoxGeneric(spinBox2Spd))
spinBox2Spd.place(x=85, y=130)
mon2.append(spinBox2Spd)
    
# Create a button
Button(root, text='GEN', bg=DEFAULTCOLOR, font=FAVORITE_FONT, command=btnClickFunction).place(x=190, y=30)

Button(root, text="RND", bg=DEFAULTCOLOR, font=FAVORITE_FONT, command=btnRNDClickFunction).place(x=150, y=30)

Button(root, text="MAX", bg=DEFAULTCOLOR, font=FAVORITE_FONT, command=btnMAXClickFunction).place(x=150, y=62)

# Create a group of radio buttons
frame=Frame(root, width=0, height=0, bg=DEFAULTCOLOR)
frame.place(x=15, y=2)
ARBEES=[
('CSV', '0'), 
('TAB', '1'), 
]
for text, mode in ARBEES:
    rbGroupOne=Radiobutton(frame, text=text, variable=rbVariable, value=mode, bg=DEFAULTCOLOR, font=FAVORITE_FONT, command=changeDelim ).pack(side='left', anchor = 'w')

txtFrame = Frame(root, bg='#FFFFFF')
txtFrame.place(x=15, y=190)

text_area = ScrolledText(txtFrame, wrap="word", width=30, height=10)
text_area.pack(fill="both", expand=True, padx=5, pady=5)

on_load()

# do i need this update?
root.update()

root.mainloop()
        
