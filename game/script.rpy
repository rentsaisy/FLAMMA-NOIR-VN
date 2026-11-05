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
 
label tutorial_battle:
    jump tutorial

label scene_1:
    jump firstscene
    
label scene_2:
    jump secondscene
    
label scene_3:
    "The flames spread, consuming his house. The fire grows stronger, devouring everything in its path."
    # "This is our newest member."
    Sonya "This is our newest member."
    Katerine "Hello, everyone. I’m the new lawyer."
    Sonya "Alright. Let’s introduce ourselves. I’m the Lead Investigator, responsible for coordinating our investigations."
    Ivan "I’m the Field Investigator. I handle investigations and evidence directly at the crime scene."
    Alexei "I’m the Technical Investigator. I analyze technical evidence and help uncover hidden information."
    "Suddenly, a new case comes in."
    Sonya "Looks like this is your first case."
    Katerine "Forest arson?"
    return

label scene_4:
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

    