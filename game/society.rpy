label society1:
  $ societyVisits = 1
  scene bg parlor
  show prez
  protag "Hi, I'm %(player_name)s, we spoke on the phone? Thank you for taking the time to meet with me."
  prez "Hello, I’m Lucinda Payne, President of the Oakglen Garden Society."
  hide prez
  show prez annoyed
  prez "I understand you’re the new building manager that snake hired to coax out the lost treasures of Renalda Grimalli? "
  protag "Excuse me?"
  hide prez annoyed
  show prez mad
  prez "I take it that you took the job without doing your homework. Let me tell you a little secret, your boss is looking for something at Elmhearst and he’s running out of time. "
  protag "Lost treasures? Time? I don’t understand. I’m just trying to restore the courtyard."
  hide prez mad
  show prez
  prez "Of course you are dear, that’s what he told you after all. If that’s what you want from this, I suppose I can offer what assistance I can, provided you tell me what he’s looking for over there. "
  protag "How are you so sure he is?"
  hide prez
  show prez mad
  prez "Douglas Beckham is a man who always gets what he wants. No matter how he has to do it. "
  hide prez mad
  show prez
  prez "In your world, he is just a real estate guru who helps save historic homes. But in mine, he’s a man who enjoys power."
  hide prez
  show prez annoyed
  prez "Just be certain you’ve got yours in hand or he will take it from you."
  hide prez annoyed
  show prez
  prez "But I disgress, you wanted help with the gardens."
  prez "Here. Renalda kept meticulous notes when the house was being built. You can have her construction notes and letters to the builders. I hope they serve you well."
  protag "Thank you. Cam at Blooms and Boughs said that Miss Grimalli founded the Garden Society in Oakglen? "
  hide prez
  show prez happy
  prez "It’s true. She had the great ability to bring people close to her and make them feel special."
  hide prez happy
  show prez annoyed
  prez "She was our elder and we mourned her passing deeply. We had hoped that she would leave Elmhearst to us so that we would have a permanent home but we were forced to turn to other avenues."
  hide prez annoyed
  show prez mad
  prez "We held a gala in her name and raised enough to build this municipal conservatory, but there has been such push back from the nosy town historian, Libby."
  prez "She thinks we are trampling on the community gardens around town but this conservatory serves a different purpose, much like a vegetable plot could never be mistaken for a botanical garden"
  protag "I see. Well. Thank you. This was very informational."
  hide prez

  "Wow, there’s something seriously twisted going on in this town. And how did Lucinda seem to know so much about my boss, Douglas? Something’s not right."
  
  jump travel

label society2:
  $ societyVisits = 2
  scene bg parlor
  show prez
  "WEEK TWO OF VISITING LUCINDA"
  prez "Lucinda apologies for previous week after protag call about courtyard find."
  if ghost == False:
    jump society2terrarium
  else:
    menu:
      "Tell Lucinda about Terrarium":
        jump society2terrarium
      "Tell Lucinda about Renalda’s ghost.":
        jump society2ghost

label society2terrarium:
  protag "I found some plantssss. a Terrarium!"
  prez "Lucinda is shocked. Renalda invented them."
  "Protag gets the terrarium key."
  $ terrariumKey = True
  jump society2end

label society2ghost:
  protag "GHOSTS. I SEE DEAD PEOPLE"
  prez "Lucinda is shocked but thinks she can help. Lucinda produces letters Renalda wrote to the estate owners she modeled her fountains after. "
  $ personalLetters = True
  jump society2end

label society2end:
  prez "Lucinda wants to know what Douglas knows about the courtyard"
  menu:
    "Have not seen":
      prez "ah, i would have expected him to be around"
    "Truth":
      protag "I speak truth!"
    "Lie":
      protag "I speak LIES!"
  prez "Lucinda asks if the GS can be of any more assistance."
  protag "Protag asks if Renalda or the GS ever get B&B plants."
  prez "Lucinda says no. They grow their own from seeds."
  jump travel

label society3:
  $ societyVisits = 3
  scene bg parlor
  show prez
  "WEEK THREE OF VISITING LUCINDA"
  hide prez
  jump travel