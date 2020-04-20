
label shop1:
  $ shopVisits = 1
  scene bg shop
  "So I decided to check out the store, Blooms and Boughs, the local garden shop"
  show cam happy
  cam "Hello, welcome to Blooms and Boughs, how can I help you?"
  menu:
    "Gardening Tools":
      protag  "I’m looking for some tools to help me pull out some old flower beds and containers."
    "Information":
      protag "I’m looking for some information about local flora to help replant a historic garden."
  hide cam happy
  show cam
  cam "I think I have just the thing. You must be the new building manager over at the Elmhearst."
  hide cam
  show cam happy
  cam "I’m Cam Webber, the owner here. Your boss stirred up the town when he bought that place. It looks like the grounds are in pretty good shape though."
  protag "How did you know who I was?"
  hide cam happy
  show cam sad
  cam "Sorry, gossip travels fast when one of the people in your building is a news anchor."
  hide cam sad
  show cam happy
  cam "It’s not bad, though. We’ve been waiting for you to get here. Just excitement really. Well, here are the tools and the books about our local climate."
  hide cam happy
  show cam
  cam "Let me know if you need anymore help."
  menu:
    "I think I see what I need":
      hide cam
      show cam happy
      cam "Great, just pick out what you want and I’ll have everything sent over to the manor."
    "Hmm, do you have any books about the historic gardens from around here?":
      hide cam
      show cam sad
      cam "Sorry, I don’t. You could check the library. Or you could go talk to the Garden Society. I think the lady who built that house founded it or something. Here’s the card for their President."
      $ haveGardenCard = True
  show cam happy
  cam "Thank you for stopping by! See you again soon!"
  hide cam happy
  "I didn’t expect to cause a stir coming here. It’s strange to be known before you introduce yourself but it looks like everyone in town keeps an eye on each other."
  "I guess I better figure out who I want to see about the gardens this week. There’s so much work to be done."
  jump travel

label shop2:
  $ shopVisits = 2
  scene bg shop
  show cam
  "AVO BEAR HIMSELF, CAM, BACK FOR WEEK 2"
  if isHorticulturist == True:
    "Cam horticulturist bkgd"
    "Cam sells special grow light"
  else:
    cam "HEY FRIEND. HOW CAN I HELPS?"
    menu:
      "Terrarium Tools":
        $ terrariumTools = True
      "Terrarium Plants":
        $ terrariumPlants = True
    cam "I KNOW LOTS ABOUT TERRARIUMS!"
    if terrariumTools == True:
      "I buy some tools"
    else:
      "I buy some plants"
  protag "I need to get back to the garden."
  "Cam wonders what exactly Protag found."
  hide cam
  jump travel

label shop3:
  $ shopVisits = 2
  scene bg shop
  show cam
  protag "Hey cam! What do you have for modern pump systems?"
  cam "Cam says can have one ordered to fit. Might need to come see the setup so they get the right connections."
  protag "That works, you're welcome to come over to Elmhearst whenever."
  hide cam
  show cam happy
  cam "That's great! I've always dreamed of seeing Elmhearst up close."
  protag "You have? Why didn't you apply for the building super job?"
  hide cam happy
  show cam sad
  cam "I did, but I wasn't chosen."
  hide cam sad
  show cam happy
  cam "But I'm glad you got the job. It's been great talking to you."
  cam "Can I get you anything else?"
  if ghost == True:
     menu:
      "Something for the Alter":
        protag "I was looking for some herbs to compliment the alter in the courtyard."
      "Tools and Pots":
        protag "Tools to help transplant plants and some pots please!"
  else:
    menu:
      "Something for the Fountain":
        protag "I was looking for some flowers to compliment the fountain in the courtyard."
      "Tools and Pots":
        protag "Tools to help transplant plants and some pots please!"
  
  hide cam happy
  show cam
  cam "Can do! Here ya go!"
  protag "Thanks, Cam, have a nice day!"
  hide cam
  show cam happy
  cam "Thanks you too!"
  hide cam happy
  jump travel