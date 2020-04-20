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
  "I arrive at the Garden Society at the time Lucinda and I agree about."
  prez "Thank you for stopping by. I’m glad you called about what you found in the courtyard."
  if ghost == True:
    jump society2ghost
  else:
    jump society2terrarium

label society2terrarium:
  protag "I found a strange terrarium built into the back wall of the courtyard. It looks like there’s something growing in it but I can’t tell right now what it is."
  prez  "I’m not surprised. Renalda was constantly cross breeding things to come up with new varieties."
  hide prez
  show prez happy
  prez "She would cross breed herbs to make them more potent in healing applications. Her aloe is amazing on everyone from rashes to burns."
  hide prez happy
  show prez
  prez "Here, she used to make her own contraptions. I think this might open that case for you."
  "Lucy hands me a an old looking key that looks like it might fit the terrarium."
  protag "Thank you, Lucy!"
  $ terrariumKey = True
  jump society2end

label society2ghost:
  prez "But you weren’t making any sense. Tell me again, what got you so emotional?"
  protag "I saw Renalda’s ghost in the courtyard!"
  protag "She lead me to the valve where the fountain lines ran and then there was a glass case set in the wall."
  prez "Holy smokes! You SAW HER?"
  prez "This...I...I can’t believe it. The fountains huh? I think I can help."
  prez "I have some letter collections of hers that she donated to us before her death. She modeled that fountain after one she saw in the 20’s in France. The letters and translations are in the file."
  "Lucy gives me a statsh of letters. Reading through it, I discover that Renalda was having an affair with a local pastor. She refused to give up her faith in the Goddess and so the relationship ended and she became a recluse."
  "My purusal of the letters is interrupted by a question from Lucy." 
  $ personalLetters = True
  jump society2end

label society2end:
  hide prez
  show prez annoyed
  prez "Tell me, what does Douglas know about the courtyard?"
  menu:
    "Lie":
      protag "I haven’t seen him lately. Why are you so against him?"
    "Truth":
      protag "He’s my boss. We spoke about the courtyard this morning. Why are you so against him?"
  prez "He fought us in court over Renalda’s estate for 3 years. He nearly bankrupted us with the court battle. He’s after something."
  protag "Lucinda, was Renalda a witch?"
  hide prez annoyed
  show prez
  "Lucy seems surprised by the question."
  prez " . . . yes."
  "Things were a bit awkward after that, and I had work to do. After a few weird moments, I waved goodbye to Lucy, promising to talk to her later."
  jump travel

label society3:
  $ societyVisits = 3
  scene bg parlor
  show prez
  prez "Hello, %(player_name)s!"
  protag "Hey, Lucy!"
  protag "Protag reveals the letters between Lucy and Renalda in the stack."
  prez "Lucy confesses that Renalda was the Elder of their coven.  Lucy is HP, and pseudo daughter to Renalda. Renalda was supposed to leave Elmhearst to the GS to be their home but will disappeared."
  protag "Protag apologizes. Reveals that Douglas is Renalda’s nephew."
  prez "Lucy already knew. Renalda had been close to his mother until she became a witch then, it tore the family apart. That’s when Renalda changed the will but Lucy can’t prove it."
  menu:
    "Support Lucy":
      hide prez
      show prez happy
      prez "Lucy is happy, provides last packet of letters"
      protag "Reveal books/notes"
      hide prez happy
    "Defend Douglas":
      hide prez
      show prez mad
      prez "Lucy is angry, but provides last packet of letters"
      protag "Reveal books/notes"
      hide prez mad
  show prez
  prez "PLEASE Give them to me"
  menu:
    "Agree":
      hide prez
      show prez happy
      prez "I'm glad you're willing to help"
      protag "Let's go!"
      hide prez happy
    "Ask Donald":
      show prez annoyed
      prez "If you feel that is best"
      protag "Let's go!"
      hide prez annoyed
  jump travel