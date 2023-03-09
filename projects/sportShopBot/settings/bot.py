import os

from settings.tokens import BOT_TOKEN as bot_token, API_ID, API_HASH

from pyrogram import Client


def getBot():

    if not os.path.exists(os.getcwd() + "/settings/{}".format(bot_token[:5])):

        os.makedirs(os.getcwd() + "/settings/{}".format(bot_token[:5]))

    workdir = os.path.dirname(os.path.realpath(__file__)) + "/{}".format(bot_token[:5])

    bot = Client("sportShopBot",
                 api_id=API_ID,
                 api_hash=API_HASH,
                 workdir=workdir,
                 bot_token=bot_token
                 )

    return bot
