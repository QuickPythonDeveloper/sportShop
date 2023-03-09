import os

from api.sendReq import makeApiCall

from urls.mkUrl import prepareUrl

from utils.getProdItem import getProdItem

from botCommands.BotCommand import BotCommand


class ProdImgHandle:

    def __init__(self, bot, msg, cli, main_menu, prod_id, cat_id, prodManObj, botCmdObj: BotCommand):

        self.bot = bot
        self.msg = msg
        self.cli = cli
        self.main_menu = main_menu
        self.prod_id = prod_id
        self.cat_id = cat_id
        self.prodManObj = prodManObj
        self.botCmdObj = botCmdObj

    async def doUpload(self):

        url = prepareUrl("add prod img", [self.prod_id])

        img = await self.botCmdObj.askUser("img manage", img=True)

        if img.text == "1":
            await self.prodManObj.chooseOpt(self.prod_id, self.cat_id)
        elif img.text == "2":
            await self.main_menu(self.cli, self.msg)
        else:
            image = await img.download()
            img_name = image.split("/")[-1]
            img_dir = os.getcwd() + "/downloads/" + img_name
            with open(img_dir, 'rb') as img:

                data = {"image": img}

                response = await makeApiCall(url, 'post', data, file=True)

            os.remove(img_dir)

            await self.botCmdObj.sendMsg("Added image")
            await self.doUpload()

    async def doList(self):

        url = prepareUrl("prod img list", [self.prod_id])
        img = await getProdItem(self.botCmdObj,
                                url,
                                "images",
                                "img",
                                "image",
                                img=True)

        if img != "empty" and img != "menu" and img != "back":
            await self.doDelete(img)
        elif img == "empty" or img == "back":
            await self.prodManObj.chooseOpt(self.prod_id, self.cat_id)
        else:
            await self.main_menu(self.cli, self.msg)

    async def doDelete(self, img):

        url = prepareUrl("delete prod img", [int(img['id'])])

        await makeApiCall(url, 'delete')

        await self.botCmdObj.sendMsg("Deleted image")
        await self.doList()
