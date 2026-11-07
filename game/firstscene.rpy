# SCENE 1

# Scenes pic
image sonya = "images/chara/C_Lead_Investigator.png"
image m_sonya = "images/chara/C_Lead_Investigator_Mute.png"
image katerine = "images/chara/C_Main_Character.png"
image m_katerine = "images/chara/C_Main_Character_Mute.png"
image ivan = "images/chara/C_Field_Investigator.png"
image m_ivan = "images/chara/C_Field_Investigator_Mute.png"
image alexei = "images/chara/C_Technical_Investigator.png"
image m_alexei = "images/chara/C_Technical_Investigator_Mute.png"
image oscar = "images/chara/V_The_Burner.png"
image m_oscar = "images/chara/V_The_Burner_Mute.png"

image e1 = "images/Evi/eb1.png"
image e2 = "images/Evi/eb2.png"
image e3 = "images/Evi/eb3.png"
image e4 = "images/Evi/ebri1.png"

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
image S1_8 = "images/S1_8.png"

image investigation_room:
    "images/TB/tbidle.png"
    pause 0.5
    "images/TB/tbidle1.png"
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

image fight_burner:
    "images/TB/tbfight.png"
    pause 0.7
    "images/TB/tbfight1.png"
    pause 0.7
    "images/TB/tbfight2.png"
    pause 0.7
    repeat
    
image lose_burner:
    "images/TB/tblose.png"
    pause 0.7
    "images/TB/tblose1.png"
    pause 0.7
    repeat
        
image win_burner:
    "images/TB/tbwin.png"
    pause 0.7
    "images/TB/tbwin1.png"
    pause 0.7
    "images/TB/tbwin2.png"
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
    
# ===== burner SYSTEM =====
default player_x1 = 700
default player_y1 = 500
default player_sitting1 = False
default evidence_found1 = False
default evidence_open1 = False
default player_direction1 = "down"
default PLAYER_SPEED1 = 20
define INTERACTION_RADIUS1 = 50

define COMPUTER_X1 = 780
define COMPUTER_Y1 = 390
define CHAIR_X1 = 1250
define CHAIR_Y1 = 410

default burner_hearts = 3
default burner_state = "playing"
default burner_round = 0
default burner_question = ""
default burner_choices = []
default burner_message = ""
default burner_burner_type = ""
# burner question

init python:

    # ===== burner QUESTION DATA =====

    BURNER_ROUNDS = [

        # ROUND 1 - RARE FOX
        {
            "burner": "intelligence",
            "question": "Why do you think a rare fox was found near the burned forest?",
            "choices": [
                ("It might have been trying to escape the fire and find a safer place.", "forensic"),
                ("Someone probably brought it there as a pet.", "integrity"),
                ("It must have been responsible for starting the fire.", "intelligence")
            ]
        },

        # ROUND 2 - WET SLEEVES AND GASOLINE
        {
            "burner": "forensic",
            "question": "My sleeves were wet and smelled of gasoline. What does that tell you?",
            "choices": [
                ("You were probably trying to put out the fire.", "forensic"),
                ("You may have used gasoline as an accelerant to spread the fire.", "integrity"),
                ("You must have accidentally spilled gasoline while working nearby.", "intelligence")
            ]
        },

        # ROUND 3 - THE NECKLACE
        {
            "burner": "intelligence",
            "question": "Why would someone keep a photograph of their loved one so close to their heart?",
            "choices": [
                ("Perhaps it reminds you of someone you are trying to protect.", "forensic"),
                ("You probably stole the necklace from someone.", "integrity"),
                ("It could be a reminder of the person who gave you the money.", "intelligence")
            ]
        }
    ]


    # ===== LOAD QUESTION =====
    def load_burner_round():

        current = BURNER_ROUNDS[store.burner_round]

        store.burner_burner_type = current["burner"]
        store.burner_question = current["question"]
        store.burner_choices = current["choices"]
        
    # ===== START burner =====
    def start_burner():

        store.player_sitting1 = True
        store.burner_hearts = 3
        store.burner_round = 0
        store.burner_state = "playing"
        store.burner_message = ""

        load_burner_round()


    # ===== TOGGLE SIT =====

    def toggle_sit1():

        if store.player_sitting1:

            store.player_sitting1 = False
            store.burner_state = "playing"
            store.burner_message = ""

        else:
            start_burner()


    # ===== ANSWER QUESTION =====

    def answer_type1(choice):

        if store.burner_state != "playing":
            return

        burner = store.burner_burner_type
        
        # Same type: retry
        if choice == burner:

            store.burner_message = "Same type! Try another answer."
            store.burner_state = "retry"

            renpy.restart_interaction()
            return

        winning_type = {
            "forensic": "integrity",
            "integrity": "intelligence",
            "intelligence": "forensic"
        }

        # Correct answer
        if winning_type[burner] == choice:

            store.burner_state = "win_anim"

        # Wrong answer
        else:

            store.burner_hearts = max(
                0, store.burner_hearts - 1
            )

            store.burner_state = "lose_anim"

        renpy.restart_interaction()


    # ===== FINISH WIN ANIMATION =====

    def finish_win_animation1():

        store.burner_round += 1

        if store.burner_round >= len(BURNER_ROUNDS):

            store.burner_state = "game_win"

        else:

            load_burner_round()
            store.burner_state = "playing"
            store.burner_message = ""

        renpy.restart_interaction()


    # ===== FINISH LOSE ANIMATION =====

    def finish_lose_animation1():

        if store.burner_hearts <= 0:

            store.burner_state = "game_over"

        else:

            store.burner_state = "playing"
            store.burner_message = ""

        renpy.restart_interaction()


    # ===== TRY AGAIN =====

    def try_again1():

        start_burner()

screen exploration_room():

    modal True

    # Background 
    add "investigation_room"
            
    if player_direction1 == "up":
        add "player_walk_up":
            xpos player_x1
            ypos player_y1
            xanchor 0.8
            yanchor 0.5

    elif player_direction1 == "down":
        add "player_walk_down":
            xpos player_x1
            ypos player_y1
            xanchor 0.8
            yanchor 0.5

    elif player_direction1 == "left":
        add "player_walk_left":
            xpos player_x1
            ypos player_y1
            xanchor 0.8
            yanchor 0.5

    elif player_direction1 == "right":
        add "player_walk_right":
            xpos player_x1
            ypos player_y1
            xanchor 0.8
            yanchor 0.5

    # Player Movements
    if not player_sitting1 and not evidence_open1:

        # LEFT - A
        key "K_LEFT" action [
            SetVariable("player_x1", max(590, player_x1 - PLAYER_SPEED1)),
            SetVariable("player_direction1", "left")
        ]
        key "K_a" action [
            SetVariable("player_x1", max(590, player_x1 - PLAYER_SPEED1)),
            SetVariable("player_direction1", "left")
        ]

        # RIGHT - D
        key "K_RIGHT" action [
            SetVariable("player_x1", min(1600, player_x1 + PLAYER_SPEED1)),
            SetVariable("player_direction1", "right")
        ]
        key "K_d" action [
            SetVariable("player_x1", min(1600, player_x1 + PLAYER_SPEED1)),
            SetVariable("player_direction1", "right")
        ]

        # UP - W
        key "K_UP" action [
            SetVariable("player_y1", max(380, player_y1 - PLAYER_SPEED1)),
            SetVariable("player_direction1", "up")
        ]
        key "K_w" action [
            SetVariable("player_y1", max(380, player_y1 - PLAYER_SPEED1)),
            SetVariable("player_direction1", "up")
        ]

        # DOWN - S
        key "K_DOWN" action [
            SetVariable("player_y1", min(520, player_y1 + PLAYER_SPEED1)),
            SetVariable("player_direction1", "down")
        ]
        key "K_s" action [
            SetVariable("player_y1", min(520, player_y1 + PLAYER_SPEED1)),
            SetVariable("player_direction1", "down")
        ]

    # ===== burner ANIMATION: DRAW FIRST =====

    if player_sitting1:

        if burner_state in ("playing", "retry"):
            add "fight_burner":
                xalign 0.78
                yalign 0.60

        elif burner_state == "win_anim":
            add "lose_burner":
                xalign 0.78
                yalign 0.60

            timer 2.1 action Function(finish_win_animation1)

        elif burner_state == "lose_anim":
            add "win_burner":
                xalign 0.78
                yalign 0.60

            timer 2.1 action Function(finish_lose_animation1)

    # ===== HEARTS: TOP RIGHT =====
    if player_sitting1 and burner_state not in ("game_over", "game_win"):

        hbox:
            xalign 0.97
            yalign 0.02
            spacing 5

            for i in range(burner_hearts):
                add "images/heart.png":
                    xsize 40
                    ysize 40
              # ===== burner QUESTION BUBBLE =====

    if player_sitting1 and burner_state in ("playing", "retry"):

        frame:
            xpos 60
            ypos 50
            xsize 650
            background "#18212df2"
            xpadding 25
            ypadding 20

            vbox:
                spacing 10

                text "[burner_round + 1] / 3":
                    size 18
                    color "#aaaaaa"

                text "THE BURNER":
                    size 18
                    color (
                        "#56aaff" if burner_burner_type == "forensic"
                        else "#65e68a" if burner_burner_type == "integrity"
                        else "#ff83cf"
                    )

                text burner_question:
                    size 24
                    color "#ffffff"


    # ===== THREE CHOICE BUBBLES =====

    if player_sitting1 and burner_state in ("playing", "retry"):

        vbox:
            xpos 60
            ypos 230
            xsize 650
            spacing 15

            for choice_text, choice_type in burner_choices:

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

                    action Function(answer_type1, choice_type)
        
    # ===== FOX RETRY MESSAGE =====
    if player_sitting1 and burner_state == "retry":

        add "images/chara/C_Fox.png":
            xalign 0.9
            yalign 1.0
            zoom 0.2

        text burner_message:
            xpos 500
            ypos 670
            size 25
            color "#ffffff"
            
        timer 1.5 action [
            SetVariable("burner_state", "playing"),
            SetVariable("burner_message", "")
        ]
    # ===== GAME OVER SCREEN =====
    if burner_state == "game_over":

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
    if burner_state == "game_win":

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
                action Jump("after_battle1")
                
    # Interaksi komputer
    if not player_sitting1 and not evidence_open1:

        if (player_x1 - COMPUTER_X1) ** 2 + (player_y1 - COMPUTER_Y1) ** 2 < INTERACTION_RADIUS1 ** 2:

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

        if (player_x1 - CHAIR_X1) ** 2 + (player_y1 - CHAIR_Y1) ** 2 < INTERACTION_RADIUS1 ** 2:

            textbutton (" " if player_sitting1 else "Sit Down ( E )"):
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

label firstscene:
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
    hide sonya
    show m_sonya:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    show katerine:
        xalign 0.8
        yalign 0.1
        zoom 0.256
    Katerine "Hello everyone. My name is Katerine, I am the new attorney in here."
    hide katerine
    hide m_sonya
    with dissolve
    show sonya:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Sonya "WELCOME TO NOIR KATERINE!"
    Sonya "Let`s introduce ourselves. First, I am the Lead Investigator, responsible for coordinating our investigations."
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
    hide katerine
    show m_katerine:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    show sonya:
        xalign 0.1
        yalign 0.1
        zoom 0.256
    Sonya "YUP! Isn`t it exciting you? I MEAN IT IS YOUR FIRST CASE!"
    Sonya "Find the real culprit at the crime scene. You will be going with Ivan."
    hide sonya
    show m_sonya:
        xalign 0.1
        yalign 0.1
        zoom 0.256
    show ivan:
        xalign 0.9
        yalign 0.3
        zoom 0.232
    Ivan "Huh, Me?"
    hide ivan
    show m_ivan:
        xalign 0.9
        yalign 0.3
        zoom 0.232
    show sonya:
        xalign 0.1
        yalign 0.1
        zoom 0.256
    Sonya "Yup, Tell me what you guys find after that. Good luck for both of you."
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
    Katerine "WAIT ISN`T IT BLUSHFEN?"
    Katerine "This is a protected species! Someone must have burned its habitat to drive up the animal`s market value. We need to find the other Blushfens. They might still be alive, and we could save them from the hands of those cruel people!"
    hide katerine
    show m_katerine:
        xalign 0.1
        yalign 0.1
        zoom 0.256
    show ivan:
        xalign 0.8
        yalign 0.3
        zoom 0.232
    Ivan "Do not jump to conclusions. Look around first!"
    hide m_katerine
    hide ivan
    with dissolve
    "They examine the area but finds nothing useful."
    show AF at shake
    "THUMP!"
    show katerine:
        xalign 0.1
        yalign 0.1
        zoom 0.256
    Katerine "What`s that?!"
    hide katerine
    show oscar:
        xalign 1.0
        yalign 0.3
        zoom 0.232
    Oscar "Ouch! COME HERE YOU LITTLE FOX!"
    hide oscar
    #EVI 1 =====================================
    scene black
    show e1:
        xalign 0.5
        yalign 0.5
        zoom 1.0
    "A Blushfen runs into Katherine`s arms.."    
    hide e1
    scene AF
    # =============================================
    show katerine:
            xalign 0.1
            yalign 0.1
            zoom 0.256
    Katerine "GET BACK! Why are you chasing her?"
    hide katerine
    show m_katerine:
        xalign 0.1
        yalign 0.1
        zoom 0.256
    show oscar:
        xalign 1.0
        yalign 0.3
        zoom 0.232
    Oscar "That`s none of your business. GIVE HER TO ME!"
    hide oscar
    show m_oscar:
        xalign 1.0
        yalign 0.3
        zoom 0.232
    show ivan:
        xalign 0.4
        yalign 0.3
        zoom 0.232
    Ivan "It`s our business, We are from NOIR and our job is doing investigation in here."
    hide ivan
    #EVI 2 =====================================
    scene black
    show e2:
        xalign 0.5
        yalign 0.5
        zoom 1.0
    Ivan "Who are you? also why you smell like gasoline and your sleeve cuffs look wet?"
    hide e2
    scene AF
    # =============================================
    show m_ivan:
        xalign 0.4
        yalign 0.3
        zoom 0.232
    hide m_katerine
    show katerine:
        xalign 0.1
        yalign 0.1
        zoom 0.256
    Katerine "Oscar, are you the mastermind of this forest arson?"
    hide katerine
    show m_katerine:
        xalign 0.1
        yalign 0.1
        zoom 0.256
    hide m_oscar
    show oscar:
        xalign 1.0
        yalign 0.3
        zoom 0.232
    Oscar "WHAT? HOW DO YOU KNOW MY NAME?"
    hide oscar
    show m_oscar:
        xalign 1.0
        yalign 0.3
        zoom 0.232
    hide m_katerine
    #EVI 3 =====================================
    scene black
    show e3:
        xalign 0.5
        yalign 0.5
        zoom 1.0
    Katerine "You dropped this necklace. Now answer my question, are you the-"            
    hide e3
    scene AF
    # =============================================
    show m_katerine:
        xalign 0.1
        yalign 0.1
        zoom 0.256
    hide m_oscar
    show oscar:
        xalign 1.0
        yalign 0.3
        zoom 0.232
    Oscar "GIVE IT BACK TO ME!"
    hide oscar
    hide m_ivan
    show ivan:
        xalign 0.4
        yalign 0.3
        zoom 0.232
    Ivan "Do not touch my partner! You can get that necklace if you follow us. Katerine, begin the investigation!"
    jump investigation_room
    
label investigation_room:
    
    play music "audio/bgm/home-battle.wav" fadein 1.0
    call screen exploration_room
    return

label after_battle1:
    stop music fadeout 1.0
    scene AF
    show oscar:
        xalign 1.0
        yalign 0.3
        zoom 0.232
    Oscar "ALRIGHT! you`re correct I am the burner."
    hide oscar
    scene S1_8
    Oscar "But I do it for my sister, she is sick and I need money so I take this job."
    scene AF
    show m_oscar:
        xalign 1.0
        yalign 0.3
        zoom 0.232
    show katerine:
        xalign 0.1
        yalign 0.1
        zoom 0.256
    Katerine "So the animals in here feels like that too, they`re afraid losing their family. Then Oscar, who is your boss?"
    hide katerine
    hide m_oscar
    show m_katerine:
        xalign 0.1
        yalign 0.1
        zoom 0.256
    #EVI 4 =====================================
    scene black
    show e4:
        xalign 0.5
        yalign 0.5
        zoom 1.0
    Oscar "I can`t say that, I will just give you this"
    hide e3
    scene AF
    show ivan:
        xalign 0.4
        yalign 0.3
        zoom 0.232
    Ivan "Fine, let`s take this guy to the police and we continue our investigation to search the mastermind."    
    hide m_katerine
    hide ivan
    with dissolve
    show m_ivan:
        xalign 0.4
        yalign 0.3
        zoom 0.232
    show katerine:
        xalign 0.1
        yalign 0.1
        zoom 0.256
    Katerine "A Lighter? huh? this symbol.."
    hide m_ivan
    hide katerine
    with dissolve
    scene black
    "They`re going back to NOIR office"
    return