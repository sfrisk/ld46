label molly1:
  scene bg courtyard
  show molly
  "I see molly"
  protag "Ask Molly a question"
  molly "here is my answer"
  molly "question"
  menu:
    "Firty Answer":
      $ romanceMolly = romanceMolly + 1
      hide molly
      show molly flirt
      "Phrasing!"
      hide molly flirt
      show molly
    "Garden Answer":
      $ friendshipMolly = friendshipMolly + 1
      molly "That's cool"
  molly "Molly Dreams Writer"
  molly "what are your dreams?"
  menu:
    "Horticulturist":
      $ isHorticulturist = True
    "Apothacary/Herbalist":
      $ isHorticulturist = False
  hide molly
  show molly happy
  molly "Molly Answer Happy"
  protag "Protag question Elmhearst"
  hide molly happy
  show molly
  molly "Molly Renalda history fact"
  "I wonder if someone in town might know more"
  hide molly
  show molly sad
  molly "Molly concerned at look"
  protag "It's nothing. It was lovely talking"
  hide molly sad
  show molly happy
  molly "Great talking to you!"
  hide molly
  "well I should probably get some garden stuff"
  jump shop1

label molly2:
  scene bg courtyard
  show molly
  protag "HEY Molly, my gurl in yellow!"
  molly "This is weird placeholder dialog. How are you adjusting to the new town?"
  menu:
    "Great":
      protag "I'm super liking it. Everything is so nice"
      molly "I'm glad to hear that!"
    "Missing Friends":
      protag "It is nice, but I'm missing my friends from back home."
      molly "I can understand that"
  molly "Molly talks about being new, how she admired Renalda to come to a new place and make it a home."
  protag "How do you know so much about Grimalli?"
  molly "Molly wants to write a book about her. She was an unmarried woman with society influence on her own merits. Gives hook to visit the garden society."
  protag "Protag asks about book store"
  molly "Molly loves books and how stories can outlast time."
  if weekTwoTed == True:
    jump molly2reading
  menu:
    "FLIRT":
      $ weekTwoFlirt = True
      jump molly2reading
    "Agree":
      jump molly2reading

label molly2reading:
  if weekTwoFlirt == True:
    protag "FLIRTing conversation ensues"
    molly "I AM INTO THIS"
  else:
    protag "I agree reading is the best"
    molly "I KNOW, RIGHT?"
  molly "Molly asks about reading."
  menu:
    "No Time":
      $ friendshipMolly = friendshipMolly - 1
      $ romanceMolly = romanceMolly - 1
      hide molly
      show molly sad
      molly "oh, that's too bad. I always try to find time to read no matter what."
      hide molly sad
      show molly
    "Quote poetry":
      protag "I QUOTETH ALL THE POETRY. SHALL I COMPARE THEE TO A SUMMER DAY!?"
      $ romanceMolly = romanceMolly + 1
      hide molly
      show molly flirt
      molly "ooooooooo yeah"
      hide molly flirt
      show molly
    "Gardening Books":
      $ friendshipMolly = friendshipMolly + 1
      hide molly
      show molly happy
      molly "Haha, ever the practical one, aren't you. I can appreciate that."
      hide molly happy
      show molly
  molly "Well, I really should be getting back to my apartment. It was lovely talking to you!"
  if weekTwoMolly:
    jump startWeek2AfterTalk
  jump endWeek2AfterTalk
