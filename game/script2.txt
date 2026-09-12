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
define Franz = Character('Franz', color='#efdeef') #the ghost

# The game starts here.

#/ Several days later /
label dialogBB:
    "The team continues investigating the mysterious identity known as “The Ghost.”"
    "The only evidence they have is the encrypted message recovered from The Bribe's phone."
    Alexei "I've been trying to trace this account for days."
    Katerine "And?"
    Alexei "Nothing."
    Ivan "No identity?"
    Alexei "No identity. No location. No digital footprint."
    Sonya "Then we're dealing with someone who knows how to disappear."
    "Suddenly, the computer screen flickers."
    "A new message appears."
    "«“STOP LOOKING.”»"
    Katerine "They found us."
    "Another message appears."
    "«“COME ALONE.”»"
    "A location appears on the screen."

    Katerine "I'll go."
    Ivan "Absolutely not."
    Katerine "If The Ghost wants to talk, this might be our only chance."

    #/ Abandoned Building — Night /
    "The MC enters an abandoned building."
    "The room is completely dark."
    Katerine "I'm here."
    "A voice comes from the darkness."
    Franz "You should have listened to the warning."
    Katerine "You're The Ghost."
    Franz "That name is enough."
    Katerine "You helped The Bribe hide the evidence."
    Franz "I helped someone disappear."
    Katerine "And The Burner?"
    Franz "Another loose end."
    Katerine "Who are you working for?"
    "Silence."
    Franz "You ask too many questions."
    Katerine "And you hide too many answers."
    "The Ghost steps out of the darkness."
    return

label dialogAB:
    "The Ghost disappears into the darkness."
    Ivan "Wait!"
    Katerine "Let them go."
    Ivan "Why?"
    Katerine "Because now we know who we're really looking for."
    "The Technical Investigator looks at the recovered file."
    Alexei "There's one final piece of information."
    Katerine "What?"
    "The screen displays:"
    "PROJECT FLAMMA"
    "DIRECTOR: ██████████"
    "STATUS: ACTIVE"
    Katerine "They're still operating."
    Sonya "Then this case isn't about finding a criminal anymore."
    Katerine "It's about finding the person behind all of them."
    return

    