from urls.mkUrl import prepareUrl

from api.sendReq import makeApiCall

from botCommands.BotCommand import BotCommand


async def prpLsText(attr):
    intro = "Description"

    key = attr['key'] + ":"
    value = attr['value']
    if attr['note'] is None:
        attr['note'] = "-"
    note = "Extra Description" + "\n" + attr['note']

    obj = key + "\t" + value + "\n\n" + note + "\n\n"

    txt = intro + "\n\n" + obj
    return txt


async def getAttr(attr_id: int, botCmdObj: BotCommand):
    url = prepareUrl("get or delete or edit attr", [attr_id])

    response = await makeApiCall(url, 'get')

    attr = response['attr']
    prod_id = int(attr['product_id'])
    cat_id = int(attr['cat_id'])
    next_id = attr['next_id']
    if next_id is None:
        next_id = 'none'

    prev_id = attr['prev_id']
    if prev_id is None:
        prev_id = 'none'

    txt = await prpLsText(attr)

    await botCmdObj.sendMsg(txt, "get attr", [attr_id, cat_id, prod_id, next_id, prev_id])
