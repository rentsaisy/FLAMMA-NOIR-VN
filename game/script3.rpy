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
define Agatha = Character('Agatha', color='#df0f64') #the mastermind 
define Judge = Character("Judge", color="#efcdd6") #judge

# The game starts here.

#/ The Final Investigation /
label dialogBB:
    "The investigation team finally traces the source behind The Burner, The Bribe, and The Ghost."
    "The trail leads to an elegant private estate overlooking the forest."
    Ivan "This is the place."
    Katerine "Who owns it?"
    Alexei "A private investor."
    Sonya "Let's go."

    #/ Inside the Estate /
    "The room is quiet."
    "A woman sits calmly beside a large window overlooking the forest."
    "She wears an elegant white dress."
    "Around her neck hangs a necklace decorated with white fox fur."
    Agatha "I was wondering when you would arrive."
    Katerine "You're the one behind the forest fire."
    Agatha "Behind it?"
    "She smiles."
    Agatha "I simply gave people a reason to do what they were already willing to do."
    Katerine "You destroyed an entire forest for money."
    Agatha "Destroyed?"
    "She touches the white fox-fur necklace."
    Agatha "No."
    Agatha "I transformed something worthless into something profitable."
    Katerine "And the animals?"
    Agatha "Collateral."
    Katerine "You call that collateral?"
    Agatha "I call it business."
    return

label dialogAB:
    "The room becomes quiet."
    "The Mastermind removes the white fox-fur necklace from around her neck."
    "She stares at it for a moment."
    Agatha "So…"
    Agatha "This is where it ends."
    Katerine "Yes"
    Agatha "After everything you've seen…"
    Agatha "After everything you've uncovered…"
    "She looks directly at the MC."
    Agatha "Tell me something."
    Agatha "Have you ever felt regret?"
    "The MC remains silent."
    Katerine "I have never regretted what I have done."
    Katerine "Because everything I have done, I did with a clear conscience."
    Katerine "I stood for truth."
    Katerine "For justice."
    Katerine "For honesty."
    Katerine "And for humanity."
    Katerine "So no…"
    Katerine "I have never regretted my choices."
    Katerine "If the day comes when I must face death, I want to leave this world without regrets."
    Katerine "That is the art of dying well."
    Katerine "To live by what you believe in…"
    Katerine "And to die knowing you never betrayed it."
    "The Mastermind says nothing."
    Sonya "Take her."
    "The Field Investigator approaches and places handcuffs on The Mastermind."

    # / THE JUDGMENT /

    # / Courtroom /
    "The Mastermind stands before the Judge."
    "The investigation team presents all recovered evidence."
    "Evidence 01 — Burned Lighter"
    "Evidence 02 — Financial Transactions"
    "Evidence 03 — Encrypted Messages"
    "Evidence 04 — Communication Logs"
    "Evidence 05 — White Fox Fur"
    Judge "The court has reviewed the evidence presented."
    Judge "The defendant deliberately orchestrated the destruction of forest land for financial gain."
    Judge "She recruited and manipulated others to carry out her plan, concealed evidence, and attempted to profit from the destruction."
    "The courtroom falls silent."
    Judge "Therefore, this court finds the defendant…"

    "GUILTY."
    "BANG!"
    "The Judge strikes the gavel."

    Judge "The defendant is sentenced to imprisonment and ordered to pay restitution for the damages caused by the incident."
    Judge "Any assets obtained through the illegal operation shall be seized according to the law."
    Judge "This case is hereby closed."

    #/ Outside the courtroom /
    "The MC looks toward the forest in the distance."
    "The burned land is still visible."
    "But small green leaves are beginning to grow."
    Ivan "It's going to take a long time."
    Katerine "Yeah."
    Ivan "Do you think the forest will recover?"
    Katerine "I hope so."
    "The MC looks at the evidence bag containing the white fox-fur necklace."
    Katerine "Some things can't be brought back."
    Katerine "But justice can make sure they're never forgotten."
    "CASE CLOSED"
    "THE MASTERMIND — DEFEATED"

    return

    