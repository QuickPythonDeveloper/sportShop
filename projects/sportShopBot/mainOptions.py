from settings.bot import getBot
from utils.showLs import getCat
from utils.getProd import getProd
from utils.getAttr import getAttr
from utils.getProp import getProp
from utils.getCatPar import getCatPar

from urls.mkUrl import prepareUrl

import asyncio

from pyrogram import filters

from prodCategory.methods import ProdCatMethods

from prodMan.prod import ProdHandle
from prodMan.attr import ProdAttrHandle
from prodMan.prop import ProdPropHandle

from api.sendReq import makeApiCall

from botCommands.BotCommand import BotCommand

bot = getBot()


# start command
@bot.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_text(text="Hello")
    await main_menu(client, message)


@bot.on_message(filters.command("options"))
async def main_menu(client, message):
    await asyncio.sleep(1.5)

    botCmd = BotCommand(bot, message)
    input = await botCmd.askUser("cat main")

    await check_buttons(input, client, message, botCmd)


async def check_buttons(inpt, client, message, botCmdObj):
    if inpt == "1":
        await main_menu(client, message)
    elif inpt == "2":
        prodCat = ProdCatMethods(bot, message, client, main_menu, botCmdObj)
        await prodCat.doList()
    elif inpt == "3":
        prodCat = ProdCatMethods(bot, message, client, main_menu, botCmdObj)
        await prodCat.doCreateUpdate(post=True)


@bot.on_message(filters.text)
async def check_buttons2(client, message):
    inpt = message.text
    if inpt == "1":
        await main_menu(client, message)
    elif inpt == "2":
        botCmdObj = BotCommand(bot, message)
        prodCat = ProdCatMethods(bot, message, client, main_menu, botCmdObj)
        await prodCat.doList()
    elif inpt == "3":
        botCmdObj = BotCommand(bot, message)
        prodCat = ProdCatMethods(bot, message, client, main_menu, botCmdObj)
        await prodCat.doCreateUpdate(post=True)


@bot.on_callback_query(filters=filters.regex("manage_cat_[0-9]+"))
async def manage_group(client, query):
    msg = query.message
    botCmdObj = BotCommand(bot, msg)
    await msg.delete()
    cat_id = int(query.data.split('_')[-1])
    prodCat = ProdCatMethods(bot, query.message, client, main_menu, botCmdObj)
    await prodCat.doGet(cat_id)


@bot.on_callback_query(filters=filters.regex("cat_par_[0-9]+_[0-9]+"))
async def choose_cat_parent(client, query):
    msg = query.message

    await msg.delete()
    cat_id = int(query.data.split('_')[-2])
    par_id = int(query.data.split('_')[-1])

    url = prepareUrl("add cat par", [cat_id, par_id])
    response = await makeApiCall(url, 'post')

    botCmdObj = BotCommand(bot, msg)
    await botCmdObj.sendMsg("Added parent category")

    prodCatObj = ProdCatMethods(bot, query.message, client, main_menu, botCmdObj)
    await prodCatObj.doGet(cat_id)


@bot.on_callback_query(filters=filters.regex("next_cat_[0-9]+"))
async def show_next_cat(client, query):
    await query.message.delete()
    botCmdObj = BotCommand(bot, query.message)
    nxt_cat_id = query.data.split('_')[-1]
    if nxt_cat_id == 'none':
        pass
    else:
        nxt_cat_id = int(nxt_cat_id)

        await getCat(nxt_cat_id, botCmdObj)


@bot.on_callback_query(filters=filters.regex("prev_cat_[0-9]+"))
async def show_prev_cat(client, query):
    await query.message.delete()
    botCmdObj = BotCommand(bot, query.message)
    prev_cat_id = query.data.split('_')[-1]
    if prev_cat_id == 'none':
        pass
    else:
        prev_cat_id = int(prev_cat_id)

        await getCat(prev_cat_id, botCmdObj)


@bot.on_callback_query(filters=filters.regex("next_cat_par_[0-9]+_[0-9]+"))
async def show_next_cat_par(client, query):
    await query.message.delete()
    botCmdObj = BotCommand(bot, query.message)
    cat_id = int(query.data.split('_')[-1])
    nxt_cat_id = int(query.data.split('_')[-2])
    if nxt_cat_id == 'none':
        pass
    else:
        nxt_cat_id = int(nxt_cat_id)

        await getCatPar(nxt_cat_id, botCmdObj, cat_id)


@bot.on_callback_query(filters=filters.regex("prev_cat_par_[0-9]+_[0-9]+"))
async def show_prev_cat_par(client, query):
    await query.message.delete()
    botCmdObj = BotCommand(bot, query.message)
    cat_id = int(query.data.split('_')[-1])
    prev_cat_id = int(query.data.split('_')[-2])
    if prev_cat_id == 'none':
        pass
    else:
        nxt_cat_id = int(prev_cat_id)

        await getCatPar(nxt_cat_id, botCmdObj, cat_id)


@bot.on_callback_query(filters=filters.regex("manage_prod_[0-9]+_[0-9]+"))
async def manage_prod(client, query):
    await query.message.delete()
    botCmdObj = BotCommand(bot, query.message)
    prod_id = int(query.data.split('_')[-1])
    cat_id = int(query.data.split("_")[-2])
    prodCat = ProdCatMethods(bot, query.message, client, main_menu, botCmdObj)
    prodMan = ProdHandle(bot, query.message, client, main_menu, cat_id, prodCat, botCmdObj)
    await prodMan.chooseOpt(prod_id, cat_id)


@bot.on_callback_query(filters=filters.regex("next_prod_[0-9]+"))
async def show_next_prod(client, query):
    await query.message.delete()
    botCmdObj = BotCommand(bot, query.message)
    nxt_prod_id = query.data.split('_')[-1]
    if nxt_prod_id == "none":
        pass
    else:

        await getProd(nxt_prod_id, botCmdObj)


@bot.on_callback_query(filters=filters.regex("prev_prod_[0-9]+"))
async def show_prev_prod(client, query):
    await query.message.delete()
    botCmdObj = BotCommand(bot, query.message)
    prev_prod_id = query.data.split('_')[-1]
    if prev_prod_id == "none":
        pass
    else:

        await getProd(prev_prod_id, botCmdObj)


@bot.on_callback_query(filters=filters.regex("prod_back_[0-9]+"))
async def back_prod(client, query):
    await query.message.delete()
    botCmdObj = BotCommand(bot, query.message)
    cat_id = int(query.data.split("_")[-1])
    prodCat = ProdCatMethods(bot, query.message, client, main_menu, botCmdObj)
    await prodCat.doGet(cat_id)


@bot.on_callback_query(filters=filters.regex("manage_attr_[0-9]+_[0-9]+_[0-9]+"))
async def manage_attr(client, query):
    await query.message.delete()
    botCmdObj = BotCommand(bot, query.message)
    prod_id = int(query.data.split('_')[-1])
    cat_id = int(query.data.split('_')[-2])
    attr_id = int(query.data.split('_')[-3])
    msg = query.message
    prodCat = ProdCatMethods(bot, msg, client, main_menu, botCmdObj)
    prodMan = ProdHandle(bot, msg, client, main_menu, cat_id, prodCat, botCmdObj)
    prodAttr = ProdAttrHandle(bot, msg, client, main_menu, prod_id, cat_id, prodMan, botCmdObj)
    await prodAttr.chooseOpt(attr_id)


@bot.on_callback_query(filters=filters.regex("next_attr_[0-9]+"))
async def show_next_attr(client, query):
    await query.message.delete()
    botCmdObj = BotCommand(bot, query.message)
    nxt_attr_id = query.data.split('_')[-1]
    if nxt_attr_id == "none":
        pass
    else:

        await getAttr(nxt_attr_id, botCmdObj)


@bot.on_callback_query(filters=filters.regex("prev_attr_[0-9]+"))
async def show_prev_attr(client, query):
    await query.message.delete()
    botCmdObj = BotCommand(bot, query.message)
    prev_attr_id = query.data.split('_')[-1]
    if prev_attr_id == "none":
        pass
    else:

        await getAttr(prev_attr_id, botCmdObj)


@bot.on_callback_query(filters=filters.regex("menu"))
async def go_menu(client, query):
    await query.message.delete()
    await main_menu(client, query.message)


@bot.on_callback_query(filters=filters.regex("attr_back_[0-9]+_[0-9]+"))
async def back_attr(client, query):
    await query.message.delete()
    botCmdObj = BotCommand(bot, query.message)
    prod_id = int(query.data.split("_")[-1])
    cat_id = int(query.data.split("_")[-2])
    prodCat = ProdCatMethods(bot, query.message, client, main_menu, botCmdObj)
    ProdMan = ProdHandle(bot, query.message, client, main_menu, cat_id, prodCat, botCmdObj)
    await ProdMan.chooseOpt(prod_id, cat_id)


@bot.on_callback_query(filters=filters.regex("manage_prop_[0-9]+_[0-9]+_[0-9]+"))
async def manage_prop(client, query):
    await query.message.delete()
    botCmdObj = BotCommand(bot, query.message)
    prod_id = int(query.data.split('_')[-1])
    cat_id = int(query.data.split('_')[-2])
    prop_id = int(query.data.split('_')[-3])
    msg = query.message
    prodCat = ProdCatMethods(bot, msg, client, main_menu, botCmdObj)
    prodMan = ProdHandle(bot, msg, client, main_menu, cat_id, prodCat, botCmdObj)
    prodProp = ProdPropHandle(bot, msg, client, main_menu, prod_id, cat_id, prodMan, botCmdObj)
    await prodProp.chooseOpt(prop_id)


@bot.on_callback_query(filters=filters.regex("next_prop_[0-9]+"))
async def show_next_prop(client, query):
    await query.message.delete()
    botCmdObj = BotCommand(bot, query.message)
    nxt_prop_id = query.data.split('_')[-1]
    if nxt_prop_id == "none":
        pass
    else:

        await getProp(nxt_prop_id, botCmdObj)


@bot.on_callback_query(filters=filters.regex("prev_prop_[0-9]+"))
async def show_prev_prop(client, query):
    await query.message.delete()
    botCmdObj = BotCommand(bot, query.message)
    prev_prop_id = query.data.split('_')[-1]
    if prev_prop_id == "none":
        pass
    else:
        await getProp(prev_prop_id, botCmdObj)


@bot.on_callback_query(filters=filters.regex("prop_back_[0-9]+_[0-9]+"))
async def back_prop(client, query):
    await query.message.delete()
    botCmdObj = BotCommand(bot, query.message)
    prod_id = int(query.data.split("_")[-1])
    cat_id = int(query.data.split("_")[-2])
    prodCat = ProdCatMethods(bot, query.message, client, main_menu, botCmdObj)
    ProdMan = ProdHandle(bot, query.message, client, main_menu, cat_id, prodCat, botCmdObj)
    await ProdMan.chooseOpt(prod_id, cat_id)


bot.run()
