define librarian = Character("Libby", color="#8d7db3")
define cam = Character("Cam")
define prez = Character("Lucinda", color="#00b6b9")

label traveling:
  scene bg townMap
  menu:
    "Where do I want to go this week?"
    "Town Library":
      jump library
    "Blooms and Boughs":
      jump shop
    "Garden Society":
      jump society

label library:
  scene bg library
  show librarian
  librarian "Welcome to the Oakglen Public Library! How can I direct you?"
  protag "Hello, I’m looking for some information on Elmhearst Manor."
  show librarian happy
  librarian "Oh, what a lovely house!"
  hide librarian happy
  show librarian sad
  librarian "It’s so upsetting they decided to turn it into apartments, but I suppose it couldn’t be helped."
  hide librarian sad
  show librarian
  librarian "What sorts of information would you like, dear?"
  menu:
    "I’m looking for the original blueprints of the manor house.":
      $ choice = 'blueprints'
    "I’m looking for any books about Miss Grimalli’s gardens.":
      $ choice = 'books'
  librarian "I can help you find that. Please follow me."
  librarian "I’m Libby Corso, the town librarian and unofficial historian."
  librarian "I often have to track down books for that nice young lady that lives in Elmhearst and works at the book store. She’s been talking about writing a book about Renalda for ages. Always wants to see the old deeds and records around town"
  hide librarian
  show librarian happy
  librarian "It’s so nice to see young people interested in the history of a place. "
  protag "Oh, Molly never mentioned that. How close were you with Miss Grimalli?"
  hide librarian happy
  show librarian
  librarian "Oh heavens, not at all, she and I kept to different circles. She was a very important person in town so of course we all knew of her. "
  protag "I see. Well, here’s the section I was looking for."
  librarian "Please let me know if there’s anything else I can help you find. "
  "That’s odd. Who calls someone by their first name when they aren’t acquainted? And Molly never told me she was writing a book. I guess it makes sense though, she loves books. I’d better get going."
  return

label shop:
  scene bg gardenStoreExterior
  "So I decided to check out the store, Blooms and Boughs, the local garden shop"
  scene bg gardenStoreInterior
  show cam happy
  cam "Hello, welcome to Blooms and Boughs, how can I help you?"
  menu:
    "Gardening Tools":
      protag  "I’m looking for some tools to help me pull out some old flower beds and containers."
    "Information":
      protag "I’m looking for some information about local flora to help replant a historic garden."
  hide cam happy
  show cam
  cam "I think I have just the thing. You must be the new building manager over at the Elmhearst."
  hide cam
  show cam happy
  cam "I’m Cam Webber, the owner here. Your boss stirred up the town when he bought that place. It looks like the grounds are in pretty good shape though."
  protag "How did you know who I was?"
  hide cam happy
  show cam sad
  cam "Sorry, gossip travels fast when one of the people in your building is a news anchor."
  hide cam sad
  show cam happy
  cam "It’s not bad, though. We’ve been waiting for you to get here. Just excitement really. Well, here are the tools and the books about our local climate."
  hide cam happy
  show cam
  cam "Let me know if you need anymore help."
  menu:
    "I think I see what I need":
      hide cam
      show cam happy
      cam "Great, just pick out what you want and I’ll have everything sent over to the manor."
    "Hmm, do you have any books about the historic gardens from around here?":
      hide cam
      show cam sad
      cam "Sorry, I don’t. You could check the library. Or you could go talk to the Garden Society. I think the lady who built that house founded it or something. Here’s the card for their President."
  show cam happy
  cam "Thank you for stopping by! See you again soon!"
  hide cam happy
  "I didn’t expect to cause a stir coming here. It’s strange to be known before you introduce yourself but it looks like everyone in town keeps an eye on each other."
  "I guess I better figure out who I want to see about the gardens this week. There’s so much work to be done."
  return

label society:
  scene gardenSociety
  show prez
  protag "Hi, I'm %(player_name)s, we spoke on the phone? Thank you for taking the time to meet with me."
  prez "Hello, I’m Lucinda Payne, President of the Oakglen Garden Society."
  hide prez
  show prez annoyed
  prez "I understand you’re the new building manager that snake hired to coax out the lost treasures of Renalda Grimalli? "
  protag "Excuse me?"
  hide prez annoyed
  show prez mad
  prez "I take it that you took the job without doing your homework. Let me tell you a little secret, your boss is looking for something at Elmhearst and he’s running out of time. "
  protag "Lost treasures? Time? I don’t understand. I’m just trying to restore the courtyard."
  hide prez mad
  show prez
  prez "Of course you are dear, that’s what he told you after all. If that’s what you want from this, I suppose I can offer what assistance I can, provided you tell me what he’s looking for over there. "
  protag "How are you so sure he is?"
  hide prez
  show prez mad
  prez "Douglas Beckham is a man who always gets what he wants. No matter how he has to do it. "
  hide prez mad
  show prez
  prez "In your world, he is just a real estate guru who helps save historic homes. But in mine, he’s a man who enjoys power."
  hide prez
  show prez annoyed
  prez "Just be certain you’ve got yours in hand or he will take it from you."
  hide prez annoyed
  show prez
  prez "But I disgress, you wanted help with the gardens."
  prez "Here. Renalda kept meticulous notes when the house was being built. You can have her construction notes and letters to the builders. I hope they serve you well."
  protag "Thank you. Cam at Blooms and Boughs said that Miss Grimalli founded the Garden Society in Oakglen? "
  hide prez
  show prez happy
  prez "It’s true. She had the great ability to bring people close to her and make them feel special."
  hide prez happy
  show prez annoyed
  prez "She was our elder and we mourned her passing deeply. We had hoped that she would leave Elmhearst to us so that we would have a permanent home but we were forced to turn to other avenues."
  hide prez annoyed
  show prez mad
  prez "We held a gala in her name and raised enough to build this municipal conservatory, but there has been such push back from the nosy town historian, Libby."
  prez "She thinks we are trampling on the community gardens around town but this conservatory serves a different purpose, much like a vegetable plot could never be mistaken for a botanical garden"
  protag "I see. Well. Thank you. This was very informational."
  hide prez

  "Wow, there’s something seriously twisted going on in this town. And how did Lucinda seem to know so much about my boss, Douglas? Something’s not right."
  
  return