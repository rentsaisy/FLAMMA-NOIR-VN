# default persistent.scene1_completed = False
# default persistent.scene2_completed = False
# default persistent.scene3_completed = False
# default persistent.scene4_completed = False

# label scene1:

#     # isi Scene 1 kamu di sini

#     $ persistent.scene1_completed = True

#     return

# label scene2:

#     # isi Scene 2 kamu di sini

#     $ persistent.scene2_completed = True

# #     return

transform shake:
    xoffset 0
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset -8
    linear 0.05 xoffset 8
    linear 0.05 xoffset -5
    linear 0.05 xoffset 0
 
label tutorial_battle:
    jump tutorial

# SCENE 1
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define Katerine = Character('Katerine', color="#ffffff")  #MC
define Sonya = Character('Sonya', color="#80b9c8") #lead investigator
define Ivan = Character('Ivan', color="#247d7f") # field investigator
define Alexei = Character('Alexei', color="#b2d9c4") # technical investigator
define Oscar = Character('Oscar', color="#900000") # the burner

# Scenes pic
    #SCENE 1
image sonya = "images/C_Lead_Investigator.png"
image katerine = "images/C_Main_Character.png"
image ivan = "images/C_Field_Investigator.png"
image alexei = "images/C_Technical_Investigator.png"
image oscar = "images/V_The_Burner.png"
image BF = "images/BG_forest_Before.png"
image AF = "images/BG_forest_After.png"
image BGO = "images/BG_office.png"
image S1_1 = "images/S1_1.png"
image S1_2 = "images/S1_2.png"
image S1_3 = "images/S1_3.png"
image S1_4 = "images/S1_4.png"
image S1_5 = "images/S1_5.png"
image S1_6 = "images/S1_6.png"
image S1_7 = "images/S1_7.png"

# The game starts here.
label scene_1:
    scene BF
    pause 2.0
    scene S1_1
    pause 2.0
    scene S1_2
    pause 1.5
    scene S1_3
    pause 2.0
    scene S1_4
    "The flames spread, consuming her house."
    scene S1_5
    pause 1.5
    scene S1_6
    "The fire grows stronger, devouring everything in its path."
    scene black
    pause 2.0
    scene BGO
    show sonya:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Sonya "This is our new member."
    show katerine:
        xalign 0.8
        yalign 0.1
        zoom 0.256
    Katerine "Hello, everyone. My name is Katerine, I am the new lawyer."
    hide katerine
    Sonya "Alright. Let us introduce ourselves. First, I am the Lead Investigator, responsible for coordinating our investigations."
    hide sonya
    show ivan:
        xalign 0.5
        yalign 0.3
        zoom 0.232
    Ivan "I am the Field Investigator. I handle investigations and evidence directly at the crime scene."
    hide ivan
    show alexei:
        xalign 0.5
        yalign 0.3
        zoom 0.232
    Alexei "I am the Technical Investigator. I analyze technical evidence and help uncover hidden information."
    hide alexei
    scene black
    "Suddenly, a new case comes in."
    scene BGO
    show sonya:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Sonya "Looks like this is your first case."
    hide sonya
    show katerine:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Katerine "Forest arson?"
    show sonya:
        xalign 0.1
        yalign 0.1
        zoom 0.256
    Sonya "Exactly. Find the real culprit at the crime scene. You will be going with Ivan."
    show ivan:
        xalign 0.9
        yalign 0.3
        zoom 0.232
    Ivan "Huh, Me?"
    Sonya "Yup, Tell me what you guys find after that."
    hide katerine
    hide sonya
    hide ivan
    with dissolve
    scene black
    pause 2.0
    scene AF
    "The firefighters have already left. The forest is quiet, but the smell of smoke still lingers in the air."
    show katerine:
        xalign 0.1
        yalign 0.1
        zoom 0.256
    Katerine "This forest is huge..."
    hide katerine
    scene S1_7
    "Katerine notices something lying among the ashes."
    Katerine "A burned fox..."
    scene AF
    show katerine:
        xalign 0.1
        yalign 0.1
        zoom 0.256
    Katerine "Who could do something this cruel?"
    show ivan:
        xalign 0.8
        yalign 0.3
        zoom 0.232
    Ivan "Do not jump to conclusions. Look around first."
    hide katerine
    hide ivan
    with dissolve
    "They examine the area but finds nothing useful."
    show AF at shake
    "CRACK!"
    show katerine:
        xalign 0.1
        yalign 0.1
        zoom 0.256
    Katerine "Someone is here?!"
    hide katerine
    "A figure emerges from the smoke."
    show oscar:
        xalign 1.0
        yalign 0.3
        zoom 0.232
    Oscar "You should not come here."
    show katerine:
            xalign 0.1
            yalign 0.1
            zoom 0.256
    Katerine "Why are you running from us?"
    Oscar "Who is gonna run, huh?"
    #fix size ivan
    show ivan:
            xalign 0.4
            yalign 0.3
            zoom 0.232
    Ivan "You, You are coming with us."
    return

label scene_2:
    "The flames spread, consuming his house. The fire grows stronger, devouring everything in its path."
    # "This is our newest member."
    Sonya "This is our newest member."
    Katerine "Hello, everyone. I’m the new lawyer."
    Sonya "Alright. Let’s introduce ourselves. I’m the Lead Investigator, responsible for coordinating our investigations."
    Ivan "I’m the Field Investigator. I handle investigations and evidence directly at the crime scene."
    Alexei "I’m the Technical Investigator. I analyze technical evidence and help uncover hidden information."
    "Suddenly, a new case comes in."
    Sonya "Looks like this is your first case."
    Katerine "Forest arson?"
    return

label scene_3:
    "The flames spread, consuming his house. The fire grows stronger, devouring everything in its path."
    # "This is our newest member."
    Sonya "This is our newest member."
    Katerine "Hello, everyone. I’m the new lawyer."
    Sonya "Alright. Let’s introduce ourselves. I’m the Lead Investigator, responsible for coordinating our investigations."
    Ivan "I’m the Field Investigator. I handle investigations and evidence directly at the crime scene."
    Alexei "I’m the Technical Investigator. I analyze technical evidence and help uncover hidden information."
    "Suddenly, a new case comes in."
    Sonya "Looks like this is your first case."
    Katerine "Forest arson?"
    return

label scene_4:
    "The flames spread, consuming his house. The fire grows stronger, devouring everything in its path."
    # "This is our newest member."
    Sonya "This is our newest member."
    Katerine "Hello, everyone. I’m the new lawyer."
    Sonya "Alright. Let’s introduce ourselves. I’m the Lead Investigator, responsible for coordinating our investigations."
    Ivan "I’m the Field Investigator. I handle investigations and evidence directly at the crime scene."
    Alexei "I’m the Technical Investigator. I analyze technical evidence and help uncover hidden information."
    "Suddenly, a new case comes in."
    Sonya "Looks like this is your first case."
    Katerine "Forest arson?"
    return


label start:
    return

label dialogBB:
    Sonya "Exactly. Find the real culprit at the crime scene. You’ll be going with the Field Investigator."
    Sonya "Tell me what you find when you’re done."
    "The firefighters have already left. The forest is quiet, but the smell of smoke still lingers in the air."
    Katerine "This forest is huge…"
    "Katerine notices something lying among the ashes."
    Katerine "A burned fox…"
    Katerine "Who could do something this cruel?"
    Ivan "Don't jump to conclusions. Look around first."
    "They examine the area but finds nothing useful."
    "CRACK!"
    Katerine "Who’s there?!"
    "A figure emerges from the smoke."
    Oscar "You guys shouldn't have come here."
    Katerine "Why are you running from us?"
    Oscar "Who's gonna run, huh?"
    Ivan "You're coming with us."
    return

label dialogAB:
    "The smoke slowly clears and he is gone."
    Ivan "He escaped..."
    Katerine "Forget about him, he left something behind."
    Ivan "Lighter?"
    Katerine "Smell like gasoline.."
    return

    