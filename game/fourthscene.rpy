# SCENE 4

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
image agatha = "images/chara/V_The_mastermind.png"
image m_agatha = "images/chara/V_The_mastermind_Mute.png"

image em1 = "images/Evi/em1.png"
image em2 = "images/Evi/em2.png"
image em3 = "images/Evi/em3.png"

image BGC = "images/BGC.png"
image BGO = "images/BG_office.png"
image S4_1 = "images/S4_1.png"
image S4_21 = "images/S4_21.png"
image S4_22 = "images/S4_22.png"
image S4_23 = "images/S4_23.png"
image S4_3 = "images/S4_3.png"
image S4_4 = "images/S4_4.png"
image SA = "images/SkyA.png"
image SB = "images/SkyB.png"
image END = "images/endsong.png"

transform ending_zoom:
    zoom 3.0
    xalign 0.5
    yalign 1.0
    linear 133.0 zoom 1.0
    
transform credits_scroll:
    yoffset 750
    linear 40.0 yoffset -2000
    repeat
    
screen ending_lyrics(lyric):
    frame:
        background None
        xalign 0.5
        yalign 0.85

        text lyric:
            size 30
            color "#FFFFFF"
            outlines [(2, "#000000", 0, 0)]
            text_align 0.5
            xalign 0.5
            
screen ending_credits():

    frame:
        xalign 0.0001
        yalign 0.5
        xsize 430
        ysize 750
        background "#00000099"
        padding (20, 20)
        
        vbox:
            xalign 0.5
            spacing 35
            at credits_scroll
            
            text "GROUP 3 GAME PROGRAMMING":
                size 35
                color "#FFFFFF"
                xalign 0.5

            text "TEAM LEADER":
                size 25
                color "#bbf6f9"
                xalign 0.5
            text "Aisyah Currents":
                size 22
                color "#FFFFFF"
                xalign 0.5

            text "PROGRAMMERS":
                size 25
                color "#bbf6f9"
                xalign 0.5
            text "@rentsaisy":
                size 22
                color "#FFFFFF"
                xalign 0.5
            text "@sfins":
                size 22
                color "#FFFFFF"
                xalign 0.5
            text "@deazhraa":
                size 22
                color "#FFFFFF"
                xalign 0.5

            text "STORY WRITER":
                size 25
                color "#bbf6f9"
                xalign 0.5
            text "Aisyah Currents":
                size 22
                color "#FFFFFF"
                xalign 0.5

            text "CHARACTERS":
                size 25
                color "#bbf6f9"
                xalign 0.5
            text "Katerine Ivanovna":
                size 22
                color "#FFFFFF"
                xalign 0.5
            text "Sonya Marmeladova":
                size 22
                color "#FFFFFF"
                xalign 0.5
            text "Ivan Karamoz ":
                size 22
                color "#FFFFFF"
                xalign 0.5
            text "Alexei Karamoz":
                size 22
                color "#FFFFFF"
                xalign 0.5
            text "Oscar Wilde":
                size 22
                color "#FFFFFF"
                xalign 0.5
            text "Albert Camus":
                size 22
                color "#FFFFFF"
                xalign 0.5
            text "Franz Kafka":
                size 22
                color "#FFFFFF"
                xalign 0.5
            text "Agatha Christie":
                size 22
                color "#FFFFFF"
                xalign 0.5
            text "Little Fox Blushfen":
                size 22
                color "#FFFFFF"
                xalign 0.5
                
            text "BACKGROUND DESIGN":
                size 25
                color "#bbf6f9"
                xalign 0.5
            text "Adam Safinas":
                size 22
                color "#FFFFFF"
                xalign 0.5

            text "CHARACTER DESIGN":
                size 25
                color "#bbf6f9"
                xalign 0.5
            text "Aisyah Currents":
                size 22
                color "#FFFFFF"
                xalign 0.5
                
            text "AUDIO AND MUSIC COMPOSER":
                size 25
                color "#bbf6f9"
                xalign 0.5
            text "Ella Dea Azahra":
                size 22
                color "#FFFFFF"
                xalign 0.5
            text "Adam Safinas":
                size 22
                color "#FFFFFF"
                xalign 0.5
                
            text "BACKGROUND SOUND":
                size 25
                color "#bbf6f9"
                xalign 0.5
            text "Waiting To Wake Up by MARETU":
                size 22
                color "#FFFFFF"
                xalign 0.5

            text "ENDING SONG AND SINGER":
                size 25
                color "#bbf6f9"
                xalign 0.5
            text "I wont say im in love cover by Ella Dea Azahra":
                size 22
                color "#FFFFFF"
                xalign 0.5
                
            text "LECTURER":
                size 25
                color "#bbf6f9"
                xalign 0.5
            text "Dimas Novian Aditia Syahputra, S.Tr.T., M.Tr.T.":
                size 22
                color "#FFFFFF"
                xalign 0.5
                
            text "FLAMMA NOIR":
                size 35
                color "bbf6f9"
                xalign 0.5

image investigation_room4:
    "images/TM/tmidle.png"
    pause 0.5
    "images/TM/tmidle1.png"
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

image fight_mastermind:
    "images/TM/tmfight.png"
    pause 0.7
    "images/TM/tmfight1.png"
    pause 0.7
    "images/TM/tmfight2.png"
    pause 0.7
    repeat
    
image lose_mastermind:
    "images/TM/tmlose.png"
    pause 0.7
    "images/TM/tmlose1.png"
    pause 0.7
    repeat
        
image win_mastermind:
    "images/TM/tmwin.png"
    pause 0.7
    "images/TM/tmwin1.png"
    pause 0.7
    "images/TM/tmwin2.png"
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
    
# ===== mastermind SYSTEM =====
default player_x4 = 700
default player_y4 = 500
default player_sitting4 = False
default evidence_found4 = False
default evidence_open4= False
default player_direction4 = "down"
default PLAYER_SPEED4 = 20
define INTERACTION_RADIUS4 = 50

define COMPUTER_X4 = 780
define COMPUTER_Y4 = 390
define CHAIR_X4 = 1250
define CHAIR_Y4 = 410

default mastermind_hearts = 3
default mastermind_state = "playing"
default mastermind_round = 0
default mastermind_question = ""
default mastermind_choices = []
default mastermind_message = ""
default mastermind_mastermind_type = ""

init python:

    # ===== mastermind QUESTION DATA =====

    MASTERMIND_ROUNDS = [

        # ROUND 1 - THE FLAMMA PROJECT
        {
            "mastermind": "forensic",
            "question": "What does the FLAMMA project file found on The Ghost`s flash drive tell you?",
            "choices": [
                ("It reveals a plan to establish a new conservation center for the Blushfen.", "integrity"),
                ("It contains a list of wealthy collectors interested in purchasing rare Blushfen.", "intelligence"),
                ("It is simply a proposal for expanding your uncle's existing conservation center.", "forensic")
            ]
        },

        # ROUND 2 - THE OLD NEWSPAPER
        {
            "mastermind": "intelligence",
            "question": "Why do you think I once brought our uncle to court, as reported in this old newspaper?",
            "choices": [
                ("You wanted to claim ownership of his forest for your own commercial interests.", "intelligence"),
                ("You had discovered his illegal transactions involving protected Blushfen and wanted to expose them.", "forensic"),
                ("You wanted to sue him because he refused to support your FLAMMA project.", "integrity")
            ]
        },

        # ROUND 3 - THE FAILED LAWSUIT
        {
            "mastermind": "integrity",
            "question": "If you already knew about his illegal activities, why do you think your lawsuit against him failed?",
            "choices": [
                ("Your uncle had enough influence and evidence to win the case, allowing his illegal operations to remain hidden.", "intelligence"),
                ("You eventually withdrew the lawsuit because you no longer cared about the Blushfen.", "forensic"),
                ("Your uncle had proven that the Blushfen were never part of his conservation activities.", "integrity")
            ]
        },

        # ROUND 4 - THE STUFFED BLUSHFEN
        {
            "mastermind": "forensic",
            "question": "What does this stuffed Blushfen suggest about the illegal transactions happening at the old conservation center?",
            "choices": [
                ("Protected Blushfen were being treated as valuable commodities, even becoming possessions and accessories.", "integrity"),
                ("The conservation center was preserving deceased Blushfen for educational purposes.", "intelligence"),
                ("The stuffed Blushfen must have been made by an unrelated taxidermist.", "forensic")
            ]
        },

        # ROUND 5 - THE ILLEGAL OPERATION
        {
            "mastermind": "intelligence",
            "question": "What was the real contradiction behind our uncle's conservation center?",
            "choices": [
                ("It claimed to protect the Blushfen while secretly participating in illegal transactions involving them.", "forensic"),
                ("It was struggling financially because the Blushfen were too difficult to care for.", "intelligence"),
                ("It was planning to transfer all its animals to another conservation center.", "integrity")
            ]
        },

        # ROUND 6 - THE REASON BEHIND THE FIRE
        {
            "mastermind": "integrity",
            "question": "Why did I choose to burn the forest instead of confronting our uncle through another legal battle?",
            "choices": [
                ("You wanted the old conservation center to collapse financially, clearing the way for FLAMMA.", "intelligence"),
                ("You wanted to eliminate every trace of the Blushfen so nobody could investigate their illegal trade.", "forensic"),
                ("You wanted to scare your uncle into giving you ownership of the forest.", "integrity")
            ]
        },

        # ROUND 7 - THE FLAMMA'S PURPOSE
        {
            "mastermind": "forensic",
            "question": "How was the FLAMMA project supposed to be different from our uncle`s conservation center?",
            "choices": [
                ("It was intended to provide the Blushfen with a genuinely safe habitat, free from illegal exploitation.", "integrity"),
                ("It would continue the same operations but under a new company name.", "intelligence"),
                ("It would turn the Blushfen into a profitable attraction for wealthy visitors.", "forensic")
            ]
        },

        # ROUND 8 - THE HUMAN CONSEQUENCES
        {
            "mastermind": "integrity",
            "question": "Did I ever consider what would happen to the people living near the forest when I started the fire?",
            "choices": [
                ("You prioritized destroying the old conservation center without properly considering the danger to nearby enviroment.", "intelligence"),
                ("You had ensured that everyone nearby had been evacuated before the fire started.", "forensic"),
                ("You believed the fire would remain confined to the conservation center.", "integrity")
            ]
        },

        # ROUND 9 - THE BLUSHFEN'S FATE
        {
            "mastermind": "intelligence",
            "question": "If FLAMMA was meant to save the Blushfen, why did I plan put the very species you wanted to protect in danger?",
            "choices": [
                ("You treated the destruction of their existing habitat as an acceptable sacrifice for building a new one.", "forensic"),
                ("You never intended to protect the Blushfen in the first place.", "integrity"),
                ("You assumed all the Blushfen had already been relocated before the fire.", "intelligence")
            ]
        },

        # ROUND 10 - THE MORAL RESPONSIBILITY
        {
            "mastermind": "integrity",
            "question": "After everything that happened, can I still claim that my actions were justified simply because I wanted to protect the Blushfen?",
            "choices": [
                ("No. Your intentions may have been good, but deliberately causing a fire that endangered both humans and Blushfen cannot be justified.", "intelligence"),
                ("Yes. Your goal was more important than the consequences, because FLAMMA could eventually save the species.", "forensic"),
                ("Yes. The real blame belongs entirely to your uncle, since his illegal activities started this conflict.", "integrity")
            ]
        }

    ]

    # ===== LOAD QUESTION =====
    def load_mastermind_round():

        current = MASTERMIND_ROUNDS[store.mastermind_round]

        store.mastermind_mastermind_type = current["mastermind"]
        store.mastermind_question = current["question"]
        store.mastermind_choices = current["choices"]
        
    # ===== START mastermind =====
    def start_mastermind():

        store.player_sitting4 = True
        store.mastermind_hearts = 3
        store.mastermind_round = 0
        store.mastermind_state = "playing"
        store.mastermind_message = ""

        load_mastermind_round()


    # ===== TOGGLE SIT =====

    def toggle_sit4():

        if store.player_sitting4:

            store.player_sitting4 = False
            store.mastermind_state = "playing"
            store.mastermind_message = ""

        else:
            start_mastermind()


    # ===== ANSWER QUESTION =====

    def answer_type4(choice):

        if store.mastermind_state != "playing":
            return

        mastermind = store.mastermind_mastermind_type
        
        # Same type: retry
        if choice == mastermind:

            store.mastermind_message = "Same type! Try another answer."
            store.mastermind_state = "retry"

            renpy.restart_interaction()
            return

        winning_type = {
            "forensic": "integrity",
            "integrity": "intelligence",
            "intelligence": "forensic"
        }

        # Correct answer
        if winning_type[mastermind] == choice:

            store.mastermind_state = "win_anim"

        # Wrong answer
        else:

            store.mastermind_hearts = max(
                0, store.mastermind_hearts - 1
            )

            store.mastermind_state = "lose_anim"

        renpy.restart_interaction()


    # ===== FINISH WIN ANIMATION =====

    def finish_win_animation4():

        store.mastermind_round += 1

        if store.mastermind_round >= len(MASTERMIND_ROUNDS):

            store.mastermind_state = "game_win"

        else:

            load_mastermind_round()
            store.mastermind_state = "playing"
            store.mastermind_message = ""

        renpy.restart_interaction()


    # ===== FINISH LOSE ANIMATION =====

    def finish_lose_animation4():

        if store.mastermind_hearts <= 0:

            store.mastermind_state = "game_over"

        else:

            store.mastermind_state = "playing"
            store.mastermind_message = ""

        renpy.restart_interaction()


    # ===== TRY AGAIN =====

    def try_again4():

        start_mastermind()

screen exploration_room4():

    modal True

    # Background 
    add "investigation_room4"
            
    if player_direction4 == "up":
        add "player_walk_up":
            xpos player_x4
            ypos player_y4
            xanchor 0.8
            yanchor 0.5

    elif player_direction4 == "down":
        add "player_walk_down":
            xpos player_x4
            ypos player_y4
            xanchor 0.8
            yanchor 0.5

    elif player_direction4 == "left":
        add "player_walk_left":
            xpos player_x4
            ypos player_y4
            xanchor 0.8
            yanchor 0.5

    elif player_direction4 == "right":
        add "player_walk_right":
            xpos player_x4
            ypos player_y4
            xanchor 0.8
            yanchor 0.5

    # Player Movements
    if not player_sitting4 and not evidence_open4:

        # LEFT - A
        key "K_LEFT" action [
            SetVariable("player_x4", max(590, player_x4 - PLAYER_SPEED4)),
            SetVariable("player_direction4", "left")
        ]
        key "K_a" action [
            SetVariable("player_x4", max(590, player_x4 - PLAYER_SPEED4)),
            SetVariable("player_direction4", "left")
        ]

        # RIGHT - D
        key "K_RIGHT" action [
            SetVariable("player_x4", min(1600, player_x4 + PLAYER_SPEED4)),
            SetVariable("player_direction4", "right")
        ]
        key "K_d" action [
            SetVariable("player_x4", min(1600, player_x4 + PLAYER_SPEED4)),
            SetVariable("player_direction4", "right")
        ]

        # UP - W
        key "K_UP" action [
            SetVariable("player_y4", max(380, player_y4 - PLAYER_SPEED4)),
            SetVariable("player_direction4", "up")
        ]
        key "K_w" action [
            SetVariable("player_y4", max(380, player_y4 - PLAYER_SPEED4)),
            SetVariable("player_direction4", "up")
        ]

        # DOWN - S
        key "K_DOWN" action [
            SetVariable("player_y4", min(520, player_y4 + PLAYER_SPEED4)),
            SetVariable("player_direction4", "down")
        ]
        key "K_s" action [
            SetVariable("player_y4", min(520, player_y4 + PLAYER_SPEED4)),
            SetVariable("player_direction4", "down")
        ]

    # ===== mastermind ANIMATION: DRAW FIRST =====

    if player_sitting4:

        if mastermind_state in ("playing", "retry"):
            add "fight_mastermind":
                xalign 0.78
                yalign 0.60

        elif mastermind_state == "win_anim":
            add "lose_mastermind":
                xalign 0.78
                yalign 0.60

            timer 2.1 action Function(finish_win_animation4)

        elif mastermind_state == "lose_anim":
            add "win_mastermind":
                xalign 0.78
                yalign 0.60

            timer 2.1 action Function(finish_lose_animation4)

    # ===== HEARTS: TOP RIGHT =====
    if player_sitting4 and mastermind_state not in ("game_over", "game_win"):

        hbox:
            xalign 0.97
            yalign 0.02
            spacing 5

            for i in range(mastermind_hearts):
                add "images/heart.png":
                    xsize 40
                    ysize 40
              # ===== mastermind QUESTION BUBBLE =====

    if player_sitting4 and mastermind_state in ("playing", "retry"):

        frame:
            xpos 60
            ypos 50
            xsize 650
            background "#18212df2"
            xpadding 25
            ypadding 20

            vbox:
                spacing 10

                text "[mastermind_round + 1] / 10":
                    size 18
                    color "#aaaaaa"

                text "THE MASTERMIND":
                    size 18
                    color (
                        "#56aaff" if mastermind_mastermind_type == "forensic"
                        else "#65e68a" if mastermind_mastermind_type == "integrity"
                        else "#ff83cf"
                    )

                text mastermind_question:
                    size 24
                    color "#ffffff"


    # ===== THREE CHOICE BUBBLES =====

    if player_sitting4 and mastermind_state in ("playing", "retry"):

        vbox:
            xpos 60
            ypos 230
            xsize 650
            spacing 15

            for choice_text, choice_type in mastermind_choices:

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

                    action Function(answer_type4, choice_type)
        
    # ===== FOX RETRY MESSAGE =====
    if player_sitting4 and mastermind_state == "retry":

        add "images/chara/C_Fox.png":
            xalign 0.9
            yalign 1.0
            zoom 0.2

        text mastermind_message:
            xpos 500
            ypos 670
            size 25
            color "#ffffff"
            
        timer 1.5 action [
            SetVariable("mastermind_state", "playing"),
            SetVariable("mastermind_message", "")
        ]
    # ===== GAME OVER SCREEN =====
    if mastermind_state == "game_over":

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
                action Function(try_again4)

            textbutton "HOME":
                xalign 0.5
                text_size 28
                action MainMenu(confirm=False)
                    
    # ===== GAME WIN =====
    if mastermind_state == "game_win":

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
                action Jump("after_battle4")
                
    # Interaksi komputer
    if not player_sitting4 and not evidence_open4:

        if (player_x4 - COMPUTER_X4) ** 2 + (player_y4 - COMPUTER_Y4) ** 2 < INTERACTION_RADIUS4 ** 2:

            textbutton "Inspect ( E )":
                xpos 180
                ypos 270
                text_size 16
                xpadding 8
                ypadding 4
                action SetVariable("evidence_open4", True)

            key "e" action SetVariable("evidence_open4", True)

    # Interaksi kursi
    if not evidence_open4:

        if (player_x4 - CHAIR_X4) ** 2 + (player_y4 - CHAIR_Y4) ** 2 < INTERACTION_RADIUS4 ** 2:

            textbutton (" " if player_sitting4 else "Sit Down ( E )"):
                xpos 850
                ypos 300
                text_size 16
                xpadding 8
                ypadding 4
                action Function(toggle_sit4)

            key "e" action Function(toggle_sit4)
            
    
    if evidence_open4:

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

                            add "images/Evi/em1.png":
                                xalign 0.5
                                fit "contain"
                                xysize (200, 200)

                            text "1. Old News Paper" size 18

                    # Evidence 2
                    frame:
                        xsize 270
                        ysize 270
                        background "#303d4d"
                        padding [12, 12, 12, 12]

                        vbox:
                            spacing 10

                            add "images/Evi/em2.png":
                                xalign 0.5
                                fit "contain"
                                xysize (200, 200)

                            text "2. A Project Flamma file" size 18

                    # Evidence 3
                    frame:
                        xsize 270
                        ysize 270
                        background "#303d4d"
                        padding [12, 12, 12, 12]

                        vbox:
                            spacing 10

                            add "images/Evi/em3.png":
                                xalign 0.5
                                fit "contain"
                                xysize (200, 200)

                            text "3. A stuffed Blushfen" size 18

                textbutton "Close":
                    xalign 1.0
                    action SetVariable("evidence_open4", False)

    key "K_ESCAPE" action Return()
               
label fourthscene:
    scene BGO
    "The investigation team finally traces the source behind The Burner, The Bribe, and The Ghost."
    show sonya:
        xalign 1.0
        yalign 0.1
        zoom 0.256
    Sonya "KATERINEEE!! THE GHOST DIDN`T HURT YOU RIGHT?."
    hide sonya
    show m_sonya:
        xalign 1.0
        yalign 0.1
        zoom 0.256
    show katerine:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Katerine "Sonya.. It is fine."
    hide katerine
    hide m_sonya
    with dissolve
    show alexei:
        xalign 0.5
        yalign 0.3
        zoom 0.232
    Alexei "So how can we meet the mastermind, Katerine?"
    hide alexei
    show katerine:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Katerine "I-"
    hide katerine
    show alexei:
        xalign 0.5
        yalign 0.3
        zoom 0.232
    Alexei "Hm?"
    hide alexei
    show katerine:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Katerine "I- I-"
    hide katerine
    show sonya:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Sonya "Hey..Katerine.. Calm Down."
    hide sonya
    show alexei:
        xalign 0.5
        yalign 0.3
        zoom 0.232
    Alexei "Is it because you cut off your sister?"
    hide alexei
    show sonya:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Sonya "Sister?"
    hide sonya
    show katerine:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Katerine "The mastermind- The mastermind is my older sister. Our parents got divorce and we got different last name.. Agatha Christie, The reason why I cut her off because.. She`s always been obsessed with acquiring ownership of the forest where the Blushfen live. She even once sued our uncle, who owns the forest, but he won the case. And I feel that if she`s capable of hurting our uncle, she could hurt me too. So, it`s better to stay away from her."
    hide katerine
    show ivan:
        xalign 0.5
        yalign 0.3
        zoom 0.232
    Ivan "Why she sued your uncle?"
    hide ivan
    show katerine:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Katerine "I don`t know about it."
    hide katerine
    show alexei:
        xalign 0.5
        yalign 0.3
        zoom 0.232
    Alexei "Okay I already send a black mail to her."
    hide alexei
    show katerine:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Katerine "What? How?"
    hide katerine
    show alexei:
        xalign 0.5
        yalign 0.3
        zoom 0.232
    Alexei "She`s pretty famous in fashion right?, so of course her data is so easy."
    hide alexei
    show katerine:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Katerine "What do send to her?"
    hide katerine
    show alexei:
        xalign 0.5
        yalign 0.3
        zoom 0.232
    Alexei "I just ask her to go the court tomorrow to prove that she is not the mastermind. I also mention about the blushfen we have.. and look she is agreed."
    hide alexei
    show katerine:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Katerine "Alright, let`s find more evidences."
    hide katerine
    
    scene BGC
    "The room is quiet."
    "A woman sits calmly beside a large window overlooking the forest."
    scene black
    show em3:
        xalign 0.5
        yalign 0.5
        zoom 1.0
    "She got a stuffed Blushfen on her lap." 
    hide em3
    scene BGC
    show agatha:
        xalign 0.5
        yalign 0.3
        zoom 0.232     
    Agatha "I was wondering when you would arrive."
    hide agatha
    show katerine:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Katerine "You`re the one behind the forest arson."
    hide katerine
    show agatha:
        xalign 0.5
        yalign 0.3
        zoom 0.232 
    Agatha "Behind it?"
    "She smiles."
    Agatha "I simply gave people a reason to do what they were already willing to do."
    hide agatha
    show katerine:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Katerine "You destroyed an entire forest for money."
    hide katerine
    show agatha:
        xalign 0.5
        yalign 0.3
        zoom 0.232 
    Agatha "Money? Oh darling.. Is your sister look like someone who needs money?"
    hide agatha
    show fox:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    "She touches the Blushfen."
    Fox "???" #confused
    hide fox
    show agatha:
        xalign 0.5
        yalign 0.3
        zoom 0.232 
    Agatha "No."
    Agatha "Katerine, did you know why I sued our uncle?."
    hide agatha
    show katerine:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Katerine "Why?"
    hide katerine
    scene black
    show em1:
        xalign 0.5
        yalign 0.5
        zoom 1.0  
    Agatha "Try to read this."
    hide em1
    scene BGC
    show katerine:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Katerine "You took our uncle to court because he was involved in an illegal Blushfen transactions?"
    hide katerine
    show agatha:
        xalign 0.5
        yalign 0.3
        zoom 0.232 
    Agatha "Yeah, That forest wasn`t really protect them. He wins because the evidences are not strong enough and I wish the NOIR was there.. But you`re still a child Katerine."
    hide agatha
    show katerine:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Katerine "So the FLAMMA project is for-"
    hide katerine
    show agatha:
        xalign 0.5
        yalign 0.3
        zoom 0.232 
    Agatha "Let me take off this hat and coat before we begin the investigation."
    jump investigation_room4

label investigation_room4:
    play music "audio/bgm/home-battle.wav" fadein 1.0
    call screen exploration_room4
    return

label after_battle4:
    stop music fadeout 1.0
    scene BGC
    "The room becomes quiet."
    scene S4_1
    "She stares at it for a moment."
    Agatha "So.."
    Agatha "This is where it ends."
    Katerine "Yes"
    Agatha "After everything you`ve seen.."
    Agatha "After everything you`ve uncovered.."
    Agatha "Tell me something."
    Agatha "Have you ever felt regret?"
    "The MC remains silent."
    scene S4_21
    Katerine "I have never regretted what I have done."
    Katerine "Because everything I have done, I did with a clear conscience."
    scene S4_22
    Katerine "I stood for truth."
    scene S4_23
    Katerine "For justice."
    Katerine "For honesty."
    Katerine "And for humanity."
    scene S4_21
    Katerine "So no.."
    Katerine "I have never regretted my choices."
    scene S4_22
    Katerine "If the day comes when I must face death, I want to leave this world without regrets."
    Katerine "That is the art of dying well."
    Katerine "To live by what you believe in..."
    Katerine "And to die knowing you never betrayed it."
    scene BGC
    show agatha:
        xalign 0.5
        yalign 0.3
        zoom 0.232 
    "The Mastermind says nothing."
    Agatha "My dear sister, you`re smart. I`ll take every consciences."
    hide agatha
    scene black
    "The Field Investigator approaches and places handcuffs on The Mastermind."
    scene SA
    "The NOIR go to outside the court."
    Sonya "LOOK EVERYONE!! LOOK!!"
    Ivan "The sky is very clear."
    scene SB
    Katerine "Yeah. It`s very different with the night after forest arson."
    scene SA
    Ivan "Do you think the forest will recover?"
    Katerine "Agatha said she will take full responsibility for what she have done."
    Fox "Yip Yip" #happy
    Katerine "After all FLAMMA project was to protect Blushfen, but she did it in very dumb way."
    scene S4_3
    Katerine "Thank you for your help"
    scene S4_4
    Katerine "everyone.."
    window hide
    scene SA

    # Black transparent overlay
    show expression Solid("#00000099") as ending_overlay

    show text "{color=#FFFFFF}{size=40}CASE CLOSED{/size}{/color}" at truecenter
    pause
    hide text

    show text "{color=#FFFFFF}{size=30}After Agatha Christie was freed, she began the FLAMMA project and invited NOIR to contribute.{/size}{/color}" at truecenter
    pause
    hide text

    show text "{color=#FFFFFF}{size=35}The FLAMMA project would become a new home for them...{/size}{/color}" at truecenter
    pause
    hide text

    hide ending_overlay
    play music "audio/ending.mp3"
    show END at ending_zoom
    with dissolve
    show screen ending_credits 

    show screen ending_lyrics("If there`s a prize for rotten judgment")
    pause 5.0
    show screen ending_lyrics("I guess the tycoons have won that")
    pause 5.0
    show screen ending_lyrics("No plot is worth the smog and burnin`")
    pause 5.0
    show screen ending_lyrics("That`s ancient timber, gone down in ash flat")
    pause 4.0

    show screen ending_lyrics("Who`d they think they`re trickin`?")
    pause 2.0
    show screen ending_lyrics("They just burned the earth and heaven")
    pause 2.0
    show screen ending_lyrics("Try to grease the docket")
    pause 2.0
    show screen ending_lyrics("Honey, we can see right through them")
    pause 2.0
    show screen ending_lyrics("They can`t just conceal it")
    pause 2.0
    show screen ending_lyrics("All the lungs can feel it")
    pause 2.0
    show screen ending_lyrics("Who they`re clearin` for")
    pause 4.0 

    show screen ending_lyrics("No chance, no way")
    pause 2.0
    show screen ending_lyrics("I won`t call this natural") 
    pause 2.0
    show screen ending_lyrics("The skies run dry")
    pause 2.0
    show screen ending_lyrics("Why deny it? Uh-oh")
    pause 2.0
    show screen ending_lyrics("It`s arson`s play")
    pause 2.0
    show screen ending_lyrics("I won`t call this bad luck")
    pause 5.0

    show screen ending_lyrics("I thought the courts had learned their lesson") 
    pause 5.0
    show screen ending_lyrics("It sounds so clean when they draft laws") 
    pause 4.0
    show screen ending_lyrics("My head is screaming, ``Seize the permits``")
    pause 3.0
    show screen ending_lyrics("Unless you`re dyin` to")
    pause 2.0

    show screen ending_lyrics("Drop the whole case")
    pause 2.0

    show screen ending_lyrics("They keep on denyin`")
    pause 2.0
    show screen ending_lyrics("Who sparked up the peatland forest")
    pause 2.0
    show screen ending_lyrics("Baby, we`re not buyin`")
    pause 2.0
    show screen ending_lyrics("Hon, the satellite`s before us") 
    pause 2.0
    show screen ending_lyrics("Face them in the docket")
    pause 2.0
    show screen ending_lyrics("Empty out their pocket")
    pause 2.0
    show screen ending_lyrics("Make `em pay, pay, pay the fines!")
    pause 3.0

    show screen ending_lyrics("No chance, no way")
    pause 2.0
    show screen ending_lyrics("I won`t let them walk, no")
    pause 2.0
    show screen ending_lyrics("Give up the bribes")
    pause 2.0
    show screen ending_lyrics("Read the files, they`re in court")
    pause 2.0
    show screen ending_lyrics("Their plea won`t play")
    pause 2.0
    show screen ending_lyrics("I won`t call this bad luck")
    pause 2.0
    show screen ending_lyrics("They struck the match")
    pause 2.0
    show screen ending_lyrics("Read our lips, hold the line")
    pause 2.0

    show screen ending_lyrics("You`re way off base")
    pause 2.0
    show screen ending_lyrics("I won`t settle")
    pause 2.0
    show screen ending_lyrics("Clear out the haze") 
    pause 2.0
    show screen ending_lyrics("Sue the lobby")
    pause 2.0
    show screen ending_lyrics("Don`t drop the charge")
    pause 2.0
    show screen ending_lyrics("Gavel down, face the law")
    pause 3.0

    show screen ending_lyrics("Oh")
    pause 3.0
    show screen ending_lyrics("At least out loud")
    pause 4.0
    show screen ending_lyrics("I won`t let them walk free")
    pause 7.0
    hide screen ending_lyrics
    hide screen ending_credits
    stop music fadeout 3.0
    $ persistent.scene_4_complete = True
    $ renpy.save_persistent()
    return