from utils.getCat import getCat
from utils.getCatPar import getCatPar
from utils.getProd import getProd
from utils.getAttr import getAttr
from utils.getProp import getProp

from settings.baseUrl import baseURL

from api.sendReq import makeApiCall

from botCommands.BotCommand import BotCommand


async def showList(botCmdObj: BotCommand, url, key, title, img: bool, tp, objId):
    response = await makeApiCall(url, 'get')

    items = response[key]

    if len(items) != 0:

        if img is False:

            item = items[0]
            itm_id = int(item['id'])
            if tp == 'cat':
                await getCat(itm_id, botCmdObj)
            elif tp == 'cat_par':
                await getCatPar(itm_id, botCmdObj, objId)
            elif tp == 'prod':
                await getProd(itm_id, botCmdObj)
            elif tp == 'prop':
                await getProp(itm_id, botCmdObj)
            elif tp == 'attr':
                await getAttr(itm_id, botCmdObj)

        else:

            for num, itm in enumerate(items):
                url = baseURL[:-1] + itm['image']
                await botCmdObj.sendPhoto(photo=url,
                                          caption=str(num + 1))

        return items

    await botCmdObj.sendMsg("No items to display")

    return items
