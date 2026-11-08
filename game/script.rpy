init python:

    def reset_scene_progress():

        persistent.scene_1_complete = False
        persistent.scene_2_complete = False
        persistent.scene_3_complete = False
        persistent.scene_4_complete = False

        renpy.save_persistent()

default persistent.scene_1_complete = False
default persistent.scene_2_complete = False
default persistent.scene_3_complete = False
default persistent.scene_4_complete = False


default custom_voice = None

init -1 python:
    renpy.music.register_channel(
        "template_voice",
        mixer="voice",
        loop=True
    )

    def template_voice(event, interact=True, voicefile="audio/voice/male/mul_male.wav", **kwargs ):
        if not interact:
            return
        is_custom = store.custom_voice is not None
        if event == "show":
            renpy.music.play(store.custom_voice or voicefile, channel="template_voice", loop=not is_custom)
        elif event in ("slow_done", "end"):
            if not is_custom:
                renpy.music.stop(channel="template_voice", fadeout=0.1)
            store.custom_voice = None

#Character
define narrator = Character(None, callback=template_voice, cb_voicefile="audio/voice/katerine/mul_katerine.wav")
define Katerine = Character('Katerine', color="#ffffff", callback=template_voice, cb_voicefile="audio/voice/katerine/mul_katerine.wav")  #MC
define Sonya = Character('Sonya', color="#80b9c8", callback=template_voice, cb_voicefile="audio/voice/sonya/mul_sonya.wav") #lead investigator
define Ivan = Character('Ivan', color="#247d7f", callback=template_voice, cb_voicefile="audio/voice/male/mul_male.wav") # field investigator
define Alexei = Character('Alexei', color="#b2d9c4", callback=template_voice, cb_voicefile="audio/voice/male/mul_male.wav") # technical investigator
define Oscar = Character('Oscar', color="#900000", callback=template_voice, cb_voicefile="audio/voice/male/mul_male.wav") # the burner
define Albert = Character('Albert', color="#900000", callback=template_voice, cb_voicefile="audio/voice/male/mul_male.wav") #the briber
define Franz = Character('Franz', color="#900000", callback=template_voice, cb_voicefile="audio/voice/male/mul_male.wav") #the ghost
define Fox = Character('Little Fox', color="#ec7599", callback=template_voice, cb_voicefile="audio/voice/fox/pinkvoice.wav") #pink
define Agatha = Character('Agatha', color="#efdeef", callback=template_voice, cb_voicefile="audio/voice/mastermind/mul_mastermind.wav") 

#Home BGM
define config.main_menu_music = "audio/bgm/home-battle.wav"

label tutorial_battle:
    stop music fadeout 1.0
    jump tutorial

label scene_1:
    stop music fadeout 1.0
    jump firstscene
    
label scene_2:
    stop music fadeout 1.0
    jump secondscene
    
label scene_3:
    stop music fadeout 1.0
    jump thirdscene

label scene_4:
    stop music fadeout 1.0
    jump fourthscene



label start:
    return
