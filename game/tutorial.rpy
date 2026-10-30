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
default enemy_question = "1 + 1?"

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
                add "images/heart.png":
                    xsize 40
                    ysize 40
                              
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

            textbutton "1 + 1":
                text_size 20
                text_color "#56aaff"
                background "#18212df2"
                hover_background "#ffffff"
                xpadding 25
                ypadding 12
                action Function(answer_type, "forensic")

            textbutton "2":
                text_size 20
                text_color "#65e68a"
                background "#18212df2"
                hover_background "#ffffffff"
                xpadding 25
                ypadding 12
                action Function(answer_type, "integrity")

            textbutton "0":
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

# SCENE BATTLE TUTORIAL
define Fox = Character('Little Fox', color="#ec7599")  #PINK
image fox = "images/C_Fox.png"
image foren = "images/EForensic.png"
image intel = "images/EIntelligence.png"
image integ = "images/EIntegrity.png"
image battle = "images/bgbattle.png"

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
 
label tutorial:
    scene battle
    show fox:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Fox "Welcome to Tutorial Gameplay."
    Fox "Let me introduce you to our argument types."
    hide fox 
    show foren at move_forensics
    Fox "Forensic"
    show intel at move_intelligence
    Fox "Intelligence"
    show integ at move_integrity
    Fox "Integrity"
    Fox "Forensics is strong against Intelligence, Integrity is strong against Forensics, And Intelligence is strong against Integrity."
    show fox:
        xalign 0.5
        yalign 0.1
        zoom 0.256
    Fox "In this battle, you will use arguments to defeat your opponent."
    Fox "Each argument has a type and can counter another type like in the explaination before."
    Fox "Let`s begin."
    hide fox
    hide foren
    hide intel
    hide integ
    with dissolve
    jump investigation_room_tutorial
    
label investigation_room_tutorial:
    
    call screen exploration_room_tutorial
    
    return