define librarian = Character("Librarian")
define shopOwner = Character("Owner")
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
  "we went to the library, the end"
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