from telegram.ext import (
    Updater,
    CallbackQueryHandler,
    ChosenInlineResultHandler,
    InlineQueryHandler,
    Handler,
)
import logging
from uuid import uuid4
from telegram import InlineQueryResultGame
import sys
from decouple import config


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = config("TOKEN")
LOCAL_URL = config("LOCAL_URL", "127.0.0.1")
APP_URL = config("APP_URL", "")
PORT = config("PORT", 5000)
GAME_URL = config("GAME_URL", "")


def game(update, context):
    imid = update.callback_query.inline_message_id
    uid = update.callback_query.from_user.id
    update.callback_query.answer(url=f"{GAME_URL}?i={imid}&u={uid}")


def inline(update, context):
    print("hello")
    print(update.to_json())


def hand(update, context):
    print(update.to_json)


def show(update, context):
    idd = str(uuid4())
    print(idd)
    game = InlineQueryResultGame(idd, "Binod")
    x = update.inline_query.answer([game])
    print(x)


def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CallbackQueryHandler(game))
    dispatcher.add_handler(ChosenInlineResultHandler(inline))
    dispatcher.add_handler(InlineQueryHandler(show))
    if len(sys.argv) > 1 and sys.argv[1] == "-p":
        updater.start_polling()
    else:
        updater.start_webhook(webhook_url=LOCAL_URL, url_path=TOKEN)
        updater.bot.setWebhook(APP_URL + TOKEN)


if __name__ == "__main__":
    main()
