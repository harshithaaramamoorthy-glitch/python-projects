while True:
    d={'hello':'hi! how are you?',
       'fine':'what about you!',
       'how is your studies going':'going good',
       'WHAT ABOUT YOUR FAMILY MEMBERS':'all are fine'
       'exit':'goodbye!it was nice to meeting you.'
       }
    user = input("you:")
    if user.upper() in ["BYE","EXIT","QUIT"]:
        print("bot:goodbye!")
        break
    if user.lower() in ["hi","good morning"]:
        print("bot:hello!")
    if user.lower() in ["how are you"]:
        print("bot:fine,what about you!")
    if user.lower() in ["how is your studies going"]:
        print("bot:going good!")
    if user.upper() in ["WHAT ABOUT YOUR FAMILY MEMBERS"]:
        print("bot:all are fine!")
    if user.lower() in ["bye"]:
        print("bot:goodbye!")