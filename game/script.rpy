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

init python:
    renpy.music.register_channel(
        "template_voice",
        mixer="voice",
        loop=True
    )

    def template_voice(event, interact=True, voicefile="audio/voice/male/mul_male.wav", **kwargs ):
        if not interact:
            return
        if event == "show":
            renpy.music.play(voicefile, channel="template_voice", loop=True)
        elif event in ("slow_done", "end"):
            renpy.music.stop(channel="template_voice", fadeout=0.1)

define narrator = Character(None, callback=template_voice, cb_voicefile="audio/voice/katerine/mul_katerine.wav")
define Katerine = Character('Katerine', color="#ffffff", callback=template_voice, cb_voicefile="audio/voice/katerine/mul_katerine.wav")  #MC
define Sonya = Character('Sonya', color="#80b9c8", callback=template_voice, cb_voicefile="audio/voice/sonya/mul_sonya.wav") #lead investigator
define Ivan = Character('Ivan', color="#247d7f", callback=template_voice, cb_voicefile="audio/voice/male/mul_male.wav") # field investigator
define Alexei = Character('Alexei', color="#b2d9c4", callback=template_voice, cb_voicefile="audio/voice/male/mul_male.wav") # technical investigator
define Oscar = Character('Oscar', color="#900000", callback=template_voice, cb_voicefile="audio/voice/male/mul_male.wav") # the burner
define Albert = Character('Albert', color="#900000", callback=template_voice, cb_voicefile="audio/voice/male/mul_male.wav") #the briber
define Fox = Character('Little Fox', color="#ec7599", callback=template_voice, cb_voicefile="audio/voice/fox/pinkvoice.wav") #pink

label tutorial_battle:
    jump tutorial

label scene_1:
    jump firstscene
    
label scene_2:
    jump secondscene
    
label scene_3:
    jump thirdscene

label scene_4:
    jump fourthscene



label start:
    return
