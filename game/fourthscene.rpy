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

        # viewport:
        #     xfill True
        #     yfill True
        #     scrollbars None
        #     mousewheel False
        #     draggable False

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
                
            text "MALE VOICE OVER":
                size 25
                color "#bbf6f9"
                xalign 0.5
            text "Adam Safinas":
                size 22
                color "#FFFFFF"
                xalign 0.5
            text "FEMALE VOICE OVER":
                size 25
                color "#bbf6f9"
                xalign 0.5
            text "Aisyah Currents":
                size 22
                color "#FFFFFF"
                xalign 0.5

            text "SONG AND SINGER":
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
                    
label fourthscene:
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

    return