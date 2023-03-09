from botCommands.BotCommand import BotCommand


async def mkInpt(label, botCmdObj: BotCommand, post=False, value=False, optional=False):
    inpt = await botCmdObj.askUser("mk inpt", options=[post, label, optional])

    if inpt == "1":
        return "menu"
    elif inpt == "2":
        return "back"
    elif inpt == "-1":
        inpt = value
    elif inpt == "-2":
        inpt = None

    return inpt
