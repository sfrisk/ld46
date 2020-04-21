label ted1:

  scene bg manor
  "As Douglas walked off, I found myself in the courtyard, wondering what to do."
  show ted
  "Lucky for me, I didn't have to make a decision, since Ted immediately came over to talk to me."
  ted "Good morning, %(player_name)s! It’s a lovely day, isn’t it?"
  protag "Yeah, it’s been a good day for gardening so far."
  ted "You have your work cut out for you here."
  menu:
    "Hopeful":
      "It’s not so bad. It just needs a little care."
    "Sad":
      "It’s a shame it was let go for so long."
  ted "Ah, yes, well there was a protracted legal battle after Miss Grimalli’s death. Problems with the will have left it tied up in probate court for years. "
  ted "Then the taxes lapsed and the next thing you know, the estate had okayed the sale of the property based on an older copy of the will that left everything to a blind trust."
  ted "That is until Douglas Beckham showed up in town. Next thing we knew, he had permits for restoration and he was pitching for it to be on the National Register of Historic Places. "
  protag "He’s been been very upfront with me about his restoration efforts and his problems with the courtyard. I’m hoping that I can locate some information about the house so I can try to clear out everything properly. "
  ted "Have you given my suggestion any thoughts? I know that even in the midst of an antique marvel, you can have an appreciation for modern tastes. "
  menu:
    "Maybe":
      protag "It’s still early in the debris clearing phase so I really haven’t gotten a chance to draft a new plan yet."
    "Not Really": 
      protag "I’m hoping for something that is worthy of Renalda’s legacy."
  ted "In other news, how are you adjusting to your new home? Can I be of any assistance?"
  menu:
    "Love it":
      protag "It’s a beautiful little town and the people are so friendly so far."
    "It's Okay":
      protag "Thank you, I’m settling in alright."
    "Deflect":
      protag "How do you like living at Elmhearst?"
  ted "The Manor is gorgeous and the apartments are so polished. Really, I couldn’t wait for them to finish the courtyard, it was just the place to be. How do you see yourself here at the Elmhearst?"
  menu:
    "Romantic":
      $ romanceTed = romanceTed + 1
      protag "I hope to be here for a long time."
      hide ted
      show ted flirt
      ted "I would like that"
      hide ted flirt
      show ted
    "Pragmatic":
      protag "It was just too good an opportunity to pass up professionally."
      ted "Of course."
  ted "Well, I really should get to work. It was nice chatting!"
  hide ted
  jump molly1


label ted2:
  if night == True:
    scene bg manor night
  else:
    scene bg manor
  show ted
  ted "Hi, %(player_name)s, how are you this fine morning?"
  protag "Hi Ted, I’m great! I saw you on TV last night, you sounded great."
  hide ted
  show ted happy
  ted "Thank you!"
  hide ted happy
  show ted
  ted "What are you planting here?"
  menu:
    "Answer with Scientific Terms":
      protag "I’m putting in some lilium regale bulbs to propagate near the fountain."
    "Describe Terms in Plain English":
      protag " I’m transplanting some lillies from outside to these beds next to the fountain."
  hide ted
  show ted flirt
  ted "You’re so smart. Your passion for the plants is evident when you speak."
  protag "Thank you Ted, I just love what I do."
  hide ted flirt
  show ted happy
  ted "What is your favorte color?"
  menu:
    "Green":
      $ favoriteColor = "green"
      $ romanceTed = romanceTed + 1
      ted "I'll make sure to wear a %(favoriteColor)s colored tie on the next broadcast"
    "Blue":
      $ favoriteColor = "blue"
      $ romanceTed = romanceTed + 1
      ted "I'll make sure to wear a %(favoriteColor)s colored tie on the next broadcast"
    "Red":
      $ favoriteColor = "red"
      $ romanceTed = romanceTed + 1
      ted "I'll make sure to wear a %(favoriteColor)s colored tie on the next broadcast"
    "Purple":
      $ favoriteColor = "purple"
      $ romanceTed = romanceTed + 1
      ted "I'll make sure to wear a %(favoriteColor)s colored tie on the next broadcast"
    "Pink":
      $ favoriteColor = "pink"
      $ romanceTed = romanceTed + 1
      ted "I'll make sure to wear a %(favoriteColor)s colored tie on the next broadcast"
    "None":
      $ romanceTed = romanceTed - 1
      hide ted happy
      show ted sad
      $ favoriteColor = False
      ted "Oh, well then free for all, I guess."

  protag "Where you from, Ted?"
  hide ted sad
  show ted
  ted "Here in Oakglen. I left to go to college in Pennsylvania but I ended up back here. Something just waiting to be discovered keeps me here. Why did you come here?"
  protag "I was really interested in the work. The blend of a historic house and a garden that needs my help? It was too much to pass up."
  
  if favoriteColor == False:
    hide ted
    show ted happy
    ted "Well it was nice seeing you, I should head out though!"
  else:
    hide ted
    show ted flirt
    ted "I love your passion in what you do."
    "We stand there for a few moments in silence. Oddly enough, it wans't an unconfortable silence. I find myself admiring Ted's fine eyes."
    ted "Well, as much as I would love to stay here and chat, I really should be going to work."
    protag "Yeah . . . me too."
    hide ted flirt
    show ted happy
    ted "See you later,  %(player_name)s."
  if weekTwoTed:
    jump startWeek2AfterTalk
  jump endWeek2AfterTalk
