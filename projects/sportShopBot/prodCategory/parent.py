from api.sendReq import makeApiCall

from utils.getProdItem import getProdItem

from urls.mkUrl import prepareUrl

from botCommands.BotCommand import BotCommand


class ProdCatparent:

    def __init__(self, bot, msg, cli, main_menu, prodCatObj, botCmdObj: BotCommand):

        self.bot = bot
        self.msg = msg
        self.cli = cli
        self.main_menu = main_menu
        self.prodCatObj = prodCatObj
        self.botCmdObj = botCmdObj

    async def getParId(self, cat_id: int):

        url = prepareUrl("cat par list", [cat_id])
        cat = await getProdItem(self.botCmdObj,
                                url,
                                "cats",
                                tp="cat_par",
                                objId=cat_id)
        if cat == "item":
            return "item"
        elif cat == "empty":
            await self.prodCatObj.doGet(cat_id)
        return cat

    async def addParent(self, cat_id: int):

        par_id = await self.getParId(cat_id)

    async def remParent(self, cat_id: int):

        url = prepareUrl("remove cat par", [cat_id])

        await makeApiCall(url, 'delete')

        await self.botCmdObj.sendMsg("The parent category was deleted")

        await self.prodCatObj.doGet(cat_id)
