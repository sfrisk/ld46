label library1:
  $ libraryVisits = 1
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
    "Blueprints":
      protag "I’m looking for the original blueprints of the manor house."
    "Books":
      protag "I’m looking for any books about Miss Grimalli’s gardens."
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
  hide librarian
  jump travel

label library2:
  $ libraryVisits = 2
  scene bg library
  show librarian
  "VISITING THE LIBRARY FOR THE 2ND TIME"
  protag "Protag greets Libby. Asks to keep blueprints longer."
  librarian "Libby asks about garden"
  menu:
    "Terrarium":
      $ photoAlbum = True
    "Strange Plumbing":
      $ fountainBook = True
  if photoAlbum == True:
    librarian "Libby remarks that Grimalli liked fountains. Recommends book on art nouveau style gardens and water features."
    "Check out book about antique indoor fountains."
  else:
    librarian "Libby remarks on odd art nouveau photos of Renalda’s house the library has."
    "Check out a photo album of a party thrown by Renalda Grimalli for New Years 1932."
  librarian "Libby asks if anyone in town has caught Protag eye yet."
  "WHO ASKS SOMETHING LIKE THIS. OH GOD DECISIONS."
  menu:
    "Run away":
      "Nope nope nope, I can't answer that"
      protag "*stamers*"
      "I run away"
      jump travel
    "Ted":
      "[do we wanna track this Ted approval?]"
    "Molly":
      "[do we wanna track this Molly approval?]"
  librarian "Libby chuckles but approves and protag makes a fast exit."
  hide librarian
  jump travel

label library3:
  $ libraryVisits = 3
  scene bg library
  show librarian
  "VISITING THE LIBRARY FOR THE 3RD TIME"
  hide librarian
  jump travel