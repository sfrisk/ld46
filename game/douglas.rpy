label douglas1:
  scene bg manor

  "Week one douglas stuff?"

label douglas2:
  scene bg manor
  show douglas
  protag " Good morning Douglas, how are you this morning?"
  douglas "Morning %(player_name)s."
  hide douglas
  show douglas happy
  douglas "I must say, the progress you have made in just a week is inspiring."
  douglas "Everything is getting organized and pruned. It’s like a new space already. Is there anything I can assist with?"
  protag "Thank you! It’s been very rewarding so far."
  protag ". . ."
  protag "I guess the only thing I can think of is if you have any more keys you might be hanging on to."
  hide douglas happy
  show douglas
  douglas "Keys? I gave you a master to the house, that should open any door you need."
  menu:
    "Tell him about the terrarium":
      protag "Oh no, it’s not for a door per say. There’s an old terrarium build into the back wall and I wanted to open the case. It’s a small antique lock."
    "Tell him about old plumbing line access":
      protag "Oh, it’s not for a door per say. There’s a small door blocking access to some of the old plumbing in there. It’s a small antique looking lock."
  "Douglas pulls out a small black key and hands it to me."
  douglas "Here, this is a skeleton key. It might open that. Can’t hurt."
  "RING RING"
  "Douglas' phone starts ringing"
  hide douglas
  show douglas mad
  douglas "I'm sorry, I must get this. We'll talk later, but for now here is more funds for courtyard"
  hide douglas mad
  show douglas
  douglas "Yes? This is Douglas speaking . . ."
  hide douglas
  "Douglas wanders off, and I don't hear any more of the call."
  protag "I should try using this key."
  "I wander over to the terrarium to see if the key will help. It opens the plumbing acces, but unfortunately won't open the terrarium."
  protag "Well, that’s at least one question solved."
  "Ding!"
  "Huh, someone is texting me."
  "I check my phone and see a text message from Cam."
  cam "Douglas just stopped by and upped your budget for the garden. Swing by for some deals."
  protag "Ooo, more money for plants? Excellent! Maybe I can find something for the terrarium."
  "I'm about to head out, when I see Ted and Molly across the courtyard."
  show ted:
    xalign 0.15
    yalign 1.0
  show molly:
    xalign 0.85
    yalign 1.0
  "I have some time, I should say hello to one of them."
  menu:
    "Molly":
      $ weekTwoMolly = True
      jump molly2
    "Ted":
      $ weekTwoTed = True
      jump ted2

label douglas3:
  scene bg manor
  show douglas
  douglas "Hey protag. What's up with this lily?"
  menu:
    "Renalda's work":
      protag "It was something Renalda was working on"
    "Rare discovery":
      protag "It's some sort of rare variety I've never seen before"
  douglas "Tell me more, tell me more"
  if ghost == True:
    jump douglas3ghost
  jump douglas3noGhost

label douglas3ghost:
  protag "Protag shows him altar and book."
  hide douglas
  show douglas mad
  douglas "Douglas is angry, reveals Renalda is aunt. Family wants to hide her pagan ties to ensure a positive legacy."
  protag "Protag is defiant and supportive of Renalda. Tells Douglas that she gave up a child to save family shame."
  douglas "TELL ME MORE"
  protag "STALLS FOR TIME. NEED MORE INFO"
  jump shop3

label douglas3noGhost:
  protag "Protag shows him hot house and fountains. Tell him he needs a new pump."
  hide douglas
  show douglas happy
  douglas "Douglas is happy, reveals Renalda is aunt. Family wants to assure her legacy."
  protag "Protag is happy to help but flower is not blooming yet."
  douglas "Douglas thinks he might have an answer and says he will be back."
  jump shop3