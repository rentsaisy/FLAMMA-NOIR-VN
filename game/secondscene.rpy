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
image fox = "images/chara/C_Fox.png"
image m_fox = "images/chara/C_Fox_Mute.png"
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

image ebr1 = "images/Evi/ebri1.png"
image ebr2 = "images/Evi/ebri2.png"
image ebr3 = "images/Evi/ebri3.png"

image BGH = "images/BGH.png"
image BGO = "images/BG_office.png"
image S2_1 = "images/S2_1.png"
image S2_2 = "images/S2_2.png"

image investigation_room2:
    "images/TBR/tbridle.png"
    pause 0.5
    "images/TBR/tbridle1.png"
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

image fight_briber:
    "images/TBR/tbrfight.png"
    pause 0.7
    "images/TBR/tbrfight1.png"
    pause 0.7
    "images/TBR/tbrfight2.png"
    pause 0.7
    repeat
    
image lose_briber:
    "images/TBR/tbrlose.png"
    pause 0.7
    "images/TBR/tbrlose1.png"
    pause 0.7
    repeat
        
image win_briber:
    "images/TBR/tbrwin.png"
    pause 0.7
    "images/TBR/tbrwin1.png"
    pause 0.7
    "images/TBR/tbrwin2.png"
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

init python:

    # ===== briber QUESTION DATA =====

    BRIBER_ROUNDS = [

        # ROUND 1 - THE COMPANY LIGHTER
        {
            "briber": "intelligence",
            "question": "Why was Oscar give a lighter bearing the Whaley Company logo?",
            "choices": [
                ("It could have been used by someone connected to Whaley Company to start the fire.", "forensic"),
                ("It was probably left behind by a random visitor.", "integrity"),
                ("Perhaps someone give him to frame the company.", "intelligence")
            ]
        },

        # ROUND 2 - PAYMENT FOR THE BURNER
        {
            "briber": "forensic",
            "question": "What can you tell me about this payment record labeled as a payment for the Burner?",
            "choices": [
                ("It was probably just an ordinary business transaction.", "forensic"),
                ("The payment suggests that someone hired an arsonist to deliberately burn the forest.", "integrity"),
                ("You might have been paying someone to handle an unrelated company matter.", "intelligence")
            ]
        },

        # ROUND 3 - THE GHOST AGREEMENT
        {
            "briber": "integrity",
            "question": "Why does this agreement mention someone called THE GHOST?",
            "choices": [
                ("Perhaps The Ghost is just a nickname for one of your business partners.", "forensic"),
                ("It could simply be an informal agreement with no connection to the fire.", "integrity"),
                ("The document suggests that you made a secret deal with The Ghost regarding the forest fire.", "intelligence")
            ]
        },

        # ROUND 4 - THE MASTERMIND
        {
            "briber": "intelligence",
            "question": "According to this agreement, why am I willing to take responsibility as the mastermind behind the forest fire?",
            "choices": [
                ("You were promised a financial reward after being released from prison in exchange for taking the blame.", "forensic"),
                ("You probably wanted to protect Whaley Company`s reputation.", "integrity"),
                ("Perhaps you simply wanted to take responsibility for someone else`s actions.", "intelligence")
            ]
        },

        # ROUND 5 - THE POLITICAL FUNDING
        {
            "briber": "forensic",
            "question": "What was The Ghost offering me in exchange for claiming to be the mastermind?",
            "choices": [
                ("Perhaps The Ghost was simply trying to help you escape the consequences of your actions.", "forensic"),
                ("You were promised money after your release and financial support for your political ambitions.", "integrity"),
                ("The agreement was probably just a personal favor between the two of you.", "intelligence")
            ]
        }
    ]


    # ===== LOAD QUESTION =====
    def load_briber_round():

        current = BRIBER_ROUNDS[store.briber_round]

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

        if store.briber_round >= len(BRIBER_ROUNDS):

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
    if not player_sitting2 and not evidence_open2:

        # LEFT - A
        key "K_LEFT" action [
            SetVariable("player_x2", max(590, player_x2 - PLAYER_SPEED2)),
            SetVariable("player_direction2", "left")
        ]
        key "K_a" action [
            SetVariable("player_x2", max(590, player_x2 - PLAYER_SPEED2)),
            SetVariable("player_direction2", "left")
        ]

        # RIGHT - D
        key "K_RIGHT" action [
            SetVariable("player_x2", min(1600, player_x2 + PLAYER_SPEED2)),
            SetVariable("player_direction2", "right")
        ]
        key "K_d" action [
            SetVariable("player_x2", min(1600, player_x2 + PLAYER_SPEED2)),
            SetVariable("player_direction2", "right")
        ]

        # UP - W
        key "K_UP" action [
            SetVariable("player_y2", max(380, player_y2 - PLAYER_SPEED2)),
            SetVariable("player_direction2", "up")
        ]
        key "K_w" action [
            SetVariable("player_y2", max(380, player_y2 - PLAYER_SPEED2)),
            SetVariable("player_direction2", "up")
        ]

        # DOWN - S
        key "K_DOWN" action [
            SetVariable("player_y2", min(520, player_y2 + PLAYER_SPEED2)),
            SetVariable("player_direction2", "down")
        ]
        key "K_s" action [
            SetVariable("player_y2", min(520, player_y2 + PLAYER_SPEED2)),
            SetVariable("player_direction2", "down")
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

            timer 2.1 action Function(finish_win_animation2)

        elif briber_state == "lose_anim":
            add "win_briber":
                xalign 0.78
                yalign 0.60

            timer 2.1 action Function(finish_lose_animation2)

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

                text "[briber_round + 1] / 5":
                    size 18
                    color "#aaaaaa"

                text "THE BRIBER":
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
    if not player_sitting2 and not evidence_open2:

        if (player_x2 - COMPUTER_X2) ** 2 + (player_y2 - COMPUTER_Y2) ** 2 < INTERACTION_RADIUS2 ** 2:

            textbutton "Inspect ( E )":
                xpos 180
                ypos 270
                text_size 16
                xpadding 8
                ypadding 4
                action SetVariable("evidence_open2", True)

            key "e" action SetVariable("evidence_open2", True)

    # Interaksi kursi
    if not evidence_open2:

        if (player_x2 - CHAIR_X2) ** 2 + (player_y2 - CHAIR_Y2) ** 2 < INTERACTION_RADIUS2 ** 2:

            textbutton (" " if player_sitting2 else "Sit Down ( E )"):
                xpos 850
                ypos 300
                text_size 16
                xpadding 8
                ypadding 4
                action Function(toggle_sit2)

            key "e" action Function(toggle_sit2)
            
    
    if evidence_open2:

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

                            add "images/Evi/ebri1.png":
                                xalign 0.5
                                fit "contain"
                                xysize (200, 200)

                            text "1. A whaley lighter" size 18

                    # Evidence 2
                    frame:
                        xsize 270
                        ysize 270
                        background "#303d4d"
                        padding [12, 12, 12, 12]

                        vbox:
                            spacing 10

                            add "images/Evi/ebri2.png":
                                xalign 0.5
                                fit "contain"
                                xysize (200, 200)

                            text "2. Burning fee" size 18

                    # Evidence 3
                    frame:
                        xsize 270
                        ysize 270
                        background "#303d4d"
                        padding [12, 12, 12, 12]

                        vbox:
                            spacing 10

                            add "images/Evi/ebri3.png":
                                xalign 0.5
                                fit "contain"
                                xysize (200, 200)

                            text "3. A bunch of paper" size 18

                textbutton "Close":
                    xalign 1.0
                    action SetVariable("evidence_open2", False)

    key "K_ESCAPE" action Return()
    
label secondscene:
    scene BGO
    "The investigation team returns to the office with the evidence recovered from the forest."
    show sonya:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Sonya "WELCOME BACK KATERINE..!! IVAN..!!"
    Sonya "Wait! Is that a Blushfen?!"
    hide sonya
    show fox:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    $ custom_voice = "audio/voice/fox/pinkvoice_confused.wav"
    Fox "Mrrp?"
    hide fox
    show m_fox:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    show katerine:
        xalign 0.1
        yalign 0.1
        zoom 0.256
    Katerine "We found her in the forest and I want you to check this lighter. The emblem looks like symbol of whaley company."
    hide katerine
    show m_katerine:
        xalign 0.1
        yalign 0.1
        zoom 0.256
    show sonya:
        xalign 1.0
        yalign 0.1
        zoom 0.256
    Sonya "Hmmmmm the whaley company do have a lighter product but let`s just give it to Alexei. HEY LEXEI! CAN YOU CHECK THIS THING AND TRACING THE COMPANY?!"
    hide sonya
    hide m_katerine
    hide m_fox
    with dissolve
    scene black
    show ebr1:
        xalign 0.5
        yalign 0.5
        zoom 1.0
    "The lighter with whaley company emblem are placed on the table."
    hide ebr1
    scene BGO
    show alexei:
        xalign 0.5
        yalign 0.3
        zoom 0.232
    Alexei  "I traced the emblem to a company involved in the forest development project."
    hide alexei
    show m_alexei:
        xalign 0.5
        yalign 0.3
        zoom 0.232
    show katerine:
        xalign 0.1
        yalign 0.1
        zoom 0.256
    Katerine "So the company is connected to the fire?"
    hide katerine
    show m_katerine:
        xalign 0.1
        yalign 0.1
        zoom 0.256
    show alexei:
        xalign 0.5
        yalign 0.3
        zoom 0.232
    Alexei "Not directly. But someone inside the company made several suspicious payments before the incident."
    hide alexei
    hide m_alexei
    hide m_katerine
    with dissolve
    show sonya:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Sonya "Fine, I`ll go with you Katerine tommorow to do investigation, I also wanna meet my old friend."
    hide sonya
    show katerine:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Katerine "And find whoever paid The Burner."
    hide katerine
    
    scene black    
    "The team arrives at the company`s headquarters."
    scene BGH
    "The building is almost empty."
    show sonya:
        xalign 0.1
        yalign 0.1
        zoom 0.256
    Sonya "Something feels wrong."
    hide sonya
    show m_sonya:
        xalign 0.1
        yalign 0.1
        zoom 0.256
    show katerine:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Katerine "There`s no one here."
    hide katerine
    hide m_sonya
    with dissolve
    show albert:
        xalign 0.5
        yalign 0.3
        zoom 0.232
    Albert "Hello, Sonya.."
    hide albert
    show sonya:
        xalign 0.1
        yalign 0.1
        zoom 0.256
    Sonya "Hello, my dear old friend. Albert, we got a question for you."
    hide sonya
    show m_sonya:
        xalign 0.1
        yalign 0.1
        zoom 0.256
    show katerine:
        xalign 0.5
        yalign 0.1
        zoom 0.256    
    Katerine "Are you the one who paid The Burner?"
    scene black
    show ebr2:
        xalign 0.5
        yalign 0.5
        zoom 1.0
    Albert "Ah that little boy who loves his sister so much, give this payment to him."
    hide ebr2
    scene BGH
    show katerine:
        xalign 0.5
        yalign 0.1
        zoom 0.256 
    Katerine "So you admit that you`re the mastermind."
    hide katerine
    scene S2_1
    Albert "Forest can be bought."
    Albert "And so can people."
    scene BGH
    show katerine:
        xalign 0.5
        yalign 0.1
        zoom 0.256 
    Katerine "You try to pay us?"
    hide katerine
    show albert:
        xalign 0.5
        yalign 0.3
        zoom 0.232
    Albert "Yeah, Why not?"
    hide albert
    scene black
    show ebr3:
        xalign 0.5
        yalign 0.5
        zoom 1.0
    "Sonya notices a bunch of paper on his table."
    hide ebr3
    scene BGH
    show sonya:
        xalign 0.5
        yalign 0.1
        zoom 0.256 
    Sonya "The Ghost?"
    hide sonya
    show albert:
        xalign 0.5
        yalign 0.3
        zoom 0.232
    Albert "HEY! DO NOT TOUCH MY THING!"
    hide albert
    show sonya:
        xalign 0.5
        yalign 0.1
        zoom 0.256 
    Sonya "So you admit yourself as the mastermind to hide the real mastermind? KATERINE! BEGIN THE INVESTIGATION!"
    jump investigation_room2
    
label investigation_room2:
    play music "audio/bgm/home-battle.wav" fadein 1.0
    call screen exploration_room2
    
    return

label after_battle2:
    stop music fadeout 1.0
    scene S2_2
    "The Bribe looks directly to Katerine."
    Albert "Because the moment you find The Ghost..."
    "He pauses."
    Albert "...The Ghost will find you first."
    scene BGH
    show sonya:
        xalign 0.5
        yalign 0.1
        zoom 0.256 
    Sonya "Alright keep your mouth shut the briber. Enjoy your time with the police. Katerine, let`s back to the office for rest."
    return
