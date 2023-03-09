from api.sendReq import makeApiCall

from urls.mkUrl import prepareUrl

from utils.getCat import prGetText

from botCommands.BotCommand import BotCommand


async def getCatPar(par_id: int, botCmdObj: BotCommand, cat_id: int):
    url = prepareUrl("get or delete or edit cat", [par_id])

    response = await makeApiCall(url, 'get')

    par = response['cat']
    txt = await prGetText(par)

    next_id = par['next_id']
    if next_id is None:
        next_id = 'none'
    else:
        if int(next_id) == cat_id:
            next_id = 'none'

    prev_id = par['prev_id']
    if prev_id is None:
        prev_id = 'none'
    else:
        if int(prev_id) == cat_id:
            prev_id = 'none'

    await botCmdObj.sendMsg(txt, "get cat par", [cat_id, par_id, next_id, prev_id])
