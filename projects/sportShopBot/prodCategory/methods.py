from api.sendReq import makeApiCall

from urls.mkUrl import prepareUrl

from botCommands.BotCommand import BotCommand

from prodCategory.parent import ProdCatparent
from prodMan.prod import ProdHandle

from utils.getInput import mkInpt
from utils.getProdItem import getProdItem
from utils.getCat import prGetText


class ProdCatMethods:

    def __init__(self, bot, msg, cli, main_menu, botCmdObj: BotCommand):

        self.bot = bot
        self.msg = msg
        self.cli = cli
        self.main_menu = main_menu
        self.botCmdObj = botCmdObj

    async def doList(self):

        url = prepareUrl("cat list")
        cat = await getProdItem(self.botCmdObj,
                                url,
                                "cats",
                                tp='cat')
        if cat != "menu" and cat != "back" and cat != "empty":
            # await self.doGet(int(cat['id']))
            pass
        else:
            await self.main_menu(self.cli, self.msg)

    async def doGet(self, cat_id: int):

        url = prepareUrl("get or delete or edit cat", [cat_id])
        response = await makeApiCall(url, 'get')

        cat = response['cat']

        txt = await prGetText(cat)

        await self.botCmdObj.sendMsg(txt)

        input = await self.botCmdObj.askUser("cat manage")

        if input == "1":
            prodMan = ProdHandle(self.bot, self.msg, self.cli, self.main_menu, cat_id, self, self.botCmdObj)
            await prodMan.doList()
        elif input == "2":
            prodMan = ProdHandle(self.bot, self.msg, self.cli, self.main_menu, cat_id, self, self.botCmdObj)
            await prodMan.doCreateUpdate(post=True)
        elif input == "3":
            await self.doCreateUpdate(post=True)
        elif input == "4":
            await self.doDelete(cat_id)
        elif input == "5":
            await self.doCreateUpdate(post=False, ttl=cat['title'], desc=cat['description'], cat=cat)
        elif input == "6":
            prodCatPar = ProdCatparent(self.bot, self.msg, self.cli, self.main_menu, self, self.botCmdObj)
            await prodCatPar.remParent(cat['id'])
        elif input == "7":
            prodCatPar = ProdCatparent(self.bot, self.msg, self.cli, self.main_menu, self, self.botCmdObj)
            await prodCatPar.addParent(cat['id'])
        elif input == "8":
            await self.main_menu(self.cli, self.msg)
        else:
            await self.doList()

    async def doDelete(self, cat_id: int):

        url = prepareUrl("get or delete or edit cat", [cat_id])

        input = await self.botCmdObj.askUser("conf cat del")

        if input == "Yes":

            await makeApiCall(url, 'delete')

            await self.botCmdObj.sendMsg("The selected category was deleted!")
            await self.doList()
        elif input == "Main menu":
            await self.main_menu(self.cli, self.msg)
        else:
            await self.doGet(cat_id)

    async def doCreateUpdate(self, post: bool, ttl=False, desc=False, cat=None):

        if post is True:
            text = "Added new category"
            url = prepareUrl("add cat")
        else:
            text = "Edited category"
            cat_id = int(cat['id'])
            url = prepareUrl("get or delete or edit cat", [cat_id])

        title = await mkInpt("title", self.botCmdObj, value=ttl, post=post)
        if title != "menu" and title != "back":
            description = await mkInpt("description", self.botCmdObj, value=desc, post=post)
            if description != "menu" and description != "back":

                data = {"title": title,
                        "description": description}

                if post is True:

                    response = await makeApiCall(url, 'post', data)
                else:
                    response = await makeApiCall(url, 'put', data)

                cat = response['cat']

                await self.botCmdObj.sendMsg(text)
                await self.doGet(int(response['cat']['id']))

            elif description == "menu":
                await self.main_menu(self.cli, self.msg)
            else:
                if post is True:
                    await self.main_menu(self.cli, self.msg)
                else:
                    await self.doGet(int(cat['id']))
        elif title == "menu":
            await self.main_menu(self.cli, self.msg)
        else:
            if post is True:
                await self.main_menu(self.cli, self.msg)
            else:
                await self.doGet(int(cat['id']))
