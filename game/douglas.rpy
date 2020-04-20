label douglas1:
  scene bg manor

  "Week one douglas stuff?"

label douglas2:
  scene bg manor
  show douglas
  protag "Oh, hey Douglas! How's it going today?"
  douglas "Gives an answer"
  douglas "How goes the progress on the courtyard?"
  protag "I was wondering if you had keys for the courtyard?"
  douglas "Why do you need additional keys for the courtyard?"
  menu:
    "Tell him about the terrarium":
      protag "I found a terrarium in there last night, but it's locked up."
      douglas "A response about the terrarium"
    "Tell him about old plumbing line access":
      protag "I found an old plumbing line access and wanted to see where it went."
      douglas "A response to this."
  douglas "Well, I do have this old skeleton key, if you're interested."
  "Well that key LOOKS like it would work."
  "RING RING"
  douglas "I'm sorry, I must get this. We'll talk later, but for now here is more funds for courtyard"
  douglas "Yes? This is Douglas speaking . . ."
  hide douglas
  "Oo, more funds? I could definitely use this on the terrarium!"
  "As I sit there thinking about all the things I could get with the extra funds, I see Ted and Molly entering the courtyard from different directions."
  "Describe Molly"
  "Describe Ted"
  "I have some time, I should say hello to one of them."
  menu:
    "talk to molly":
      $ weekTwoMolly = True
      jump molly2
    "talk to Ted":
      $ weekTwoTed = True
      jump ted2
