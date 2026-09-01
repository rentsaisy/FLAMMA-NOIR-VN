# SCENE 1
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define Katerine = Character('Katerine', color="#ffffff")
define Sonya = Character('Sonya', color="#80b9c8")
define Ivan = Character('Ivan', color="#247d7f")
define Alexei = Character('Alexei', color="#b2d9c4")
define Oscar = Character('Oscar', color="#900000")

# The game starts here.

label start:
    "The flames spread, consuming his house. The fire grows stronger, devouring everything in its path."
    "This is our newest member."
    Sonya "This is our newest member."
    Katerine "Hello, everyone. I’m the new lawyer."
    Sonya "Alright. Let’s introduce ourselves. I’m the Lead Investigator, responsible for coordinating our investigations."
    Ivan "I’m the Field Investigator. I handle investigations and evidence directly at the crime scene."
    Alexei "I’m the Technical Investigator. I analyze technical evidence and help uncover hidden information."
    "Suddenly, a new case comes in."
    Sonya "Looks like this is your first case."
    Katerine "Forest arson?"
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

    