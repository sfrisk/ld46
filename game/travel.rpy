label travel:
  if errands == 0:
    if week == 1:
      jump endWeek1
    if week == 2:
      jump endWeek2
    if week == 3:
      jump endWeek3
  scene bg manor
  if week == 1 and haveGardenCard == False:
    "I guess I could check out the library?"
    jump library1
  if week == 1 and haveGardenCard == True:
    "Cam did mention a Garden Society."
    "Or I could go to the library and try and find the original blueprints in the archive."
  if week == 2 and haveGardenCard == False:
    "Molly gave me some info about a Gardening Society. Maybe I should check them out?"
  $ errands = 0
  menu:
    "Where do I want to go ?"
    "Town Library":
      if week == 1:
        jump library1
      if week == 2:
        jump library2
      if week == 3:
        jump library3
    "Garden Society":
      "I call the Garden Society to find out a good time to visit."
      if week == 1:
        jump society1
      if week == 2:
        jump society2
      if week == 3:
        jump society3
