# SCENE 3

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
image franz = "images/chara/V_The_ghost.png"
image m_franz = "images/chara/V_The_ghost_Mute.png"

image eg1 = "images/Evi/eg1.png"
image eg2 = "images/Evi/eg2.png"
image eg3 = "images/Evi/eg3.png"
image em2 = "images/Evi/em2.png"

image BGB = "images/BGB.png"
image BGO = "images/BG_office.png"
image S3_1 = "images/S3_1.png"
image S3_2 = "images/S3_2.png"

image investigation_room3:
    "images/TG/tgidle.png"
    pause 0.5
    "images/TG/tgidle1.png"
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

image fight_ghost:
    "images/TG/tgfight.png"
    pause 0.7
    "images/TG/tgfight1.png"
    pause 0.7
    "images/TG/tgfight2.png"
    pause 0.7
    repeat
    
image lose_ghost:
    "images/TG/tglose.png"
    pause 0.7
    "images/TG/tglose1.png"
    pause 0.7
    repeat
        
image win_ghost:
    "images/TG/tgwin.png"
    pause 0.7
    "images/TG/tgwin1.png"
    pause 0.7
    "images/TG/tgwin2.png"
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
    
# ===== ghost SYSTEM =====
default player_x3 = 700
default player_y3 = 500
default player_sitting3 = False
default evidence_found3 = False
default evidence_open3= False
default player_direction3 = "down"
default PLAYER_SPEED3 = 20
define INTERACTION_RADIUS3 = 50

define COMPUTER_X3 = 780
define COMPUTER_Y3 = 390
define CHAIR_X3 = 1250
define CHAIR_Y3 = 410

default ghost_hearts = 3
default ghost_state = "playing"
default ghost_round = 0
default ghost_question = ""
default ghost_choices = []
default ghost_message = ""
default ghost_ghost_type = ""

init python:

    # ===== ghost QUESTION DATA =====

    GHOST_ROUNDS = [

        # ROUND 1 - THE UNKNOWN FOLDER
        {
            "ghost": "intelligence",
            "question": "Why do you think I sent this unknown folder to your email?",
            "choices": [
                ("You wanted me to discover the truth behind the forest fire and the agreement.", "intelligence"),
                ("You wanted to meet us for your own benefit.", "forensic"),
                ("You probably sent it by mistake without knowing its contents.", "integrity")
            ]
        },

        # ROUND 2 - THE FLASH DRIVE
        {
            "ghost": "forensic",
            "question": "What do you think the flashdisk found near the basement contains?",
            "choices": [
                ("It might contain evidence of the secret agreement between you and The Briber.", "forensic"),
                ("It could contain information about the person responsible for planning the forest arson.", "integrity"),
                ("It probably contains ordinary company files unrelated to the investigation.", "intelligence")
            ]
        },

        # ROUND 3 - THE GHOST AGREEMENT
        {
            "ghost": "integrity",
            "question": "Why would I make an agreement with The Briber regarding the forest fire?",
            "choices": [
                ("You were probably forced to cooperate with The Briber.", "forensic"),
                ("You wanted to receive money from the illegal destruction of the forest.", "integrity"),
                ("You wanted to help the mastermind escape responsibility for the forest arson.", "intelligence")
            ]
        },

        # ROUND 4 - THE BLUSHFEN PHOTOGRAPH
        {
            "ghost": "forensic",
            "question": "What can you tell from this photograph of your older sister with a Blushfen?",
            "choices": [
                ("She might have had a personal connection with the protected species before its habitat was destroyed.", "forensic"),
                ("She`s been in love with blushfen since we were children.", "integrity"),
                ("She was probably just visiting the forest like any other tourist.", "intelligence")
            ]
        },

        # ROUND 5 - THE MASTERMIND'S IDENTITY
        {
            "ghost": "intelligence",
            "question": "Based on the evidence, who do you think might be the mastermind behind the forest arson?",
            "choices": [
                ("My older sister, who had a hidden agenda behind her conservation project.", "forensic"),
                ("You, who probably planned everything without anyone else's involvement", "intelligence"),
                ("The Briber, who probably planned everything without anyone else's involvement.", "integrity")
            ]
        },

        # ROUND 6 - THE GHOST'S INVOLVEMENT
        {
            "ghost": "integrity",
            "question": "If I knew your sister was responsible for the forest arson, why do you think I still helped her?",
            "choices": [
                ("You were promised a financial reward for helping her.", "forensic"),
                ("You loved her and wanted to protect her, even if it meant helping her cover up a terrible crime.", "intelligence"),
                ("You were afraid she would reveal your involvement in the illegal operation.", "integrity")
            ]
        },

        # ROUND 7 - THE TRUE MOTIVE
        {
            "ghost": "intelligence",
            "question": "Then, what do you think I truly wanted when I made that agreement with The Briber?",
            "choices": [
                ("You wanted to help the woman you loved avoid the consequences of her actions, even at the cost of innocent lives.", "forensic"),
                ("You wanted to become the mastermind behind the entire operation.", "integrity"),
                ("You wanted to gain control over Whaley Company's new conservation project.", "intelligence")
            ]
        }
    ]



    # ===== LOAD QUESTION =====
    def load_ghost_round():

        current = GHOST_ROUNDS[store.ghost_round]

        store.ghost_ghost_type = current["ghost"]
        store.ghost_question = current["question"]
        store.ghost_choices = current["choices"]
        
    # ===== START ghost =====
    def start_ghost():

        store.player_sitting3 = True
        store.ghost_hearts = 3
        store.ghost_round = 0
        store.ghost_state = "playing"
        store.ghost_message = ""

        load_ghost_round()


    # ===== TOGGLE SIT =====

    def toggle_sit3():

        if store.player_sitting3:

            store.player_sitting3 = False
            store.ghost_state = "playing"
            store.ghost_message = ""

        else:
            start_ghost()


    # ===== ANSWER QUESTION =====

    def answer_type3(choice):

        if store.ghost_state != "playing":
            return

        ghost = store.ghost_ghost_type
        
        # Same type: retry
        if choice == ghost:

            store.ghost_message = "Same type! Try another answer."
            store.ghost_state = "retry"

            renpy.restart_interaction()
            return

        winning_type = {
            "forensic": "integrity",
            "integrity": "intelligence",
            "intelligence": "forensic"
        }

        # Correct answer
        if winning_type[ghost] == choice:

            store.ghost_state = "win_anim"

        # Wrong answer
        else:

            store.ghost_hearts = max(
                0, store.ghost_hearts - 1
            )

            store.ghost_state = "lose_anim"

        renpy.restart_interaction()


    # ===== FINISH WIN ANIMATION =====

    def finish_win_animation3():

        store.ghost_round += 1

        if store.ghost_round >= len(GHOST_ROUNDS):

            store.ghost_state = "game_win"

        else:

            load_ghost_round()
            store.ghost_state = "playing"
            store.ghost_message = ""

        renpy.restart_interaction()


    # ===== FINISH LOSE ANIMATION =====

    def finish_lose_animation3():

        if store.ghost_hearts <= 0:

            store.ghost_state = "game_over"

        else:

            store.ghost_state = "playing"
            store.ghost_message = ""

        renpy.restart_interaction()


    # ===== TRY AGAIN =====

    def try_again3():

        start_ghost()

screen exploration_room3():

    modal True

    # Background 
    add "investigation_room3"
            
    if player_direction3 == "up":
        add "player_walk_up":
            xpos player_x3
            ypos player_y3
            xanchor 0.8
            yanchor 0.5

    elif player_direction3 == "down":
        add "player_walk_down":
            xpos player_x3
            ypos player_y3
            xanchor 0.8
            yanchor 0.5

    elif player_direction3 == "left":
        add "player_walk_left":
            xpos player_x3
            ypos player_y3
            xanchor 0.8
            yanchor 0.5

    elif player_direction3 == "right":
        add "player_walk_right":
            xpos player_x3
            ypos player_y3
            xanchor 0.8
            yanchor 0.5

    # Player Movements
    if not player_sitting3 and not evidence_open3:

        # LEFT - A
        key "K_LEFT" action [
            SetVariable("player_x3", max(590, player_x3 - PLAYER_SPEED3)),
            SetVariable("player_direction3", "left")
        ]
        key "K_a" action [
            SetVariable("player_x3", max(590, player_x3 - PLAYER_SPEED3)),
            SetVariable("player_direction3", "left")
        ]

        # RIGHT - D
        key "K_RIGHT" action [
            SetVariable("player_x3", min(1600, player_x3 + PLAYER_SPEED3)),
            SetVariable("player_direction3", "right")
        ]
        key "K_d" action [
            SetVariable("player_x3", min(1600, player_x3 + PLAYER_SPEED3)),
            SetVariable("player_direction3", "right")
        ]

        # UP - W
        key "K_UP" action [
            SetVariable("player_y3", max(380, player_y3 - PLAYER_SPEED3)),
            SetVariable("player_direction3", "up")
        ]
        key "K_w" action [
            SetVariable("player_y3", max(380, player_y3 - PLAYER_SPEED3)),
            SetVariable("player_direction3", "up")
        ]

        # DOWN - S
        key "K_DOWN" action [
            SetVariable("player_y3", min(520, player_y3 + PLAYER_SPEED3)),
            SetVariable("player_direction3", "down")
        ]
        key "K_s" action [
            SetVariable("player_y3", min(520, player_y3 + PLAYER_SPEED3)),
            SetVariable("player_direction3", "down")
        ]

    # ===== ghost ANIMATION: DRAW FIRST =====

    if player_sitting3:

        if ghost_state in ("playing", "retry"):
            add "fight_ghost":
                xalign 0.78
                yalign 0.60

        elif ghost_state == "win_anim":
            add "lose_ghost":
                xalign 0.78
                yalign 0.60

            timer 2.1 action Function(finish_win_animation3)

        elif ghost_state == "lose_anim":
            add "win_ghost":
                xalign 0.78
                yalign 0.60

            timer 2.1 action Function(finish_lose_animation3)

    # ===== HEARTS: TOP RIGHT =====
    if player_sitting3 and ghost_state not in ("game_over", "game_win"):

        hbox:
            xalign 0.97
            yalign 0.02
            spacing 5

            for i in range(ghost_hearts):
                add "images/heart.png":
                    xsize 40
                    ysize 40
              # ===== ghost QUESTION BUBBLE =====

    if player_sitting3 and ghost_state in ("playing", "retry"):

        frame:
            xpos 60
            ypos 50
            xsize 650
            background "#18212df2"
            xpadding 25
            ypadding 20

            vbox:
                spacing 10

                text "[ghost_round + 1] / 7":
                    size 18
                    color "#aaaaaa"

                text "THE GHOST":
                    size 18
                    color (
                        "#56aaff" if ghost_ghost_type == "forensic"
                        else "#65e68a" if ghost_ghost_type == "integrity"
                        else "#ff83cf"
                    )

                text ghost_question:
                    size 24
                    color "#ffffff"


    # ===== THREE CHOICE BUBBLES =====

    if player_sitting3 and ghost_state in ("playing", "retry"):

        vbox:
            xpos 60
            ypos 230
            xsize 650
            spacing 15

            for choice_text, choice_type in ghost_choices:

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

                    action Function(answer_type3, choice_type)
        
    # ===== FOX RETRY MESSAGE =====
    if player_sitting3 and ghost_state == "retry":

        add "images/chara/C_Fox.png":
            xalign 0.9
            yalign 1.0
            zoom 0.2

        text ghost_message:
            xpos 500
            ypos 670
            size 25
            color "#ffffff"
            
        timer 1.5 action [
            SetVariable("ghost_state", "playing"),
            SetVariable("ghost_message", "")
        ]
    # ===== GAME OVER SCREEN =====
    if ghost_state == "game_over":

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
                action Function(try_again3)

            textbutton "HOME":
                xalign 0.5
                text_size 28
                action MainMenu(confirm=False)
                    
    # ===== GAME WIN =====
    if ghost_state == "game_win":

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
                action Jump("after_battle3")
                
    # Interaksi komputer
    if not player_sitting3 and not evidence_open3:

        if (player_x3 - COMPUTER_X3) ** 2 + (player_y3 - COMPUTER_Y3) ** 2 < INTERACTION_RADIUS3 ** 2:

            textbutton "Inspect ( E )":
                xpos 180
                ypos 270
                text_size 16
                xpadding 8
                ypadding 4
                action SetVariable("evidence_open3", True)

            key "e" action SetVariable("evidence_open3", True)

    # Interaksi kursi
    if not evidence_open3:

        if (player_x3 - CHAIR_X3) ** 2 + (player_y3 - CHAIR_Y3) ** 2 < INTERACTION_RADIUS3 ** 2:

            textbutton (" " if player_sitting3 else "Sit Down ( E )"):
                xpos 850
                ypos 300
                text_size 16
                xpadding 8
                ypadding 4
                action Function(toggle_sit3)

            key "e" action Function(toggle_sit3)
            
    
    if evidence_open3:

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

                            add "images/Evi/eg1.png":
                                xalign 0.5
                                fit "contain"
                                xysize (200, 200)

                            text "1. Unknown Folder" size 18

                    # Evidence 2
                    frame:
                        xsize 270
                        ysize 270
                        background "#303d4d"
                        padding [12, 12, 12, 12]

                        vbox:
                            spacing 10

                            add "images/Evi/eg2.png":
                                xalign 0.5
                                fit "contain"
                                xysize (200, 200)

                            text "2. A flashdisk" size 18

                    # Evidence 3
                    frame:
                        xsize 270
                        ysize 270
                        background "#303d4d"
                        padding [12, 12, 12, 12]

                        vbox:
                            spacing 10

                            add "images/Evi/eg3.png":
                                xalign 0.5
                                fit "contain"
                                xysize (200, 200)

                            text "3. Picture a Girl with Blushfen" size 18

                textbutton "Close":
                    xalign 1.0
                    action SetVariable("evidence_open3", False)

    key "K_ESCAPE" action Return()
    
label thirdscene:
    scene BGO
    "The team continues investigating the mysterious identity known as The Ghost."
    show katerine:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Katerine "Hmmm guys, someone send me a mail message. And there`s a zip file on it."
    hide katerine
    show sonya:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Sonya "WAIT KATERINE! DO NOT OPEN IT, LEXEI!!!"
    hide sonya
    show alexei:
        xalign 1.0
        yalign 0.3
        zoom 0.232
    Alexei "Sonya.. I`m not deaf. Can you just call me without yelling?"
    hide alexei
    show m_alexei:
        xalign 1.0
        yalign 0.3
        zoom 0.232
    show sonya:
        xalign 0.1
        yalign 0.1
        zoom 0.256
    Sonya "Well..I`m the leader so it`s up to me."
    hide sonya
    hide m_alexei
    with dissolve
    show katerine:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Katerine "Lexei, can you check this zip file for me, the sender account is also anonymous but I`m pretty sure he is the ghost."
    hide katerine
    show alexei:
        xalign 0.5
        yalign 0.3
        zoom 0.232
    Alexei "How?"
    hide alexei
    show katerine:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Katerine "Because the briber tell that the ghost will find me first."
    hide katerine
    show alexei:
        xalign 0.5
        yalign 0.3
        zoom 0.232
    Alexei "What a great conclusion, just wait and let me trace this person."
    hide alexei
    scene black
    show eg1:
        xalign 0.5
        yalign 0.5
        zoom 1.0    
    "Alexei found the encrypted message on zip file and try to recover it."
    hide eg1
    scene BGO
    show alexei:
        xalign 1.0
        yalign 0.3
        zoom 0.232
    Alexei "I`ve been trying to trace this account for days."
    hide alexei
    show m_alexei:
        xalign 1.0
        yalign 0.3
        zoom 0.232
    show katerine:
        xalign 0.3
        yalign 0.1
        zoom 0.256
    Katerine "And?"
    hide katerine
    show m_katerine:
        xalign 0.3
        yalign 0.1
        zoom 0.256
    show alexei:
        xalign 1.0
        yalign 0.3
        zoom 0.232  
    Alexei "Nothing."
    hide alexei
    show ivan:
        xalign 0.8
        yalign 0.3
        zoom 0.232
    Ivan "No identity?"
    hide ivan
    show m_ivan:
        xalign 0.8
        yalign 0.3
        zoom 0.232
    show alexei:
        xalign 1.0
        yalign 0.3
        zoom 0.232  
    Alexei "No identity. No digital footprint. But there`s a location he leaves"
    hide alexei
    show sonya:
        xalign 0.1
        yalign 0.1
        zoom 0.256
    Sonya "I think he want to meet us?"
    hide sonya
    hide m_katerine
    hide m_ivan
    hide m_alexei
    with dissolve
    show alexei:
        xalign 0.5
        yalign 0.3
        zoom 0.232 
    Alexei "Nope, he want to meet katerine and someone who can read his encrypted message which is me. So two person is enough."
    hide alexei
    show katerine:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Katerine "Why me?"
    hide katerine
    show fox:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Fox "Waa" #sad
    hide fox
    show alexei:
        xalign 0.5
        yalign 0.3
        zoom 0.232 
    Alexei "I don`t know, and Katerine.. How the ghost find your account? and actually I`m stalking about your background before, your background completely clean in the internet like someone who never exist."
    hide alexei
    show katerine:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Katerine "Because I only use internet for important things?"
    hide katerine
    show alexei:
        xalign 0.5
        yalign 0.3
        zoom 0.232
    Alexei "Ughh.. fine. If The Ghost wants to talk, this might be our only chance."
    hide alexei

    scene black
    "Katerine and Alexei enter a basement of abandoned building."
    scene BGB
    "The basement is completely dark."
    show katerine:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Katerine "I think I step something."
    hide katerine
    scene black
    show eg2:
        xalign 0.5
        yalign 0.5
        zoom 1.0 
    Katerine "A flashdisk?"
    hide eg2
    scene BGB
    show alexei:
        xalign 0.5
        yalign 0.3
        zoom 0.232
    Alexei "Let me check this on my laptop."
    hide alexei 
    show katerine:
        xalign 0.5
        yalign 0.1
        zoom 0.256   
    Katerine "What?! You bring laptop in this situation?"
    hide katerine
    show alexei:
        xalign 0.5
        yalign 0.3
        zoom 0.232
    Alexei "I am an IT guy, I always with my laptop."
    hide alexei 
    show franz:
        xalign 0.5
        yalign 0.3
        zoom 0.232
    Franz "You should have listened to the warning."
    hide franz    
    show katerine:
        xalign 0.5
        yalign 0.1
        zoom 0.256 
    Katerine "AAAAAAA! What? There`s a warning?"
    hide katerine
    show alexei:
        xalign 0.5
        yalign 0.3
        zoom 0.232
    Alexei "Ah He said do not come here, but the rule is meant to be broken."
    hide alexei
    show katerine:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Katerine "Lexei.. okay fine. So the ghost?"
    hide katerine
    show franz:
        xalign 0.5
        yalign 0.3
        zoom 0.232
    Franz "That name is enough."
    hide franz
    show katerine:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Katerine "Who are you working for or are you the mastermind?"
    hide katerine
    show franz:
        xalign 0.5
        yalign 0.3
        zoom 0.232
    "Silence."
    Franz "You really look like her and you ask too many questions."
    hide franz
    show katerine:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Katerine "Her?"
    hide katerine
    scene S3_1
    Franz "Sadly, I can`t kill you. But maybe I`ll try to keep your partner shut."
    scene BGB
    show alexei:
        xalign 0.5
        yalign 0.3
        zoom 0.232
    Alexei "Stop right there Franz Kafka. I already contact the police and the NOIR."
    hide alexei
    scene black
    show eg3:
        xalign 0.5
        yalign 0.5
        zoom 1.0 
    Alexei "And look at this katerine."
    hide eg3
    scene BGB
    show katerine:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Katerine "This is.. Alright begin the investigation."
    jump investigation_room3
    
label investigation_room3:
    
    call screen exploration_room3
    
    return

label after_battle3:
    scene BGB
    show franz:
        xalign 0.5
        yalign 0.3
        zoom 0.232
    Franz "WOW YOU ALSO SMART LIKE HER!"
    hide franz
    scene S3_2
    Katerine "Keep your mouth shut. I`m nothing like her."
    scene BGB
    show alexei:
        xalign 0.5
        yalign 0.3
        zoom 0.232
    Alexei "You look scary when serious."
    hide alexei
    show katerine:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Katerine "Because now we know who we`re really looking for."
    hide katerine
    show alexei:
        xalign 0.5
        yalign 0.3
        zoom 0.232
    Alexei "There`s one final piece of information."
    hide alexei
    scene black
    show em2:
        xalign 0.5
        yalign 0.5
        zoom 1.0    
    Katerine "What?"
    "The screen displays"
    "PROJECT FLAMMA"
    "DIRECTOR: ██████████"
    "STATUS: ACTIVE"
    hide em2
    scene BGB
    show katerine:
        xalign 0.1
        yalign 0.1
        zoom 0.256
    Katerine "JUST WHAT EXACTLY HER MOTIVE?! I WILL NEVER UNDERSTAND HER!"
    hide katerine
    show m_katerine:
        xalign 0.1
        yalign 0.1
        zoom 0.256
    show alexei:
        xalign 0.4
        yalign 0.3
        zoom 0.232
    Alexei "Calm down Katerine, I think we need to go back to the office first. The police will take the ghost, now please calm yourself."
    hide alexei
    show m_alexei:
        xalign 0.4
        yalign 0.3
        zoom 0.232
    show franz:
        xalign 1.0
        yalign 0.3
        zoom 0.232
    Franz "Katerine, I hope you`re not fighting with your sister again."
    hide franz
    hide m_katerine
    hide m_alexei
    with dissolve
    scene S3_2
    Katerine "Silence! You just a fool and a tool for her."
    scene BGB
    show franz:
        xalign 0.5
        yalign 0.3
        zoom 0.232
    Franz "So you too.."
    return
