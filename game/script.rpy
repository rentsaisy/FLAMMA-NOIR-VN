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

#     return
default battle_result = None
default battle_try_again = False
default battle_previous_choice = None
default battle_show_result_popup = False

transform win_cover_animation:
    yoffset -720
    ease 0.8 yoffset 0

transform lose_cover_animation:
    yoffset 720
    ease 0.8 yoffset 0
    
init python:

    def battle_choose(argument_type):

        # Do not accept choices after the battle ends.
        if store.battle_result is not None:
            return

        enemy_type = store.battle_enemy_arguments[
            store.battle_phase
        ]["type"]

        counters = {
            "Forensics": "Integrity",
            "Integrity": "Intelligence",
            "Intelligence": "Forensics"
        }

        # Same argument type: ask the player to try again.
        if argument_type == enemy_type:
            store.battle_try_again = True
            renpy.show_screen("battle_try_again_screen")
            renpy.restart_interaction()
            return

        store.battle_try_again = False

        # Player wins this exchange.
        if counters.get(argument_type) == enemy_type:
            store.battle_enemy_hp -= 50

            if store.battle_enemy_hp <= 0:
                store.battle_enemy_hp = 0
                store.battle_result = "win"
                store.battle_show_result_popup = False
                renpy.show_screen("battle_result_screen")
                renpy.restart_interaction()
                return

        # Player loses this exchange.
        elif counters.get(enemy_type) == argument_type:
            store.battle_mc_lives -= 1

            if store.battle_mc_lives <= 0:
                store.battle_mc_lives = 0
                store.battle_result = "lose"
                store.battle_show_result_popup = False
                renpy.show_screen("battle_result_screen")
                renpy.restart_interaction()
                return

        renpy.restart_interaction()

screen battle_result_screen():

    modal True
    zorder 200

    if battle_result == "win":

        add Solid("#000000") at win_cover_animation

    elif battle_result == "lose":

        add Solid("#000000") at lose_cover_animation

    # Show the result popup after the cover animation.
    if not battle_show_result_popup:
        timer 0.9 action SetVariable(
            "battle_show_result_popup", True
        )
    if battle_show_result_popup:

        frame:
            add "gui/overlay/confirm.png"
            xalign 0.5
            yalign 0.5
            xsize 500
            ysize 300
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 30

                if battle_result == "win":
                    text "YOU WIN":
                        size 48
                        color "#FFFDFD"
                        xalign 0.5

                    text "You defeated your opponent.":
                        color "#FFFFFF"
                        xalign 0.5

                else:
                    text "YOU LOSE":
                        size 48
                        color "#360618"
                        xalign 0.5

                    text "You have run out of lives.":
                        color "#FFFFFF"
                        xalign 0.5

                textbutton "Continue":
                    xalign 0.5
                    action Return(battle_result)
                    
screen battle_try_again_screen():

    modal True
    zorder 300

    # Transparent dark overlay.
    add Solid("#00000066")

    # Character.
    add "fox":
        xalign 1.0
        yalign 1.0
        zoom 0.256

    # Dialogue bubble.
    frame:
        add "gui/overlay/confirm.png"
        xalign 0.5
        yalign 0.82
        xsize 300
        ysize 120

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 12

            text "Try again!":
                size 30
                color "#FFF7F7"
                xalign 0.5

            textbutton "OK":
                xalign 0.5
                action Hide("battle_try_again_screen")
                
default battle_phase = 0

screen battle_screen():

    add battle_background


    # =========================================
    # ENEMY
    # =========================================

    add battle_enemy_image:
        xpos 850
        ypos 280
        xanchor 0.5
        yanchor 0.5
        zoom 0.236


    # =========================================
    # ENEMY ARGUMENT BUBBLE
    # =========================================

    frame:
        xpos 300
        ypos 140
        xsize 500
        ysize 150

        background battle_enemy_bubble

        text battle_enemy_arguments[battle_phase]["text"]:
            xalign 0.1
            yalign 0.5
            xmaximum 430
            text_align 0.5
            size 25
            color "#ffffff"


    # =========================================
    # ENEMY HP
    # =========================================

    bar:
        xpos 0
        ypos 470
        xsize 1280
        ysize 38

        value battle_enemy_hp
        range battle_enemy_max_hp

        left_bar Solid("#000000")
        right_bar Solid("#F3EEEE")


    # =========================================
    # MC LIVES
    # =========================================

    if battle_mc_lives >= 1:
        text "♥":
            xpos 1080
            ypos 30
            size 40
            color "#ff4d6d"

    if battle_mc_lives >= 2:
        text "♥":
            xpos 1140
            ypos 30
            size 40
            color "#ff4d6d"

    if battle_mc_lives >= 3:
        text "♥":
            xpos 1200
            ypos 30
            size 40
            color "#ff4d6d"


    # =========================================
    # PLAYER ARGUMENTS
    # =========================================
    # PLAYER ARGUMENTS BACKGROUND FRAME
    fixed:
        xpos 120
        ypos 550
        xsize 1160
        ysize 130

        # One black transparent frame for all 3 bubbles.
        frame:
            xpos -120
            ypos -45
            xsize 1280
            ysize 400
            background "#000000B8"
    for i, argument in enumerate(battle_player_arguments):

        textbutton argument["text"]:

            xpos 80 + (i * 390)
            ypos 560

            xsize 350
            ysize 110

            background battle_player_bubble[i]
            hover_background battle_player_bubble_hover[i]
            text_xalign 0.5
            text_yalign 0.5

            text_xmaximum 300
            text_size 16
            text_color "#ffffff"

            action Function(
                battle_choose,
                argument["type"]
            )
            
label battle(
    enemy_name,
    enemy_image,
    enemy_arguments,
    player_arguments,
    background,
    enemy_bubble,
    player_bubbles,
    player_bubbles_hover,
    enemy_hp,
    phase,
    mc_lives,
    enemy_max_hp
):

    $ battle_enemy_name = enemy_name
    $ battle_enemy_image = enemy_image
    $ battle_enemy_arguments = enemy_arguments
    $ battle_player_arguments = player_arguments
    $ battle_background = background
    $ battle_enemy_bubble = enemy_bubble
    $ battle_player_bubble = player_bubbles
    $ battle_player_bubble_hover = player_bubbles_hover

    # Save the initial battle settings.
    $ battle_initial_hp = enemy_hp
    $ battle_initial_phase = phase
    $ battle_initial_lives = mc_lives
    $ battle_enemy_max_hp = enemy_max_hp

    # Repeat battle until the player wins.
    while True:

        $ battle_enemy_hp = battle_initial_hp
        $ battle_phase = battle_initial_phase
        $ battle_mc_lives = battle_initial_lives

        $ battle_result = None
        $ battle_try_again = False
        $ battle_show_result_popup = False

        call screen battle_screen

        # Show the result screen when the battle ends.
        if battle_result == "win" or battle_result == "lose":

            call screen battle_result_screen
            $ result = _return

            if result == "win":
                return "win"

            elif result == "lose":
                # Restart the battle with initial HP and lives.
                pass
                
transform shake:
    xoffset 0
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset -8
    linear 0.05 xoffset 8
    linear 0.05 xoffset -5
    linear 0.05 xoffset 0


# SCENE BATTLE TUTORIAL
define Fox = Character('Little Fox', color="#ec7599")  #PINK
image fox = "images/C_Fox.png"
image foren = "images/EForensic.png"
image intel = "images/EIntelligence.png"
image integ = "images/EIntegrity.png"

transform move_forensics:
    xpos 300
    ypos 300
    xanchor 0.5
    yanchor 0.5
    zoom 0.1

    pause 1.5
    linear 1.0 xpos 640 ypos 150


transform move_intelligence:
    xpos 640
    ypos 300
    xanchor 0.5
    yanchor 0.5
    zoom 0.1

    pause 1.5
    linear 1.0 xpos 420 ypos 400


transform move_integrity:
    xpos 980
    ypos 300
    xanchor 0.5
    yanchor 0.5
    zoom 0.1

    pause 1.5
    linear 1.0 xpos 860 ypos 400
 
label tutorial_battle:
    scene black
    show fox:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Fox "Welcome to the Battle Tutorial."
    Fox "Let me introduce you to our argument types."
    hide fox 
    show foren at move_forensics
    Fox "Forensic"
    show intel at move_intelligence
    Fox "Intelligence"
    show integ at move_integrity
    Fox "Integrity"
    Fox "Forensics is strong against Integrity, Integrity is strong against Intelligence, And Intelligence is strong against Forensics."
    show fox:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Fox "In this battle, you will use arguments to defeat your opponent."
    Fox "Each argument has a type and can counter another type like in the explaination before."
    Fox "Let's begin."
    hide fox
    hide foren
    hide intel
    hide integ
    with dissolve

    $ result = renpy.call("battle",
        enemy_name="Enemy",
        enemy_image="images/enemy.png",
        enemy_hp=50,
        enemy_max_hp=50,
        phase=0,
        mc_lives=3,
        enemy_arguments=[
            {
                "text": "Kebakaran ini bukan urusanmu.",
                "type": "Integrity"
            }
        ],
        player_arguments=[
            {
                "text": "Bukti di lokasi kejadian menunjukkan sebaliknya.",
                "type": "Forensics"
            },
            {
                "text": "Tindakanmu telah menghancurkan kehidupan\nbanyak orang.",
                "type": "Integrity"
            },
            {
                "text": "Aku sudah mengetahui rencanamu sejak awal.",
                "type": "Intelligence"
            }
        ],
        background="images/bgbattle.png",
        enemy_bubble="images/Ben_integ.png",
        player_bubbles=[
            "images/B_foren.png",
            "images/B_integ.png",
            "images/B_intel.png"
        ],
        player_bubbles_hover=[
            "images/Bhov_foren.png",
            "images/Bhov_integ.png",
            "images/Bhov_intel.png"
        ]
    )

    if _return == "win":
        show fox:
            xalign 0.5
            yalign 0.1
            zoom 0.256

        Fox "Tutorial complete."

    return
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

    