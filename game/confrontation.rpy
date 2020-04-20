label confrontation:
  ## JAVERT. AT LAST. WE SEE EACH OTHER PLAIN!
  scene bg manor
  "I arrive back at the manor after running errands to a loud argument"

  protag "What is going on here?"
  show librarian
  prez "Libby witchhunter, against coven. Had Renalda’s last will. "
  hide librarian
  show douglas
  douglas "Douglas wants to suppress coven in aunt past"
  hide douglas
  show cam
  cam "Cam wants to get a credit on the new day lily, admired Renalda as horticulturist"
  hide cam
  show prez
  prez "Lucy wants her coven protected and the grimoire from Elmhearst."
  hide prez
  show ted
  ted "Ted wants a sensational story and this is it."
  hide ted
  show molly
  molly "Molly is a witch in the coven but she wants everyone to move on."
  hide molly

  menu:
    "What do you do?"
    "Side with Libby":
      $ friendshipMolly = -10
      $ romanceMolly = -10
    "Protect the Coven":
      $ friendshipTed = -10
      $ romanceTed = -10
    "Side with Douglas":
      $ friendshipMolly = -10
      $ romanceMolly = -10
    "Side with Cam":
      $ friendshipTed = -10
      $ romanceTed = -10
      $ friendshipMolly = -10
      $ romanceMolly = -10

  if romanceMolly > 5:
    jump romanceMolly
  if romanceTed > 5:
    jump romanceTed
  jump noRomance

label romanceMolly:
  show molly flirty
  "I romance the Molly!"
  hide molly flirty
  jump lilyBooms


label romanceTed:
  show ted flirty
  "Romance the Ted!"
  hide ted flirty
  jump lilyBlooms

label noRomance:
  "I don't romance anyone."
  "Lily doesn’t bloom but it is very alive."
  "the end"
  return

label lilyBlooms:
  show prez left
  show cam right
  "OMG THE LILY BLOOMED AS I ASKED THEM OUT. OMG"
  "CAM AND LUCY CHECK EACH OTHER OUT"
  "OMG THE END"
  return