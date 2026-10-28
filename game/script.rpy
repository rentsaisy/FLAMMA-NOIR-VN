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
image investigation_room_tutor:
    "images/TGF/tgidle.png"
    pause 0.5
    "images/TGF/tgidle1.png"
    pause 0.5
    repeat
    
# Idle animation
image player_idle:
    "images/MC/mcidle.png"
    pause 0.15
    "images/MC/mcidle1.png"
    pause 0.15
    repeat
    
# Walking down (S)
image player_walk_down:
    "images/MC/mcnetral.png"
    pause 0.15
    "images/MC/mcblink.png"
    pause 0.15
    "images/MC/mcnetral1.png"
    pause 0.15
    "images/MC/mcblink1.png"
    repeat

# Walking up (W)
image player_walk_up:
    "images/MC/mcback.png"
    pause 0.15
    "images/MC/mcback2.png"
    pause 0.15
    "images/MC/mcback1.png"
    pause 0.15
    repeat

# Walking left (A)
image player_walk_left:
    "images/MC/mcleft.png"
    pause 0.15
    "images/MC/mcleft1.png"
    pause 0.15
    repeat

# Walking right (D)
image player_walk_right:
    "images/MC/mcright.png"
    pause 0.15
    "images/MC/mcright1.png"
    pause 0.15
    repeat

# Sitting while thinking
image fight_tg:
    "images/TGF/tgfight.png"
    pause 0.7
    "images/TGF/tgfight1.png"
    pause 0.7
    "images/TGF/tgfight2.png"
    pause 0.7
    repeat
        
# tg lose
image lose_tg:
    "images/TGF/tglose.png"
    pause 0.7
    "images/TGF/tglose1.png"
    pause 0.7
    repeat
    
# tg win
image win_tg:
    "images/TGF/tgwin.png"
    pause 0.7
    "images/TGF/tgwin1.png"
    pause 0.7
    "images/TGF/tgwin2.png"
    pause 0.7
    repeat
    
default player_x = 700
default player_y = 500
default player_sitting = False
default evidence_found = False
default evidence_open = False
default player_direction = "down"
default PLAYER_SPEED = 20
define INTERACTION_RADIUS = 50

define COMPUTER_X = 780
define COMPUTER_Y = 390
define CHAIR_X = 1250
define CHAIR_Y = 410


# ===== COMBAT SYSTEM =====
default combat_total_rounds = 1
default combat_hearts = 3
default enemy_type = "forensic"
default combat_state = "playing"
default combat_message = ""
default combat_round = 0

# Enemy question
default enemy_question = "What evidence reveals the truth?"

init python:

    # Type cycle:
    # Forensic < Integrity
    # Integrity < Intelligence
    # Intelligence < Forensic

    def start_combat():
        store.player_sitting = True
        store.combat_hearts = 3
        store.enemy_type = "forensic"
        store.combat_state = "playing"
        store.combat_message = ""
        store.combat_round = 0

    def toggle_sit():
        if store.player_sitting:
            store.player_sitting = False
            store.combat_state = "playing"
            store.combat_message = ""
        else:
            start_combat()
    
    def answer_type(choice):

        if store.combat_state != "playing":
            return

        enemy = store.enemy_type

        # Same type: retry without losing a heart
        if choice == enemy:
            store.combat_message = "Same type! Try another answer."
            store.combat_state = "retry"
            renpy.restart_interaction()
            return

        winning_type = {
            "forensic": "integrity",
            "integrity": "intelligence",
            "intelligence": "forensic"
        }

        # Player wins
        if winning_type[enemy] == choice:
            store.combat_state = "win_anim"

        # Player loses
        else:
            store.combat_hearts = max(0, store.combat_hearts - 1)
            store.combat_state = "lose_anim"

        renpy.restart_interaction()
            
    def finish_win_animation():
        store.combat_state = "game_win"
        renpy.restart_interaction()
        
    def finish_lose_animation():

        if store.combat_hearts <= 0:
            store.combat_state = "game_over"
        else:
            store.combat_state = "playing"
            store.combat_message = ""

    def try_again():
        start_combat()

screen exploration_room_tutorial():

    modal True

    # Background 
    add "investigation_room_tutor"
            
    if player_direction == "up":
        add "player_walk_up":
            xpos player_x
            ypos player_y
            xanchor 0.8
            yanchor 0.5

    elif player_direction == "down":
        add "player_walk_down":
            xpos player_x
            ypos player_y
            xanchor 0.8
            yanchor 0.5

    elif player_direction == "left":
        add "player_walk_left":
            xpos player_x
            ypos player_y
            xanchor 0.8
            yanchor 0.5

    elif player_direction == "right":
        add "player_walk_right":
            xpos player_x
            ypos player_y
            xanchor 0.8
            yanchor 0.5

    # Player Movements
    if not player_sitting and not evidence_open:

        # LEFT - A
        key "K_LEFT" action [
            SetVariable("player_x", max(590, player_x - PLAYER_SPEED)),
            SetVariable("player_direction", "left")
        ]
        key "K_a" action [
            SetVariable("player_x", max(590, player_x - PLAYER_SPEED)),
            SetVariable("player_direction", "left")
        ]

        # RIGHT - D
        key "K_RIGHT" action [
            SetVariable("player_x", min(1600, player_x + PLAYER_SPEED)),
            SetVariable("player_direction", "right")
        ]
        key "K_d" action [
            SetVariable("player_x", min(1600, player_x + PLAYER_SPEED)),
            SetVariable("player_direction", "right")
        ]

        # UP - W
        key "K_UP" action [
            SetVariable("player_y", max(380, player_y - PLAYER_SPEED)),
            SetVariable("player_direction", "up")
        ]
        key "K_w" action [
            SetVariable("player_y", max(380, player_y - PLAYER_SPEED)),
            SetVariable("player_direction", "up")
        ]

        # DOWN - S
        key "K_DOWN" action [
            SetVariable("player_y", min(520, player_y + PLAYER_SPEED)),
            SetVariable("player_direction", "down")
        ]
        key "K_s" action [
            SetVariable("player_y", min(520, player_y + PLAYER_SPEED)),
            SetVariable("player_direction", "down")
        ]

    # ===== ENEMY ANIMATION: DRAW FIRST =====

    if player_sitting:

        if combat_state in ("playing", "retry"):
            add "fight_tg":
                xalign 0.78
                yalign 0.60

        elif combat_state == "win_anim":
            add "lose_tg":
                xalign 0.78
                yalign 0.60

            timer 2.1 action Function(finish_win_animation)

        elif combat_state == "lose_anim":
            add "win_tg":
                xalign 0.78
                yalign 0.60

            timer 2.1 action Function(finish_lose_animation)

   # ===== HEARTS: TOP RIGHT =====
    if player_sitting and combat_state not in ("game_over", "game_win"):

        hbox:
            xalign 0.97
            yalign 0.02
            spacing 5

            for i in range(combat_hearts):
                text "♥":
                    size 40
                    color "#ff405b"             
    # ===== ENEMY QUESTION BUBBLE =====
    if player_sitting and combat_state in ("playing", "retry"):

        frame:
            xpos 500
            ypos 50
            xsize 580
            background "#18212df2"
            xpadding 25
            ypadding 20

            vbox:
                spacing 10

                text "ENEMY":
                    size 18
                    color (
                        "#56aaff" if enemy_type == "forensic"
                        else "#65e68a" if enemy_type == "integrity"
                        else "#ff83cf"
                    )

                text enemy_question:
                    size 26
                    color "#ffffff"

        # ===== THREE CHOICE BUBBLES =====
        vbox:
            xpos 500
            ypos 200
            spacing 15

            textbutton "FORENSIC":
                text_size 20
                text_color "#56aaff"
                background "#18212df2"
                hover_background "#ffffff"
                xpadding 25
                ypadding 12
                action Function(answer_type, "forensic")

            textbutton "INTEGRITY":
                text_size 20
                text_color "#65e68a"
                background "#18212df2"
                hover_background "#ffffffff"
                xpadding 25
                ypadding 12
                action Function(answer_type, "integrity")

            textbutton "INTELLIGENCE":
                text_size 20
                text_color "#ff83cf"
                background "#18212df2"
                hover_background "#ffffff"
                xpadding 25
                ypadding 12
                action Function(answer_type, "intelligence")

    
    # ===== FOX RETRY MESSAGE =====
    if player_sitting and combat_state == "retry":

        add "images/C_Fox.png":
            xalign 0.9
            yalign 1.0
            zoom 0.2

        text combat_message:
            xpos 500
            ypos 670
            size 25
            color "#ffffff"
            
        timer 1.5 action [
            SetVariable("combat_state", "playing"),
            SetVariable("combat_message", "")
        ]
    # ===== GAME OVER SCREEN =====
    if combat_state == "game_over":

        add Solid("#000000")

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 25

            text "LOSE":
                size 65
                color "#ff405b"
                xalign 0.5

            textbutton "TRY AGAIN":
                xalign 0.5
                text_size 28
                action Function(try_again)

            textbutton "HOME":
                xalign 0.5
                text_size 28
                action MainMenu(confirm=False)
                    
    # ===== GAME WIN =====
    if combat_state == "game_win":

        add Solid("#000000")

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 25

            text "WIN":
                size 65
                color "#bbf6f9"
                xalign 0.5

            textbutton "CONTINUE":
                xalign 0.5
                text_size 28
                action MainMenu(confirm=False)
                
    # Interaksi komputer
    if not player_sitting and not evidence_open:

        if (player_x - COMPUTER_X) ** 2 + (player_y - COMPUTER_Y) ** 2 < INTERACTION_RADIUS ** 2:

            textbutton "Inspect ( E )":
                xpos 180
                ypos 270
                text_size 16
                xpadding 8
                ypadding 4
                action SetVariable("evidence_open", True)

            key "e" action SetVariable("evidence_open", True)

    # Interaksi kursi
    if not evidence_open:

        if (player_x - CHAIR_X) ** 2 + (player_y - CHAIR_Y) ** 2 < INTERACTION_RADIUS ** 2:

            textbutton (" " if player_sitting else "Sit Down ( E )"):
                xpos 850
                ypos 300
                text_size 16
                xpadding 8
                ypadding 4
                action Function(toggle_sit)

            key "e" action Function(toggle_sit)
            
    
    if evidence_open:

        frame:
            xalign 0.5
            yalign 0.5
            xsize 900
            ysize 450
            background "#18212df2"
            padding [25, 20]

            vbox:
                spacing 15

                text "INVESTIGATION EVIDENCES" size 25 color "#ffffff"

                hbox:
                    spacing 20

                    # Evidence 1
                    frame:
                        xsize 270
                        ysize 270
                        background "#303d4d"
                        padding [12, 12, 12, 12]

                        vbox:
                            spacing 10

                            add "images/Evi/E.png":
                                xalign 0.5
                                fit "contain"
                                xysize (200, 200)

                            text "Evidence 1" size 18

                    # Evidence 2
                    frame:
                        xsize 270
                        ysize 270
                        background "#303d4d"
                        padding [12, 12, 12, 12]

                        vbox:
                            spacing 10

                            add "images/Evi/E.png":
                                xalign 0.5
                                fit "contain"
                                xysize (200, 200)

                            text "Evidence 2" size 18

                    # Evidence 3
                    frame:
                        xsize 270
                        ysize 270
                        background "#303d4d"
                        padding [12, 12, 12, 12]

                        vbox:
                            spacing 10

                            add "images/Evi/E.png":
                                xalign 0.5
                                fit "contain"
                                xysize (200, 200)

                            text "Evidence 3" size 18

                textbutton "Close":
                    xalign 1.0
                    action SetVariable("evidence_open", False)

    key "K_ESCAPE" action Return()

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
    jump investigation_room_tutorial
    
label investigation_room_tutorial:
    scene black
    "You enter the investigation room."

    call screen exploration_room_tutorial

    "The investigation is complete."

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

    