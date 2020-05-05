from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler


def echo(update, context):
    update.message.reply_text(f'Я получил сообщение "{update.message.text}"')


def main():
    updater = Updater('1121846344:AAH6Xmry_2HfNc9i6YjxvSoBnMJbJ0jKeLo',
                      use_context=True)
    dp = updater.dispatcher
    text_handler = MessageHandler(Filters.text, echo)
    dp.add_handler(text_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()