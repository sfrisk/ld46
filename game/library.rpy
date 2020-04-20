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
    protag "Hello, I’m looking for historical blueprints of Elmhearst Manor."
  else:
    protag "Hi Libby! Do you think I could keep the blueprints of the house a little longer? I’m working on figuring out some changes and it helps to see the original design."
    librarian "Keep them as long as you want!"
  librarian "What kinds of changes are you looking at?"
  menu:
    "Terrarium":
      $ photoAlbum = True
      jump library2Terrarium
    "Strange Plumbing":
      $ fountainBook = True
      jump library2Plumbing

label library2Terrarium:
  protag "There’s a strange terrarium looking glass case built into the back wall. I can’t get it open and I can’t tell what it used to be."
  librarian "I believe the library has a photo album of a Chamber of Commerce Party she hosted at her estate one night in 1932. Here you can check it out with the blueprints."
  "I go with Libby to the front desk to check out the photo album."
  if libraryVisits == 1:
    "While I'm there, I also check out the blueprints"
  jump library2ending

label library2Plumbing:
  protag "There’s a strange plumbing value that comes out of an access door that looks like a mess of pipes. I can’t tell what they were trying to do with it."
  librarian "ou know, Miss Grimalli used to be completely mesmerized by these french fountains at an estate she stayed at in the 30’s."
  librarian "I think they were featured in this book about Art Nouveau water features. It’s in right now."
  "I go with Libby to the front desk to check out the Art Nouveau book."
  if libraryVisits == 1:
    "While I'm there, I also check out the blueprints"
  jump library2ending

label library2ending:
  hide librarian
  show librarian happy
  "As she is checking out my books, Libby smiles at me. I find myself distrusting that smile."
  librarian "So you’ve been here a couple weeks now. Has anyone caught your eye?"
  menu:
    "Run away":
      "Wut? Who ASKS something like that?"
      protag "You know, I really gotta run. Bye Libby!"
    "Ted":
      $ romanceTed = romanceTed + 1
      "I think Ted is really sweet."
    "Molly":
      $ romanceMolly = romanceMolly + 1
      " I think Molly is really nice."
  librarian "*chuckles*"
  "I decide to make a hasty retreat before she asks anything else"
  hide librarian happy
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