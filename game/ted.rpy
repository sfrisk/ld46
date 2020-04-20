label ted1:
  scene bg manor
  show ted
  ted "Good morning, %(player_name)s! It’s a lovely day, isn’t it?"
  protag "Yeah, it’s been a good day for gardening so far."
  ted "You have your work cut out for you here."
  menu:
    "It’s not so bad. It just needs a little care.":
      $ jibberish = True
    "It’s a shame it was let go for so long.":
      $ jiberish = False
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
    "Romantic Answer":
      protag "I hope to be here for a long time."
    "Pragmatic Answer":
      protag "It was just too good an opportunity to pass up professionally."
  "[FINISH CONVO]"
  hide ted
  jump molly1


label ted2:
  scene bg manor
  show ted
  ted "Hey, %(player_name)s!"
  protag "Hi, Ted, I really enoyed your [recent broadcast]"
  ted "Oh you saw it?"
  ted "How goes the garden?"
  menu:
    "Answer with Scientific Terms":
      protag "My Answer. SCIENCEY Answer"
    "Describe Terms in plain english":
      protag "Easy to understand verison"
  ted "You're pretty smart, you know that"
  protag "Who, me? (is very modest)"
  ted "What is your favorte color?"
  menu:
    "Green":
      $ favoriteColor = "green"
    "Blue":
      $ favoriteColor = "blue"
    "Red":
      $ favoriteColor = "red"
    "Purple":
      $ favoriteColor = "purple"
    "Pink":
      $ favoriteColor = "pink"
  ted "I'll make sure to wear a %(favoriteColor)s colored tie on the next broadcast"
  protag "Where you from?"
  ted "Ted is from Oakglen. He left for college in NY. He asks ?"
  protag "An Answer"
  "THERE IS A MOMENT"
  if weekTwoTed == True:
    menu:
      "Shall I flirt?"
      "Yes":
        $ weekTwoFlirt = True
      "No":
        $ weekTwoFlirt = False
  ted "Well, lovely chatting, but I have to go. See you later!"
  if weekTwoTed:
    jump startWeek2AfterTalk
  jump endWeek2AfterTalk
