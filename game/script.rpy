# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define protag = Character("player_name", color="#6ca7c3", dynamic=True)
define romanceA = Character("Romance A")
define romanceB = Character("Romance B")
$ friendshipA = 0
$ friendshipB = 0
$ romanceA = 0
$ romanceB = 0
# The game starts here.

label start:
    scene bg room
    show protag happy

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

    menu:
        "Who do you want to work with on the community garden planning committee?"
        "Romance Option A":
            protag "I choose Romance Option A!"
            jump romance_a
        "Romance Option B":
            protag "I choose Romance Option A!"
            jump romance_b


label romance_a:
    "And so Romance A and I began working together on the garden project"
    hide protag happy
    show romanceA happy
    $ capitalize_prounoun = subject_pronoun.capitalize()
    romanceA "%(player_name)s? %(capitalize_prounoun)s seems pretty cool."
    jump ending

label romance_b:
    "And so Romance A and I began working together on the garden project"
    hide protag happy
    show romanceA happy
    $ capitalize_prounoun = subject_pronoun.capitalize()
    romanceB "%(player_name)s? %(capitalize_prounoun)s seems pretty cool."
    jump ending



label ending:
    "And that's the end of the story"
    return
