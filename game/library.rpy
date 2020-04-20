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
  $ libraryVisits = libraryVisits + 1
  scene bg library
  show librarian
  if libraryVisits == 1:
    librarian "Welcome to the Oakglen Public Library! How can I direct you?"
    protag "Hello, I’m looking for some information on Elmhearst Manor."
  else:
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
  $ libraryVisits = libraryVisits + 1
  scene bg library
  show librarian
  librarian "Greets protag"
  protag "Ask about hot house daylilies"
  hide librarian
  show librarian sad
  librarian "I am puzzled."
  protag "Protag explains the setup, terrarium is a hot house for a rare flower and looks like center of a strange display."
  hide librarian sad
  show librarian
  librarian "Libby thinks that you’ve been spending too much time with Molly."
  protag "Protag wants to know why Libby seems upset."
  hide librarian
  show librarian sad
  librarian "Libby reveals town history is steeped in witchcraft. Now witches come here and meddle in people’s lives."
  menu:
    "Apologize":
      "Wow, this seems to have really upset Libby. I should probably apologize."
      protag "I'm sorry if I upset you."
    "???":
      ".... well this is weiiird"
  hide librarian sad
  show librarian
  librarian "Never you mind dear."
  librarian "Libby fetches protag a book on the town charter and history and one on water loving plants."
  protag "Protag notices Renalda’s name on a book return slip inside."
  if libraryVisits == 3:
    "Protag leaves (If visited Libby 3 times, finds a will that leaves Elmhearst to POGS)"
  hide librarian
  jump travel