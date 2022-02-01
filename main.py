from telegram.ext import Updater, MessageHandler, Filters
from key import TOKEN


def main():
    updater = Updater(
        token=TOKEN,
        use_context=True
    )

    dispatcher = updater.dispatcher

    echo_handler = MessageHandler(Filters.all, do_echo)

    dispatcher.add_handler(echo_handler)

    updater.start_polling()
    updater.idle()


def do_echo(update, context):
    name = update.message.from_user.first_name
    text = update.message.text
    update.message.reply_text(text=f'Привет, {name}!\nТы написал "{text}"')


if __name__ == '__main__':
    main()
