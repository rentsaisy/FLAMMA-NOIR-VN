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

# #     return

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
define Fox = Character('Little Fox', color="#ec7599", callback=template_voice, cb_voicefile="audio/voice/fox/pinkvoice.wav") #pink

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

    