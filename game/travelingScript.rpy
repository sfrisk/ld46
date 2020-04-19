define librarian = Character("Libby Corso")
define shopOwner = Character("Cam Webber")
define president = Character("President")

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
  show shopOwner happy
  shopOwner "Hello, welcome to Blooms and Boughs, how can I help you?"
  menu:
    "Gardening Tools":
      protag  "I’m looking for some tools to help me pull out some old flower beds and containers."
    "Information":
      protag "I’m looking for some information about local flora to help replant a historic garden."
  shopOwner "I think I have just the thing. You must be the new building manager over at the Elmhearst."
  shopOwner "I’m Cam Webber, the owner here. Your boss stirred up the town when he bought that place. It looks like the grounds are in pretty good shape though."
  protag "How did you know who I was?"
  shopOwner "Sorry, gossip travels fast when one of the people in your building is a news anchor."
  shopOwner "It’s not bad, though. We’ve been waiting for you to get here. Just excitement really. Well, here are the tools and the books about our local climate."
  shopOwner "Let me know if you need anymore help."
  menu:
    "I think I see what I need":
      shopOwner "Great, just pick out what you want and I’ll have everything sent over to the manor."
    "Hmm, do you have any books about the historic gardens from around here?":
      shopOwner "Sorry, I don’t. You could check the library. Or you could go talk to the Garden Society. I think the lady who built that house founded it or something. Here’s the card for their President."
  shopOwner "Thank you for stopping by! See you again soon!"
  
  "I didn’t expect to cause a stir coming here. It’s strange to be known before you introduce yourself but it looks like everyone in town keeps an eye on each other."
  "I guess I better figure out who I want to see about the gardens this week. There’s so much work to be done."
  return

label society:
  "we worked on the garden. the end"
  return