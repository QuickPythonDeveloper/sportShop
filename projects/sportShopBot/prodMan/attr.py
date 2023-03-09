from api.sendReq import makeApiCall

from utils.getInput import mkInpt
from utils.getProdItem import getProdItem
from utils.getAttr import prpLsText

from urls.mkUrl import prepareUrl

from botCommands.BotCommand import BotCommand


class ProdAttrHandle:

    def __init__(self, bot, msg, cli, main_menu, prod_id: int, cat_id: int, prodManObj, botCmdObj: BotCommand):
        self.bot = bot
        self.msg = msg
        self.cli = cli
        self.main_menu = main_menu
        self.prod_id = prod_id
        self.cat_id = cat_id
        self.prodManObj = prodManObj
        self.botCmdObj = botCmdObj

    async def doList(self):

        url = prepareUrl("attr list", [self.prod_id])
        attr = await getProdItem(self.botCmdObj,
                                 url,
                                 "attrs",
                                 tp="attr",
                                 title="key")
        if attr != "empty" and attr != "menu" and attr != "back":
            pass
        elif attr == "empty" or attr == "back":
            await self.prodManObj.chooseOpt(self.prod_id, self.cat_id)
        else:
            await self.main_menu(self.cli, self.msg)

    async def chooseOpt(self, attr_id: int):

        url = prepareUrl("get or delete or edit attr", [attr_id])

        response = await makeApiCall(url, 'get')

        attr = response['attr']
        txt = await prpLsText(attr)
        await self.botCmdObj.sendMsg(txt)

        input = await self.botCmdObj.askUser("attr manage")

        if input == "1":
            await self.doList()
        elif input == "2":
            await self.doCreateUpdate(True)
        elif input == "3":
            await self.doCreateUpdate(False, attr['key'], attr['value'],
                                      attr['note'], attr=attr)
        elif input == "4":
            await self.doList()
        elif input == "5":
            await self.doDelete(attr)
        else:
            await self.main_menu(self.cli, self.msg)

    async def doCreateUpdate(self, post: bool, key=False, value=False, note=False, attr=None):

        if post is True:
            text = "Added new description"
            url = prepareUrl("add attr", [self.prod_id])
        else:
            text = "Edited description"
            attr_id = int(attr['id'])
            url = prepareUrl("get or delete or edit attr", [attr_id])

        key = await mkInpt("Description title", self.botCmdObj, value=key, post=post)
        if key != "menu" and key != "back":
            value = await mkInpt("Description", self.botCmdObj, value=value, post=post)
            if value != "menu" and value != "back":
                note = await mkInpt("Extra Description", self.botCmdObj, post=post, value=note, optional=True)
                if note != "menu" and note != "back":

                    data = {"key": key,
                            "value": value,
                            "note": note}

                    if post is True:
                        response = await makeApiCall(url, 'post', data)
                    else:
                        response = await makeApiCall(url, 'put', data)

                    if response['status'] == 'max number of attrs':

                        await self.botCmdObj.sendMsg("Max number of descriptions have been created for this product")
                        await self.doList()
                    else:

                        attr = response['attr']
                        attr_id = int(attr['id'])

                        await self.botCmdObj.sendMsg(text)
                        await self.chooseOpt(attr_id)

                elif note == "back":
                    if post is False:
                        await self.chooseOpt(attr)
                    else:
                        await self.prodManObj.chooseOpt(self.prod_id, self.cat_id)
                else:
                    await self.main_menu(self.cli, self.msg)
            elif value == "back":
                if post is False:
                    await self.chooseOpt(attr)
                else:
                    await self.prodManObj.chooseOpt(self.prod_id, self.cat_id)
            else:
                await self.main_menu(self.cli, self.msg)
        elif key == "back":
            if post is False:
                await self.chooseOpt(attr)
            else:
                await self.prodManObj.chooseOpt(self.prod_id, self.cat_id)
        else:
            await self.main_menu(self.cli, self.msg)

    async def doDelete(self, attr):

        url = prepareUrl("get or delete or edit attr", [int(attr['id'])])

        await makeApiCall(url, 'delete')

        await self.botCmdObj.sendMsg("Deleted description")

        await self.doList()
