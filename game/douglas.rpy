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
  douglas "Hey, what’s going on with that weird flower in the back there?"
  menu:
    "Renalda's work":
      protag "It’s something I think Renalda was breeding a special flower when she died."
    "Rare discovery":
      protag " It’s a rare flower I’ve never seen before."
  douglas "What’s that glass case it’s in?"
  if terrariumKey == True:
    jump douglas3ghost
  jump douglas3noGhost

label douglas3ghost:
  protag "I throw the lever and show him the alter"
  hide douglas
  show douglas mad
  douglas "What in the name of God is that?! Is that an altar?"
  douglas "*shakes head*"
  douglas "Renalda was my aunt. We’re trying to make sure she is remembered for the right reasons. She played with this witchcraft nonsense until she died."
  protag "It’s not nonsense. She believed. It’s not for us to judge her for that."
  hide douglas mad
  show douglas
  douglas "I suppose. Please excuse me."
  "Well that was awkward. Guess I'll go visit Cam for some supplies."
  jump shop3

label douglas3noGhost:
  protag "I think it’s a hot house and fountains, based on some contemporary installations. It needs a new pump though. I think Cam can do the work but I wanted to clear it with you."
  hide douglas
  show douglas happy
  douglas "Of course! Renalda was my aunt and we just want to ensure her legacy is preserved as a lady of society."
  protag " That’s great! I just hope I can get the flower to bloom!"
  douglas "I might have an answer. I’ll be right back."
  hide douglas happy
  ". . ."
  "I wait a few moments, but Douglas doesn't return.  I decide he can call me if he needs me, and head to Cam for some supplies."
  jump shop3