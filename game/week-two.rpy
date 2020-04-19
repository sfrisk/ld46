label startWeek2:
  $ errands = 1
  $ week = 2
  $ weekTwoTed = False
  $ weekTwoMolly = False
  "WEEK 2 BABY"
  "Talk to Boss"
  "Sees Ted doing a thing. Sees molly doing a different thing"
  menu:
    "talk to molly":
      "this will trigger talking to Molly when she's mapped out"
      $ weekTwoMolly = True
    "talk to Ted":
      "this will trigger talking to Ted when he's mapped out"
      $ weekTwoTed = True
  jump shop2

label endWeek2:
  "Interact in Garden ⅔ cleared now, new plants in places."
  if ghost == True:
    "Renalda shows ritual altar behind terrarium wall. Garden looks more witchy"
  else:
    "Plumbing problem found, central fountain works. Garden look historic."
  if weekTwoTed == True:
    "Molly shows up for a convo"
  else:
    "ted shows up for a convo"
  "end week 2"
  jump startWeek3