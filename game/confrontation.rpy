label confrontation:
  ## JAVERT. AT LAST. WE SEE EACH OTHER PLAIN!
  scene bg manor
  "Cam and I arrive at he manor to see what seems to be everyone in down all yelling at each other."
  protag "ENOUGH! Listen, there’s a lot of sneaking around here. Let’s have it out. Each of you gets to tell me what you are doing here and what you want. "
  show librarian
  prez "My name is Liberty Corso and I am a witch hunter. I was on the trail of Renalda’s coven when she died and I have been working to keep the suspected witches from gaining ground in Oakglen. I have been holding them at bay."
  hide librarian
  show douglas
  douglas "When Libby failed to kill Renalda, my mother sent me to win the battle for the estate to make sure that no one would know that she was a witch. I am to cement her legacy as a horticulturalist with whatever you find."
  hide douglas
  show cam
  cam "I wanted to get a credit for the new flower with you and Renalda. She was a hero of mine growing up. She could manipulate plants with magic! Everyone in the right horticultural circles knew she was a witch. She was a great one. I want to see if that terrarium is magic."
  hide cam
  show prez
  prez "What kind of fucked up people kill people for being witches? What is this? 1634? Get out of here with that bullshit. I just want the grimoire from the altar. Douglas already made sure we have no home here. And plants that respond to magic?"
  hide prez
  show ted
  ted "I was looking for a sensational story and this is it! Covens! Witch hunters! Magic plants"
  hide ted
  show molly
  molly "Lucy! Why can’t we all just move on? Renalda wouldn’t want us to fight!"
  hide molly

  menu:
    "What do you do?"
    "Side with Libby and Douglas":
      show molly mad
      "Molly really didn't seem to like that answer"
      hide molly mad
      $ romanceMolly = -10
    "Side with Lucy":
      show ted mad
      "Ted really didn't seem to like that answer"
      hide ted mad
      $ romanceTed = -10
    "Side with Cam":
      "I glance at Ted and Lucy. Neither seem happy with that answer."
      $ romanceTed = -10
      $ romanceMolly = -10

  if romanceMolly > 2:
    jump romanceMolly
  if romanceTed > 2:
    jump romanceTed
  jump noRomance

label romanceMolly:
  "Deciding to defuse the situation, I walk up to Molly."
  show molly flirty
  protag "Would you like to go to dinner with me?"
  molly "YES!"
  hide molly flirty
  jump lilyBooms


label romanceTed:
  "Deciding to defuse the situation, I walk up to Molly."
  show ted flirty
  protag "Would you like to go to dinner with me?"
  ted "YES"

  hide ted flirty
  jump lilyBlooms

label noRomance:
  ". . . We all just kinda look at each other awkwardly."
  "there would be more to this ending, but LDJAM is over."
  return

label lilyBlooms:
  show prez left
  show cam right
  "To my surprise, as my love says yes, the flower in the terranium starts to flower."
  "OMG THE LILY BLOOMED AS I ASKED THEM OUT. OMG"
  "CAM AND LUCY CHECK EACH OTHER OUT"
  "OMG THE END"
  return