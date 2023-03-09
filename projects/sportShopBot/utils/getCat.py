from api.sendReq import makeApiCall

from urls.mkUrl import prepareUrl

from botCommands.BotCommand import BotCommand


async def prGetText(cat):
    intro = "Category"
    title = "Title" + "\n" + cat['title']
    description = "Description" + "\n" + cat['description']

    parent = "Category" + "\n"
    if cat['parent'] is not None:
        parent += cat['parent']['title']
    else:
        parent += "-"

    children = "Sub categories" + "\n"
    if cat['childCats'] is not None:
        children += " و ".join([x['title'] for x in cat['childCats']])
    else:
        children += "-"

    txt = intro + "\n\n" + title + "\n\n" + description + "\n\n" + parent + "\n\n" + children + "\n\n"

    return txt


async def getCat(cat_id: int, botCmdObj: BotCommand):
    url = prepareUrl("get or delete or edit cat", [cat_id])

    response = await makeApiCall(url, 'get')

    cat = response['cat']
    txt = await prGetText(cat)

    next_id = cat['next_id']
    if next_id is None:
        next_id = 'none'

    prev_id = cat['prev_id']
    if prev_id is None:
        prev_id = 'none'

    await botCmdObj.sendMsg(txt, "get cat", [cat_id, next_id, prev_id])
