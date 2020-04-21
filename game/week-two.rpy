label startWeek2:
  $ errands = 1
  $ week = 2
  $ weekTwoTed = False
  $ weekTwoFlirt = False
  $ weekTwoMolly = False
  $ night = False
  scene bg manor
  "Before I know it, a week has gone by."
  "The courtyard is starting to look better, I can see bits of green starting to poke out of the ground."
  jump douglas2

label startWeek2AfterTalk:
  "Well that was fun. Best get to work. Let's see what Cam has for me today."
  jump shop2

label endWeek2:
  $ night = True
  scene bg manor night
  "I work on the courtyard throughout the week. It's finally starting to look mostly cleared out. Finally Saturday night, I have a chance to take a break."
  if terrariumKey == True:
    show ghost
    "While I relax, a familiar looking ghost appears."
    "She beckons me to a well concealed lever near the glass case. There is a slot for the key Lucinda gave me."
    "With a click, it turns, the case opens and the wall swivels on a track in the floor to reveal a large and ornate altar with a statue of the Goddess on it."
    hide ghost
  elif personalLetters == True:
    "By candlelight in the courtyard, I read the packet of letters I got from Lucy."
    "They're about a summer of visits between Renalda and a French Marquess."
    "They get surprising candid about their lives and Renalda mentions her former lover, a local pastor, as well as how she has taken in a young girl who has no family, knowing the pain of living without it."
  else:
    "Looking over the book I borrowed from the library over dinner, I get an idea."
    "I quickly rush down with a flashlight and examine the pump housing. The pumps have been ripped out, forcefully. I manage to reconnect some lines with hose and clamps and the water starts to filter through the glass case."
  
  if weekTwoFlirt == True:
    "Glancing over, I notice something surprising, the flower in the terrarium has started to bloom."
  "When I'm down, I look up, surprised to see somone approaching."

  if weekTwoTed == True:
    jump molly2
  else:
    jump ted2

label endWeek2AfterTalk:
  scene bg manor night
  jump startWeek3