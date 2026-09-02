# SCENE 
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define Katerine = Character('Katerine', color="#ffffff")  #MC
define Sonya = Character('Sonya', color="#80b9c8") #lead investigator
define Ivan = Character('Ivan', color="#247d7f") # field investigator
define Alexei = Character('Alexei', color="#b2d9c4") # technical investigator
define Oscar = Character('Oscar', color="#900000") # the burner
define Albert = Character('Albert', color="#98c156") #the briber

# The game starts here.

label dialogBB:
    "The investigation team returns to the office with the evidence recovered from the forest."
    "The burned lighter and the company emblem are placed on the table."
    Alexei  "I traced the emblem to a company involved in the forest development project."
    Katerine "So the company is connected to the fire?"
    Alexei "Not directly. But someone inside the company made several suspicious payments before the incident."
    Sonya "Then we follow the money."
    Katerine "And find whoever paid The Burner."

    #later that day -- corporate building
    "The team arrives at the company's headquarters."
    "The building is almost empty."
    Ivan "Something feels wrong."
    Katerine "There's no one here."
    "Suddenly, the lights turn on."
    "A woman is sitting calmly behind a large desk."
    "She places an envelope filled with money on the table."
    Albert "You've come a long way just to ask questions."
    Katerine "Are you the one who paid The Burner?"
    Albert "That's a serious accusation."
    Katerine "We have evidence."
    Albert "Evidence can be bought."
    "She smiles."
    Albert "And so can people."
    return

label dialogAB:
    "The Bribe quickly grabs her phone."
    Ivan "Stop!"
    "She throws the phone onto the floor."
    "The screen shatters."
    Katerine "What was she trying to delete?"
    Alexei "Wait…"
    "The Technical Investigator picks up the damaged phone."
    Alexei "I managed to recover one file."
    Katerine "What is it?"
    "A list of encrypted messages appears on the screen."
    Alexei "These messages were exchanged shortly before the fire."
    Ivan "Who's the recipient?"
    "The Technical Investigator tries to trace the account."
    "ACCESS DENIED."
    Alexei "There's no name."
    Katerine "No name?"
    Alexei "No identity. No phone number. No registered account."
    "The screen suddenly displays a single message."

    "«“The fire is only the beginning.”»"
    Katerine "Who sent this?"
    "The Technical Investigator continues analyzing the message."
    Alexei "There's one more thing."
    "The screen reveals a strange symbol."
    "GHOST // 00:00"
    Ivan "Ghost?"
    Albert "..."
    "The Bribe suddenly stops smiling."
    Katerine "You know who that is."
    Albert "I don't know anything."
    Katerine "You're lying."
    Albert "You should stop digging."
    Katerine "Why?"
    "The Bribe looks directly at the MC."
    Albert "Because the moment you find The Ghost…"
    "She pauses."
    Albert "…The Ghost will find you first."

    return

    