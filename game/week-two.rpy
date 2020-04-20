label startWeek2:
  $ errands = 1
  $ week = 2
  $ weekTwoTed = False
  $ weekTwoFlirt = False
  $ weekTwoMolly = False
  scene bg manor
  "WEEK 2 BABY"
  jump douglas2

label startWeek2AfterTalk:
  "Well that was fun. Best get to work. Let's see what Cam has for me today."
  jump shop2

label endWeek2:
  scene bg manor
  "Interact in Garden ⅔ cleared now, new plants in places."
  if ghost == True:
    "Renalda shows ritual altar behind terrarium wall. Garden looks more witchy"
  else:
    "Plumbing problem found, central fountain works. Garden look historic."
  if weekTwoFlirt == True:
    "Terrarium Bloooooomed!"
  if weekTwoTed == True:
    jump molly2
  else:
    "ted shows up for a convo"

label endWeek2AfterTalk:
  scene bg manor
  "end week 2"
  jump startWeek3