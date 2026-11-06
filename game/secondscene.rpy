# SCENE 1

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# define Katerine = Character('Katerine', color="#ffffff")  #MC
# define Sonya = Character('Sonya', color="#80b9c8") #lead investigator
# define Ivan = Character('Ivan', color="#247d7f") # field investigator
# define Alexei = Character('Alexei', color="#b2d9c4") # technical investigator
# define Albert = Character('Albert', color="#900000") # the briber
# define Fox = Character('Little Fox', color="#ec7599")  #PINK
# Scenes pic
image sonya = "images/chara/C_Lead_Investigator.png"
image m_sonya = "images/chara/C_Lead_Investigator_Mute.png"
image katerine = "images/chara/C_Main_Character.png"
image m_katerine = "images/chara/C_Main_Character_Mute.png"
image ivan = "images/chara/C_Field_Investigator.png"
image m_ivan = "images/chara/C_Field_Investigator_Mute.png"
image alexei = "images/chara/C_Technical_Investigator.png"
image m_alexei = "images/chara/C_Technical_Investigator_Mute.png"
image albert = "images/chara/V_The_briber.png"
image m_albert = "images/chara/V_The_briber_Mute.png"

image e1 = "images/Evi/eb1.png"
image e2 = "images/Evi/eb2.png"
image e3 = "images/Evi/eb3.png"

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


image investigation_room2:
    "images/briber/idle.png"

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

image fight_briber:
    "images/briber/fight.png"
    pause 0.7
    "images/briber/fight1.png"
    pause 0.7
    "images/briber/fight2.png"
    pause 0.7
    repeat
    
image lose_briber:
    "images/briber/lose.png"
    pause 0.7
    "images/briber/lose1.png"
    pause 0.7
    repeat
        
image win_briber:
    "images/briber/win.png"
    pause 0.7
    "images/briber/win1.png"
    pause 0.7
    "images/briber/win2.png"
    pause 0.7
    repeat
        
transform shake:
    xoffset 0
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset -8
    linear 0.05 xoffset 8
    linear 0.05 xoffset -5
    linear 0.05 xoffset 0
    
# ===== briber SYSTEM =====
default player_x2 = 700
default player_y2 = 500
default player_sitting2 = False
default evidence_found2 = False
default evidence_open2= False
default player_direction2 = "down"
default PLAYER_SPEED2 = 20
define INTERACTION_RADIUS2 = 50

define COMPUTER_X2 = 780
define COMPUTER_Y2 = 390
define CHAIR_X2 = 1250
define CHAIR_Y2 = 410

default briber_hearts = 3
default briber_state = "playing"
default briber_round = 0
default briber_question = ""
default briber_choices = []
default briber_message = ""
default briber_briber_type = ""
# briber question

init python:

    # ===== briber QUESTION DATA =====

    briber_ROUNDS = [

        # ROUND 1 - RARE FOX
        {
            "briber": "intelligence",
            "question": "Why do you think a rare fox was found near the burned forest?",
            "choices": [
                ("It might have been trying to escape the fire and find a safer place.", "forensic"),
                ("Someone probably brought it there as a pet.", "integrity"),
                ("It must have been responsible for starting the fire.", "intelligence")
            ]
        },

        # ROUND 2 - WET SLEEVES AND GASOLINE
        {
            "briber": "forensic",
            "question": "My sleeves were wet and smelled of gasoline. What does that tell you?",
            "choices": [
                ("You were probably trying to put out the fire.", "forensic"),
                ("You may have used gasoline as an accelerant to spread the fire.", "integrity"),
                ("You must have accidentally spilled gasoline while working nearby.", "intelligence")
            ]
        },

        # ROUND 3 - THE NECKLACE
        {
            "briber": "intelligence",
            "question": "Why would someone keep a photograph of their loved one so close to their heart?",
            "choices": [
                ("Perhaps it reminds you of someone you are trying to protect.", "forensic"),
                ("You probably stole the necklace from someone.", "integrity"),
                ("It could be a reminder of the person who gave you the money.", "intelligence")
            ]
        }
    ]


    # ===== LOAD QUESTION =====
    def load_briber_round():

        current = briber_ROUNDS[store.briber_round]

        store.briber_briber_type = current["briber"]
        store.briber_question = current["question"]
        store.briber_choices = current["choices"]
        
    # ===== START briber =====
    def start_briber():

        store.player_sitting2 = True
        store.briber_hearts = 3
        store.briber_round = 0
        store.briber_state = "playing"
        store.briber_message = ""

        load_briber_round()


    # ===== TOGGLE SIT =====

    def toggle_sit2():

        if store.player_sitting2:

            store.player_sitting2 = False
            store.briber_state = "playing"
            store.briber_message = ""

        else:
            start_briber()


    # ===== ANSWER QUESTION =====

    def answer_type2(choice):

        if store.briber_state != "playing":
            return

        briber = store.briber_briber_type
        
        # Same type: retry
        if choice == briber:

            store.briber_message = "Same type! Try another answer."
            store.briber_state = "retry"

            renpy.restart_interaction()
            return

        winning_type = {
            "forensic": "integrity",
            "integrity": "intelligence",
            "intelligence": "forensic"
        }

        # Correct answer
        if winning_type[briber] == choice:

            store.briber_state = "win_anim"

        # Wrong answer
        else:

            store.briber_hearts = max(
                0, store.briber_hearts - 1
            )

            store.briber_state = "lose_anim"

        renpy.restart_interaction()


    # ===== FINISH WIN ANIMATION =====

    def finish_win_animation2():

        store.briber_round += 1

        if store.briber_round >= len(briber_ROUNDS):

            store.briber_state = "game_win"

        else:

            load_briber_round()
            store.briber_state = "playing"
            store.briber_message = ""

        renpy.restart_interaction()


    # ===== FINISH LOSE ANIMATION =====

    def finish_lose_animation2():

        if store.briber_hearts <= 0:

            store.briber_state = "game_over"

        else:

            store.briber_state = "playing"
            store.briber_message = ""

        renpy.restart_interaction()


    # ===== TRY AGAIN =====

    def try_again2():

        start_briber()

screen exploration_room2():

    modal True

    # Background 
    add "investigation_room2"
            
    if player_direction2 == "up":
        add "player_walk_up":
            xpos player_x2
            ypos player_y2
            xanchor 0.8
            yanchor 0.5

    elif player_direction2 == "down":
        add "player_walk_down":
            xpos player_x2
            ypos player_y2
            xanchor 0.8
            yanchor 0.5

    elif player_direction2 == "left":
        add "player_walk_left":
            xpos player_x2
            ypos player_y2
            xanchor 0.8
            yanchor 0.5

    elif player_direction2 == "right":
        add "player_walk_right":
            xpos player_x2
            ypos player_y2
            xanchor 0.8
            yanchor 0.5

    # Player Movements
    if not player_sitting2 and not evidence_open1:

        # LEFT - A
        key "K_LEFT" action [
            SetVariable("player_x2", max(590, player_x2 - PLAYER_SPEED2)),
            SetVariable("player_direction1", "left")
        ]
        key "K_a" action [
            SetVariable("player_x2", max(590, player_x2 - PLAYER_SPEED2)),
            SetVariable("player_direction1", "left")
        ]

        # RIGHT - D
        key "K_RIGHT" action [
            SetVariable("player_x2", min(1600, player_x2 + PLAYER_SPEED2)),
            SetVariable("player_direction1", "right")
        ]
        key "K_d" action [
            SetVariable("player_x2", min(1600, player_x2 + PLAYER_SPEED2)),
            SetVariable("player_direction1", "right")
        ]

        # UP - W
        key "K_UP" action [
            SetVariable("player_y2", max(380, player_y2 - PLAYER_SPEED2)),
            SetVariable("player_direction1", "up")
        ]
        key "K_w" action [
            SetVariable("player_y2", max(380, player_y2 - PLAYER_SPEED2)),
            SetVariable("player_direction1", "up")
        ]

        # DOWN - S
        key "K_DOWN" action [
            SetVariable("player_y2", min(520, player_y2 + PLAYER_SPEED2)),
            SetVariable("player_direction1", "down")
        ]
        key "K_s" action [
            SetVariable("player_y2", min(520, player_y2 + PLAYER_SPEED2)),
            SetVariable("player_direction1", "down")
        ]

    # ===== briber ANIMATION: DRAW FIRST =====

    if player_sitting2:

        if briber_state in ("playing", "retry"):
            add "fight_briber":
                xalign 0.78
                yalign 0.60

        elif briber_state == "win_anim":
            add "lose_briber":
                xalign 0.78
                yalign 0.60

            timer 2.1 action Function(finish_win_animation1)

        elif briber_state == "lose_anim":
            add "win_briber":
                xalign 0.78
                yalign 0.60

            timer 2.1 action Function(finish_lose_animation1)

    # ===== HEARTS: TOP RIGHT =====
    if player_sitting2 and briber_state not in ("game_over", "game_win"):

        hbox:
            xalign 0.97
            yalign 0.02
            spacing 5

            for i in range(briber_hearts):
                add "images/heart.png":
                    xsize 40
                    ysize 40
              # ===== briber QUESTION BUBBLE =====

    if player_sitting2 and briber_state in ("playing", "retry"):

        frame:
            xpos 60
            ypos 50
            xsize 650
            background "#18212df2"
            xpadding 25
            ypadding 20

            vbox:
                spacing 10

                text "[briber_round + 1] / 3":
                    size 18
                    color "#aaaaaa"

                text "THE briber":
                    size 18
                    color (
                        "#56aaff" if briber_briber_type == "forensic"
                        else "#65e68a" if briber_briber_type == "integrity"
                        else "#ff83cf"
                    )

                text briber_question:
                    size 24
                    color "#ffffff"


    # ===== THREE CHOICE BUBBLES =====

    if player_sitting2 and briber_state in ("playing", "retry"):

        vbox:
            xpos 60
            ypos 230
            xsize 650
            spacing 15

            for choice_text, choice_type in briber_choices:

                textbutton choice_text:

                    xfill True

                    text_size 19

                    text_color (
                        "#56aaff" if choice_type == "forensic"
                        else "#65e68a" if choice_type == "integrity"
                        else "#ff83cf"
                    )

                    background "#18212df2"
                    hover_background "#40536a"

                    xpadding 20
                    ypadding 15

                    action Function(answer_type2, choice_type)
        
    # ===== FOX RETRY MESSAGE =====
    if player_sitting2 and briber_state == "retry":

        add "images/chara/C_Fox.png":
            xalign 0.9
            yalign 1.0
            zoom 0.2

        text briber_message:
            xpos 500
            ypos 670
            size 25
            color "#ffffff"
            
        timer 1.5 action [
            SetVariable("briber_state", "playing"),
            SetVariable("briber_message", "")
        ]
    # ===== GAME OVER SCREEN =====
    if briber_state == "game_over":

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
                action Function(try_again1)

            textbutton "HOME":
                xalign 0.5
                text_size 28
                action MainMenu(confirm=False)
                    
    # ===== GAME WIN =====
    if briber_state == "game_win":

        add Solid("#000000")

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 25

            text "CONGRATULATION!":
                size 65
                color "#bbf6f9"
                xalign 0.5
                
            text "INVESTIGATION COMPLETE":
                size 65
                color "#bbf6f9"
                xalign 0.5

            textbutton "CONTINUE":
                xalign 0.5
                text_size 28
                action Jump("after_battle2")
                
    # Interaksi komputer
    if not player_sitting2 and not evidence_open1:

        if (player_x2 - COMPUTER_X2) ** 2 + (player_y2 - COMPUTER_Y2) ** 2 < INTERACTION_RADIUS2 ** 2:

            textbutton "Inspect ( E )":
                xpos 180
                ypos 270
                text_size 16
                xpadding 8
                ypadding 4
                action SetVariable("evidence_open1", True)

            key "e" action SetVariable("evidence_open1", True)

    # Interaksi kursi
    if not evidence_open1:

        if (player_x2 - CHAIR_X2) ** 2 + (player_y2 - CHAIR_Y2) ** 2 < INTERACTION_RADIUS2 ** 2:

            textbutton (" " if player_sitting2 else "Sit Down ( E )"):
                xpos 850
                ypos 300
                text_size 16
                xpadding 8
                ypadding 4
                action Function(toggle_sit1)

            key "e" action Function(toggle_sit1)
            
    
    if evidence_open1:

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

                            add "images/Evi/eb1.png":
                                xalign 0.5
                                fit "contain"
                                xysize (200, 200)

                            text "1. A Blushfen" size 18

                    # Evidence 2
                    frame:
                        xsize 270
                        ysize 270
                        background "#303d4d"
                        padding [12, 12, 12, 12]

                        vbox:
                            spacing 10

                            add "images/Evi/eb2.png":
                                xalign 0.5
                                fit "contain"
                                xysize (200, 200)

                            text "2. A sleeve cuffs look wet" size 18

                    # Evidence 3
                    frame:
                        xsize 270
                        ysize 270
                        background "#303d4d"
                        padding [12, 12, 12, 12]

                        vbox:
                            spacing 10

                            add "images/Evi/eb3.png":
                                xalign 0.5
                                fit "contain"
                                xysize (200, 200)

                            text "3. A necklace" size 18

                textbutton "Close":
                    xalign 1.0
                    action SetVariable("evidence_open1", False)

    key "K_ESCAPE" action Return()
    
label secondscene:
    jump investigation_room2
    
label investigation_room2:
    
    call screen exploration_room2
    
    return

label after_battle2:
    return
