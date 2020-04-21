# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define protag = Character("player_name", color="#6ca7c3", dynamic=True)
define douglas = Character("Douglas")
define ted = Character("Ted")
define molly = Character("Molly")
define neighbor1 = Character("Neighbor")
define neighbor2 = Character("Neighbor 2")
define librarian = Character("Libby", color="#8d7db3")
define cam = Character("Cam", color="#7b9f2d")
define prez = Character("Lucinda", color="#00b6b9")

# The game starts here.

label start:
    scene bg manor
    $ friendshipTed = 0
    $ friendshipMolly = 0
    $ romanceTed = 0
    $ romanceMolly = 0
    $ libraryVisits = 0
    $ societyVisits = 0
    $ shopVisits = 0
    $ haveGardenCard = False
    $ isHorticulturist = False
    $ growLight = False
    $ terrariumTools = False
    $ terrariumPlants = False
    $ terrariumKey = False
    $ personalLetters = False
    $ photoAlbum = False
    $ fountainBook = False
    $ favoriteColor = ""
    $ ghost = False
    $ player_name = renpy.input("What is your name", default=getRandomName())
    $ player_name = player_name.strip();

    if player_name == "":
        $ player_name = getRandomName()

    protag "It's %(player_name)s."

    menu:
        "What are your preferred pronouns?"
        "She/Her":
            $ subject_pronoun = 'she'
            $ object_pronoun = 'her'
            $ possessive_adjective = 'her'
            $ possessive_pronoun = 'hers'
            $ reflexive_pronoun = 'herself'
        "He/Him":
            $ subject_pronoun = 'he'
            $ object_pronoun = 'him'
            $ possessive_adjective = 'him'
            $ possessive_pronoun = 'his'
            $ reflexive_pronoun = 'himself'
        "They/Them":
            $ subject_pronoun = 'they'
            $ object_pronoun = 'them'
            $ possessive_adjective = 'their'
            $ possessive_pronoun = 'theirs'
            $ reflexive_pronoun = 'themself'
    protag "My prefered pronouns are '%(subject_pronoun)s/%(object_pronoun)s'"

    scene bg manor

    "It was my first day of my new job. I had been surprised when Douglas had reached out offering me the job at Elmhearst, but here I was."
    "It was a dream job, and I couldn't wait to start."
    "I pulled my car up to the large manor, and couldn't believe my luck that I would be able to work on such a fabulous historical building."
    show douglas
    "As I got out of my car, Douglas came out to meet me."
    hide douglas
    show douglas happy
    douglas "Welcome to The Elmhearst. I've been looking forward to seeing you, %(player_name)s."
    "I shook Douglas's hand."
    protag "It is nice to meet you too. The Elmhearst is a lovely building."
    douglas "It is indeed. Right this way please."
    "As Douglas led the way towards the manor, he began explaining the history of it."
    hide douglas happy
    show douglas
    douglas "This manor used to be the home of a reclusive heiress, Renalda Grimalli. "
    douglas "Renalda had few visitors but letters belonging to her showed that she used to be known for the beauty of the courtyard. It was said to be a place where she would hold strange rituals. "
    hide douglas
    show douglas mad
    douglas "Rumors about the things she used to do here have tempted ghost hunters and occult nuts to comb over the grounds for years."
    douglas "No one’s ever found anything but that never stopped them. At least until I got the fences mended."
    hide douglas mad
    show douglas
    douglas "I’ve spent a small fortune to turn this old estate into luxurious apartments."
    douglas "My previous building manager did what they could with the grounds as you can tell but the inner garden in the courtyard was just too much for them. Everything they tried just withered. "
    hide douglas
    show douglas mad
    douglas "I can’t have the entire heart of the manor look like a scraggly dying mess. The residents have tried, I’ve tried. I’m at my wit’s end. Just...keep it alive."
    hide douglas mad
    show douglas
    "We entered the couryard of Elmhearst. The courtyard was as Douglas said: a mess. Dead plants everywhere."
    "Still, something drew my to the courtyard. I was sure I could help revive it."

    "Sitting on some benches to the side of the courtyard, sat a few of what I assumed were people who were renting apartments in the estate."
    
    show ted:
      xalign 0.15
      yalign 1.0
    "One was a man wearing a well fitted suit.  I think I've seen him on TV before"
    hide ted

    show molly:
      xalign 0.85
      yalign 1.0
    "A woman sat in the corner, a book in her hand. She looked up as Douglas and I came into the room."
    hide molly

    douglas "Ah good, you're all here."

    douglas "I wanted to introduce you to %(player_name)s, our new building manager. %(player_name)s comes to us from a rather famous estate museum and gardens. I hope you will all make %(object_pronoun)s feel welcome at Elmhearst."
    douglas "Why don’t you tell us what you’d like to see with the courtyard?"

    protag "Thank you for the welcome! As for the garden, I haven’t had a good chance to really see what’s in there yet, but what do you want to see in there?"
    hide douglas
    show ted
    ted "Hello. I'm Ted, and I’d like something to be a real centerpiece. Something with a dramatic effect when you walk in."

    menu:
        "That sounds awesome!":
            hide ted
            show ted happy
            ted "I knew you were a person of good taste."
            hide ted happy
            $ romanceTed = romanceTed + 2
        "That sounds interesting!":
            ted "I'm glad you think so."
            hide ted
            $ romanceTed = romanceTed + 1
        "That sounds out of place for this space.":
            hide ted
            show ted mad
            ted "Well some people don't have any class."
            hide ted mad
            $ romanceTed = romanceTed - 1
    

    show molly
    protag "How about you? What do you want to see?"

    show molly happy
    molly "Hi, I'm Molly and it's great to meet you"
    hide molly happy
    show molly
    molly "I’d like to see it as a functional space. Where you can sit, and read or have a nice cup of tea in the morning."
    menu:
        "That sounds awesome!":
            hide molly
            show molly happy
            molly "Glad you like my idea!"
            $ romanceMolly = romanceMolly + 2
        "That sounds interesting!":
            $ romanceMolly = romanceMolly + 1
            molly "I thought it sounded cool."
        "That sounds out of place for this space.":
            hide molly
            show molly mad
            $ friendshipMolly = friendshipMolly - 2
            $ romanceMolly = romanceMolly - 2
            molly "Well you didn't need to be so rude."

    hide molly
   
    show douglas
    douglas "I’m sure you’ll have plenty of ideas once you really get your hands in there."
    douglas "I have some phone calls I need to make, but be sure to let me know if you need anything."

    jump startWeek1