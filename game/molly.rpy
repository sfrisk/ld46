label molly1:
  scene bg manor
  show molly
  "As Ted leaves, Molly is quick to replace him."
  molly "Hi, I just wanted to have a change to introduce myself again. I'm Molly Grimalli."
  molly "Why did you decide to come to Elmhearst?"
  menu:
    "Firt":
      $ romanceMolly = romanceMolly + 1
      protag "Why, to meet lovely flowers, such as yourself."
      hide molly
      show molly flirt
      molly "You think I'm a flower? Why, aren't you a charmer."
      protag "In all seriousness, this job is kinda a dream come true for me."
      hide molly flirt
      show molly
    "The Garden":
      protag "Working at Elmhearst was a job of a lifetime. Really a dream come true."
  molly "I dream of being a writer. When I found out that The Elmhearst was opening up for apartment living I simple had to come!"
  molly "For now though, I work at a local bookstore, and look for information on Renalda. I want to write a book about her some day."
  molly "What are your dreams?"
  menu:
    "Horticulturist":
      "I really want to become a horticulturist some day."
      $ isHorticulturist = True
    "Apothacary/Herbalist":
      "I've really been facinated with plant based medicine. I hope to get an herb garden growing here soon."
      $ isHorticulturist = False
  hide molly
  show molly happy
  molly "Oh that's lovely."
  protag "By the way, do you know of any good garden shops in town?"
  hide molly happy
  show molly
  molly "There is Blooms and Boughs, a few blocks from here. If you want anything else, you'd have to go to a department store an hour away."
  protag "Oh excellent, I'll make sure to check it out."
  molly "It was lovely talking to you."
  protag "You too!"
  "After she leave, I text Douglas about heading over to Blooms and Boughs for some supplies. He sends me a budget, and I head over."
  jump shop1

label molly2:
  if night == True:
    scene bg manor night
  else:
    scene bg manor
  show molly
  protag "Hi Molly, how are you?"
  hide molly
  show molly happy
  molly "I’m great thank you! How are you adjusting to the new digs?"
  menu:
    "Great!":
      protag "I think it’s a successful transplant,"
      molly "I'm glad to hear that!"
    "Missing Friends":
      protag " I miss my friends back in Ashton."
      molly "I can understand that"
  molly "I moved here about 3 years before Renalda passed away. I was always just drawn to her. I decided to do what she did and make Oakglen my home too."
  protag "You know a lot about her. Does the book store carry any books on her or the house?"
  molly "Molly wants to write a book about her. She was an unmarried woman with society influence on her own merits. Gives hook to visit the garden society."
  protag "You know a lot about her. Does the book store carry any books on her or the house?"
  molly "Oh, no, nothing like that. I joined the Oakglen Garden Society just before she died. Renalda founded it in 1931."
  molly "She was an unmarried woman who cultivated society influence on her own merits. Lucy and the others have been like a family to me. I wanted to write a biography about Renalda and they have been so helpful. They have so many stories about this house."
  if weekTwoTed == True:
    jump molly2reading
  if societyVisits == 0:
    protag "Lucy?"
    molly "Oh, you don't know Lucy? She's the president of the local Gardening Society."
    molly "I think I have her number around her somewhere. She might have some interesting info for you."
  protag "Why did you decide to work in a book store?"
  molly "I love the smell of books. And how stories can outlast time."
  menu:
    "Romantic":
      $ weekTwoFlirt = True
      $ romanceMolly = romanceMolly + 1
      protag "That sounds romantic."
      hide molly
      show molly flirt
      molly "I think so too."
      hide molly flirt
      show molly
      jump molly2reading
    "Agree":
      protag "I couldn’t agree more."
      
      jump molly2reading

label molly2reading:
  molly "Do you like to read?"
  menu:
    "No Time":
      protag "No, I don’t really have time."
      $ friendshipMolly = friendshipMolly - 1
      $ romanceMolly = romanceMolly - 1
      hide molly
      show molly sad
      molly "Oh, that's too bad. I always try to find time to read no matter what."
      hide molly sad
      show molly
    "Quote a Book":
      protag "There are more things in heaven and Earth, Horatio, Than are dreamt of in your philosophy."
      $ romanceMolly = romanceMolly + 1
      hide molly
      show molly flirt
      molly "A fan of the Bard, huh?"
      hide molly flirt
      show molly
    "Gardening Books":
      $ friendshipMolly = friendshipMolly + 1
      protag "Just gardening books really."
      hide molly
      show molly happy
      molly "Haha, ever the practical one, aren't you. I can appreciate that."
      hide molly happy
      show molly
  if weekTwoMolly:
    molly "I should go before I’m late. Bye %(player_name)s!"
    jump startWeek2AfterTalk
  molly "Well, I really should be getting back to my apartment. It was lovely talking to you!"
  jump endWeek2AfterTalk
