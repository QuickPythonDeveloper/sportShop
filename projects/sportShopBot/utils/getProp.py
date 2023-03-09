from urls.mkUrl import prepareUrl

from api.sendReq import makeApiCall

from botCommands.BotCommand import BotCommand


async def prpPropTxt(prop):
    intro = "Production attribute"

    if prop['color'] is None:
        prop['color'] = "-"
    if prop['weight'] is None:
        prop['weight'] = "-"
    if prop['size'] is None:
        prop['size'] = "-"
    color = "color" + "\n" + prop['color']
    weight = "weight" + "\n" + str(prop['weight'])
    size = "size" + "\n" + str(prop['size'])
    price = "price" + "\n" + str(prop['price'])
    stc_count = "Stock count" + "\n" + str(prop['stock_count'])

    txt = intro + "\n" + color + "\n" + weight + "\n" + size + "\n" + price + "\n" + stc_count

    return txt


async def getProp(prop_id: int, botCmdObj: BotCommand):
    url = prepareUrl("get or delete or edit prod prop", [prop_id])

    response = await makeApiCall(url, 'get')

    prop = response['prop']
    cat_id = prop['cat_id']
    prod_id = prop['prod_id']
    next_id = prop['next_id']
    if next_id is None:
        next_id = 'none'

    prev_id = prop['prev_id']
    if prev_id is None:
        prev_id = 'none'

    txt = await prpPropTxt(prop)

    await botCmdObj.sendMsg(txt, "get prop", [prop_id, cat_id, prod_id, next_id, prev_id])
