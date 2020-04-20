label travel:
  if errands == 0:
    if week == 1:
      jump endWeek1
    if week == 2:
      jump endWeek2
    if week == 3:
      jump endWeek3
  scene bg townMap
  if week == 1 and haveGardenCard == False:
    "I guess I could check out the library?"
    jump library1
  if week == 1 and haveGardenCard == True:
    "Cam did mention a Garden Society. [some ideas about garden society]"
    "Or I could go to the library [some ideas about library stuff]"
  if week == 2 and haveGardenCard == False:
    "Molly gave me some info about a Gardening Society. I should check them out."
  $ errands = 0
  menu:
    "Where do I want to go ?"
    "Town Library":
      if libraryVisits == 0:
        jump library1
      if libraryVisits == 1:
        jump library2
      if libraryVisits == 2:
        jump library3
    "Garden Society":
      if societyVisits == 0:
        jump society1
      if societyVisits == 1:
        jump society2
      if societyVisits == 2:
        jump society3
