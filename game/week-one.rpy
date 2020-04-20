label startWeek1:
  $ week = 1
  $ errands = 1
  jump ted1

label endWeek1:
  scene bg manor
  if societyVisits == 1:
    $ ghost = True
    "Protag reads letters in courtyard."
    show ghost
    "Renalda’s ghost appears then disappears behind debris"
    hide ghost
    "Find a strange valve with pipes heading deeper towards back wall."
    "Try to turn on valve. It is stuck."
    "Follows pipes to a hidden terrarium built into wall behind some debris."
    "It is alive but clearly has been neglected. Grow light is busted, water source is clogged, plant is weak, key to open it is missing."

  else:
    "Protag reads blueprints and locates a strange valve."
    menu:
      "Try to Turn on Valve":
        "It is stuck"
      "Follow pipe"
    "Follows pipe to a hidden terrarium built into wall behind debris"
    "It is alive but clearly has been neglected. Grow light is busted, water source is clogged, plant is weak, key to open it is missing."


  "Garden is ¼ cleared and terrarium is visible with sad looking plant in it."
  jump startWeek2