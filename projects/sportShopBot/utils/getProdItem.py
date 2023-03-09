from utils.showLs import showList

from botCommands.BotCommand import BotCommand


async def getProdItem(botCmdObj: BotCommand, url, key, tp, title="title", img=False, objId=None):
    itms = await showList(botCmdObj, url, key, title, img, tp, objId)

    if len(itms) == 0:
        return "empty"

    if img is True:

        inpt = await botCmdObj.askUser("del img")

        if inpt[0] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            itm = itms[int(inpt) - 1]
            return itm
        elif inpt == "1":
            return "back"
        else:
            return "menu"

    return "item"
