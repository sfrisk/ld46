# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define protag = Character("player_name", color="#6ca7c3", dynamic=True)
define boss = Character("Boss")
define newsAnchor = Character("News Anchor")
define bookstoreOwner = Character("Bookstore Owner")
define neighbor1 = Character("Neighbor")
define neighbor2 = Character("Neighbor 2")
# The game starts here.

label start:

    $ friendshipA = 0
    $ friendshipB = 0
    $ romanceA = 0
    $ romanceB = 0
    $ visitedShop = False
    $ visitedLibrary = False

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

    scene bg exteriorElmherst

    show boss
    show protag
    boss "Welcome to The Elmhearst." 
    boss "This manor used to be the home of a reclusive heiress, Renalda Grimalli. "
    boss "Renalda had few visitors but letters belonging to her showed that she used to be known for the beauty of the courtyard. It was said to be a place where she would hold strange rituals. "
    boss "Rumors about the things she used to do here have tempted ghost hunters and occult nuts to comb over the grounds for years."
    boss "No one’s ever found anything but that never stopped them. At least until I got the fences mended."

    scene bg interiorElmherst
    show boss
    show protag

    boss "I’ve spent a small fortune to turn this old estate into luxurious apartments."
    boss "My previous building manager did what they could with the grounds as you can tell but the inner garden in the courtyard was just too much for them. Everything they tried just withered. "
    boss "I can’t have the entire heart of the manor look like a scraggly dying mess. The residents have tried, I’ve tried. I’m at my wit’s end. Just...keep it alive."
    
    scene bg commonRoom
    "We entered the couryard of Elmhearst where a handful of building residences were already waiting for the meeing to start"
    
    show newsAnchor
    "One was a man wearing a well fitted suit.  I think I've seen hi on TV before"
    hide newsAnchor

    show b
    "A woman sat in the corner, a book in her hand. She looked up as my boss and I came into the room."
    hide b

    show boss
    boss "Lastly, I wanted to introduce you to %(player_name)s, our new building manager. %(player_name)s comes to us from a rather famous estate museum and gardens. I hope you will all make %(object_pronoun)s feel welcome at Elmhearst."
    hide boss

    neighbor1 "Hey"
    newsAnchor "Hey there"
    neighbor2 "Hi"
    show b
    bookstoreOwner "Greetings!"
    hide b

    boss "Why don’t you tell us what you’d like to see with the courtyard?"
    hide boss

    show protag
    protag "Thank you for the welcome! As for the garden, I haven’t had a good chance to really see what’s in there yet, but what do you want to see in there?"
    hide protag

    show newsAnchor
    newsAnchor "I’d like something to be a real centerpiece. Something with a dramatic effect when you walk in."

    menu:
        "That sounds awesome!":
            $ friendshipA = friendshipA + 1
            $ romanceA = romanceA + 2
        "That sounds interesting!":
            $ friendshipA = friendshipA + 1
        "That sounds out of place for this space.":
            $ friendshipA = friendshipA - 2
            $ romanceA = romanceA - 2
    hide newsAnchor

    show protag
    protag "How about you? What do you want to see?"
    hide protag

    show b
    bookstoreOwner "Well, I’d like to see it as a functional space. Where you can sit, and read or have a nice cup of tea in the morning."
    menu:
        "That sounds awesome!":
            hide b
            show b happy
            bookstoreOwner "Glad you like my idea!"
            $ friendshipB = friendshipB + 1
            $ romanceB = romanceB + 2
        "That sounds interesting!":
            $ friendshipB = friendshipB + 1
            bookstoreOwner "I thought it sounded cool."
        "That sounds out of place for this space.":
            hide b
            show b sad
            $ friendshipB = friendshipB - 2
            $ romanceB = romanceB - 2
            bookstoreOwner "Well you didn't need to be so rude"

    hide b
   
    show Boss
    boss "I’m sure you’ll have plenty of ideas once you really get your hands in there."


    menu:
        "Who do you want to work with on the community garden planning committee?"
        "Romance Option A":
            protag "I choose News Anchor!"
            jump romance_a
        "Romance Option B":
            protag "I choose Bookstore Owner!"
            jump romance_b

label romance_a:
    "And so Romance A and I began working together on the garden project"
    hide protag happy
    show newsAnchor happy
    $ capitalize_prounoun = subject_pronoun.capitalize()
    newsAnchor "%(player_name)s? %(capitalize_prounoun)s seems pretty cool."
    jump startWeek1

label romance_b:
    "And so Romance A and I began working together on the garden project"
    hide protag happy
    show b happy
    $ capitalize_prounoun = subject_pronoun.capitalize()
    bookstoreOwner "%(player_name)s? %(capitalize_prounoun)s seems pretty cool."
    jump startWeek1



label ending:
    "And that's the end of the story"
    return
