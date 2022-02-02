from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
from key import TOKEN


def main():
    updater = Updater(
        token=TOKEN,
        use_context=True
    )

    dispatcher = updater.dispatcher

    echo_handler = MessageHandler(Filters.all, do_echo)
    hello_handler = MessageHandler(Filters.text('привет'), say_hello)

    dispatcher.add_handler(hello_handler)
    dispatcher.add_handler(echo_handler)

    updater.start_polling()
    print('Бот успешно запустился')
    updater.idle()


def do_echo(update: Update, context: CallbackContext) -> None:
    name = update.message.from_user.first_name
    id = update.message.chat_id
    text = update.message.text
    update.message.reply_text(text=f'{text}')


def say_hello(update: Update, context: CallbackContext) -> None:
    name = update.message.from_user.first_name
    surname = update.message.from_user.last_name
    id = update.message.chat_id
    username = update.message.from_user.username
    text = update.message.text
    update.message.reply_text(text=f'Привет, {name} {surname}-@{username}\nid: {id}\n'
                                   'Приятно познакомится с живым человеком!)\n'
                                   'Я — бот.\n'
                                   'Умею показывать что ты написал.\n')


if __name__ == '__main__':
    main()
