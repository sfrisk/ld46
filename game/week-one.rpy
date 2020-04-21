label startWeek1:
  $ week = 1
  $ errands = 1
  jump ted1

label endWeek1:
  scene bg manor night
  if societyVisits == 1:
    $ ghost = True
    "Later that week when I get a moment to myself, I read the construction notes that Lucy from the Garden Society gave me."
    show ghost
    "I'm surprised to find my ability to read the letters suddenly much easier. When I look up, I see a ghost of a woman who looks oddly familiar."
    "The ghost drifts across the courtyard and disapears behind some debris."
    hide ghost
    "Curious, I follow, moving the debris away. I find a strange valve with pipes heading deeper towards the back wall."
  else:
    "Later that week, I read the blueprints I got from the library over dinner. Noticing something odd notated in the blueprints, I go to the courtyard to a corner covered in debris."
    "Beneath the debris, I find a strange valv with pipes heading deeper towards the back wall."
  "I try to turn on valve."
  "It is stuck."
  "I follow the pipes to a hidden terrarium built into wall behind some debris."
  "It is alive but clearly has been neglected. Grow light is busted, water source is clogged, plant is weak, key to open it is missing."
  protag "Maybe Douglas as the key?  I'll ask him in the morning."
  "There is nothing else to do for now, so I go to bed, prepping for the week to come."
  jump startWeek2