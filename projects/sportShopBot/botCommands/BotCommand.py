from pyromod import listen
from pyrogram.types import (ReplyKeyboardMarkup,
                            InlineKeyboardMarkup,
                            InlineKeyboardButton)


class BotCommand:

    def __init__(self, bot, msg):

        self.bot = bot
        self.msg = msg

    async def prepRepMarkTxt(self, ttl, options=None):

        if ttl == "choose":
            return "choose the command"

        elif ttl == "conf cat del":
            return "Confirm?"

        elif ttl == "up img":
            return "Upload the image:"

        elif ttl == "mk inpt":

            post = options[0]
            label = options[1]
            optional = options[2]

            if post is False:
                text = f"Enter new {label}(If you don`t want to change the {label} enter -1)"
            else:
                text = f'Enter the {label}'

            if optional is True:
                text += "If you want to set it to empty enter -2"

            return text

        elif ttl == "del img":
            return "Enter the picture`s number to delete that picture."

    async def prepCatMainRepMark(self):

        reply_markup = ReplyKeyboardMarkup([
            ['Display the categories list'],
            ['Add new category']
        ],
            one_time_keyboard=True,
            resize_keyboard=True
        )

        return reply_markup

    async def prepCatManRepMark(self):

        reply_markup = ReplyKeyboardMarkup([
            ['Add new category'],
            ['Display the categories` list'],
            ['Add product to category'],
            ['Delete category', 'Edit category'],
            ['Delete parent category', 'Add parent category'],
            ['Return', 'Main menu']
        ],
            one_time_keyboard=True,
            resize_keyboard=True
        )

        return reply_markup

    async def prepConfDelCatRepMark(self):

        reply_markup = ReplyKeyboardMarkup([
            ['Confirm'],
            ['Return', 'Main menu']
        ],
            one_time_keyboard=True,
            resize_keyboard=True
        )

        return reply_markup

    async def prepProdManRepMark(self):

        reply_markup = ReplyKeyboardMarkup([
            ['Delete product', 'Edit product'],
            ['Confirm to upload in Instagram'],
            ['Display products` descriptions', 'Add product`s description'],
            ['Display products` attributes', 'Add product`s attribute'],
            ['Display products` images', 'Add product`s image'],
            ['Return', 'Main menu']
        ],
            one_time_keyboard=True,
            resize_keyboard=True
        )

        return reply_markup

    async def prepProdAttrManRepMark(self):

        reply_markup = ReplyKeyboardMarkup([
            ['Add description', 'edit description'],
            ['Display descriptions` list', 'Delete description'],
            ['Return', 'Main menu']
        ],
            one_time_keyboard=True,
            resize_keyboard=True
        )

        return reply_markup

    async def prepReturnRepMark(self):

        reply_markup = ReplyKeyboardMarkup([
            ['Return', 'Main menu']
        ],
            one_time_keyboard=True,
            resize_keyboard=True
        )

        return reply_markup

    async def prepProdPropManRepMark(self):

        reply_markup = ReplyKeyboardMarkup([
            ['Add attribute', 'Edit attribute'],
            ['Display attributes` list', 'Delete attribute'],
            ['Return', 'Main menu']
        ],
            one_time_keyboard=True,
            resize_keyboard=True
        )

        return reply_markup

    async def prepGetProdAttrInMark(self, ids):

        attr_id = ids[0]
        cat_id = ids[1]
        prod_id = ids[2]
        next_id = ids[3]
        prev_id = ids[4]

        reply_markup = InlineKeyboardMarkup([

            [InlineKeyboardButton(
                "Manage description",
                callback_data="manage_attr_{}_{}_{}".format(attr_id,
                                                            cat_id,
                                                            prod_id)
            )],
            [
                InlineKeyboardButton(
                    "Next",
                    callback_data="next_attr_{}".format(next_id)
                ),
                InlineKeyboardButton(
                    "Previous",
                    callback_data="prev_attr_{}".format(prev_id)
                )
            ],
            [InlineKeyboardButton(
                "Return",
                callback_data="attr_back_{}_{}".format(cat_id,
                                                       prod_id)
            ),
                InlineKeyboardButton(
                    "Main menu",
                    callback_data="menu"
                )]
        ])

        return reply_markup

    async def prepGetCatInMark(self, ids):

        cat_id = ids[0]
        next_id = ids[1]
        prev_id = ids[2]

        reply_markup = InlineKeyboardMarkup([

            [InlineKeyboardButton(
                "Manage group",
                callback_data="manage_cat_{}".format(cat_id)
            )],
            [InlineKeyboardButton(
                "Next",
                callback_data="next_cat_{}".format(next_id)
            ),
                InlineKeyboardButton(
                    "Previous",
                    callback_data="prev_cat_{}".format(prev_id)
                )],

            [InlineKeyboardButton(
                "Main menu",
                callback_data="menu"
            )
            ]
        ]
        )

        return reply_markup

    async def prepGetCatParInMark(self, ids):

        cat_id = ids[0]
        par_id = ids[1]
        next_id = ids[2]
        prev_id = ids[3]

        reply_markup = InlineKeyboardMarkup([

            [InlineKeyboardButton(
                "Mark as parent category",
                callback_data="cat_par_{}_{}".format(cat_id, par_id)
            )],
            [InlineKeyboardButton(
                "Next",
                callback_data="next_cat_par_{}_{}".format(next_id,
                                                          cat_id)
            ),
                InlineKeyboardButton(
                    "Previous",
                    callback_data="prev_cat_par_{}_{}".format(prev_id,
                                                              cat_id)
                )],

            [InlineKeyboardButton(
                "Main menu",
                callback_data="menu"
            )
            ]
        ]
        )

        return reply_markup

    async def prepGetProdInMark(self, ids):

        cat_id = ids[0]
        prod_id = ids[1]
        next_id = ids[2]
        prev_id = ids[3]

        reply_markup = InlineKeyboardMarkup([

            [InlineKeyboardButton(
                "Manage product",
                callback_data="manage_prod_{}_{}".format(cat_id,
                                                         prod_id)
            )],
            [
                InlineKeyboardButton(
                    "Next",
                    callback_data="next_prod_{}".format(next_id)
                ),
                InlineKeyboardButton(
                    "Previous",
                    callback_data="prev_prod_{}".format(prev_id)
                )
            ],
            [InlineKeyboardButton(
                "Return",
                callback_data="prod_back_{}".format(cat_id)
            ),
                InlineKeyboardButton(
                    "Main menu",
                    callback_data="menu"
                )]
        ]
        )

        return reply_markup

    async def prepGetProdPropInMark(self, ids):

        prop_id = ids[0]
        cat_id = ids[1]
        prod_id = ids[2]
        next_id = ids[3]
        prev_id = ids[4]

        reply_markup = InlineKeyboardMarkup([

            [InlineKeyboardButton(
                "Manage attribute",
                callback_data="manage_prop_{}_{}_{}".format(prop_id,
                                                            cat_id,
                                                            prod_id)
            )],
            [
                InlineKeyboardButton(
                    "Next",
                    callback_data="next_prop_{}".format(next_id)
                ),
                InlineKeyboardButton(
                    "Previous",
                    callback_data="prev_prop_{}".format(prev_id)
                )
            ],
            [InlineKeyboardButton(
                "Return",
                callback_data="prop_back_{}_{}".format(cat_id,
                                                       prod_id)
            ),
                InlineKeyboardButton(
                    "Main menu",
                    callback_data="menu"
                )]
        ]
        )

        return reply_markup

    async def sendMsg(self, text, ttl=None, ids=None):

        reply_markup = None

        if ttl is not None:
            if ttl == "get attr":
                reply_markup = await self.prepGetProdAttrInMark(ids)

            elif ttl == "get cat":
                reply_markup = await self.prepGetCatInMark(ids)

            elif ttl == "get cat par":
                reply_markup = await self.prepGetCatParInMark(ids)

            elif ttl == "get prod":
                reply_markup = await self.prepGetProdInMark(ids)

            elif ttl == "get prop":
                reply_markup = await self.prepGetProdPropInMark(ids)

        await self.bot.send_message(self.msg.chat.id,
                                    text=text,
                                    reply_markup=reply_markup)

    async def askUser(self, ttl, img=False, options=None):

        if ttl == "cat main":
            reply_markup = await self.prepCatMainRepMark()
            text = await self.prepRepMarkTxt("choose")

        elif ttl == "cat manage":
            reply_markup = await self.prepCatManRepMark()
            text = await self.prepRepMarkTxt("choose")

        elif ttl == "conf cat del":
            reply_markup = await self.prepConfDelCatRepMark()
            text = await self.prepRepMarkTxt("conf cat del")

        elif ttl == "prod manage":
            reply_markup = await self.prepProdManRepMark()
            text = await self.prepRepMarkTxt("choose")

        elif ttl == "attr manage":
            reply_markup = await self.prepProdAttrManRepMark()
            text = await self.prepRepMarkTxt("choose")

        elif ttl == "img manage":
            reply_markup = await self.prepReturnRepMark()
            text = await self.prepRepMarkTxt("up img")

        elif ttl == "prop manage":
            reply_markup = await self.prepProdPropManRepMark()
            text = await self.prepRepMarkTxt("choose")

        elif ttl == "mk inpt":
            reply_markup = await self.prepReturnRepMark()
            text = await self.prepRepMarkTxt("mk inpt", options)

        elif ttl == "del img":
            reply_markup = await self.prepReturnRepMark()
            text = await self.prepRepMarkTxt("del img")

        input = await self.bot.ask(self.msg.chat.id,
                                   text,
                                   reply_markup=reply_markup)
        if img is True:
            return input

        return input.text

    async def sendPhoto(self, photo, caption):

        await self.bot.send_photo(chat_id=self.msg.chat.id,
                                  photo=photo,
                                  caption=caption)
