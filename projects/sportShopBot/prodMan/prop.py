from api.sendReq import makeApiCall

from urls.mkUrl import prepareUrl

from utils.getProdItem import getProdItem
from utils.getInput import mkInpt
from utils.getProp import prpPropTxt

from botCommands.BotCommand import BotCommand


class ProdPropHandle:

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

        url = prepareUrl("prod prop list", [self.prod_id])
        size = await getProdItem(self.botCmdObj,
                                 url,
                                 "props",
                                 tp="prop",
                                 title="price")
        if size != "empty" and size != "menu" and size != "back":
            # await self.chooseOpt(size)
            pass
        elif size == "empty" or size == "back":
            await self.prodManObj.chooseOpt(self.prod_id, self.cat_id)
        else:
            await self.main_menu(self.cli, self.msg)

    async def chooseOpt(self, prop_id: int):

        # await self.doGet(prop_id)
        url = prepareUrl("get or delete or edit prod prop", [prop_id])
        response = await makeApiCall(url, 'get')

        prop = response['prop']
        txt = await prpPropTxt(prop)

        await self.botCmdObj.sendMsg(txt)

        input = await self.botCmdObj.askUser("prop manage")

        if input == "1":
            await self.doList()
        elif input == "2":
            await self.doCreateUpdate(True)
        elif input == "3":
            await self.doCreateUpdate(False, prop['weight'], prop['color'], prop['size'],
                                      prop['price'], prop['stock_count'], prop=prop)
        elif input == "4":
            await self.doList()
        elif input == "5":
            await self.doDelete(prop)
        else:
            await self.main_menu(self.cli, self.msg)

    async def doCreateUpdate(self, post: bool, weight=False, color=False,
                             size=False, price=False, stc_count=False, prop=None):

        if post is True:
            text = "6"
            url = prepareUrl("add prod prop", [self.prod_id])
        else:
            text = "7"
            prop_id = int(prop['id'])
            url = prepareUrl("get or delete or edit prod prop", [prop_id])

        weight = await mkInpt("Weight", self.botCmdObj, value=weight, post=post, optional=True)
        if weight != "menu" and weight != "back":
            color = await mkInpt("Color", self.botCmdObj, value=color, post=post, optional=True)
            if color != "menu" and color != "back":
                size = await mkInpt("Size", self.botCmdObj, value=size, post=post, optional=True)
                if size != "menu" and size != "back":
                    price = await mkInpt("Price", self.botCmdObj, value=price, post=post)
                    if price != "menu" and price != "back":
                        stc_count = await mkInpt("Stock count", self.botCmdObj, post=post, value=stc_count)
                        if stc_count != "menu" and stc_count != "back":

                            data = {"weight": weight,
                                    "color": color,
                                    "size": size,
                                    "price": float(price),
                                    "stock_count": int(stc_count)}

                            if post is True:
                                response = await makeApiCall(url, 'post', data)
                            else:
                                response = await makeApiCall(url, 'put', data)

                            prop = response['prop']
                            prop_id = int(prop['id'])

                            await self.botCmdObj.sendMsg(text)
                            await self.chooseOpt(prop_id)

                        elif stc_count == "back":
                            if post is False:
                                await self.chooseOpt(prop)
                            else:
                                await self.prodManObj.chooseOpt(self.prod_id, self.cat_id)
                        else:
                            await self.main_menu(self.cli, self.msg)
                    elif price == "back":
                        if post is False:
                            await self.chooseOpt(prop)
                        else:
                            await self.prodManObj.chooseOpt(self.prod_id, self.cat_id)
                    else:
                        await self.main_menu(self.cli, self.msg)
                elif size == "back":
                    if post is False:
                        await self.chooseOpt(prop)
                    else:
                        await self.prodManObj.chooseOpt(self.prod_id, self.cat_id)
                else:
                    await self.main_menu(self.cli, self.msg)
            elif color == "back":
                if post is False:
                    await self.chooseOpt(prop)
                else:
                    await self.prodManObj.chooseOpt(self.prod_id, self.cat_id)
            else:
                await self.main_menu(self.cli, self.msg)
        elif weight == "back":
            if post is False:
                await self.chooseOpt(prop)
            else:
                await self.prodManObj.chooseOpt(self.prod_id, self.cat_id)
        else:
            await self.main_menu(self.cli, self.msg)

    async def doDelete(self, prop):

        url = prepareUrl("get or delete or edit prod prop", [int(prop['id'])])
        response = await makeApiCall(url, 'delete')

        await self.botCmdObj.sendMsg("Added attribute")
        await self.doList()
