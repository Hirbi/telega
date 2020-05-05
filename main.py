from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
import time as times


def echo(update, context):
    text = update.message.text
    update.message.reply_text(f'Я получил сообщение "{text}"')


def time(update, context):
    update.message.reply_text(times.asctime().split()[3])


def date(update, context):
    ans = ' '.join(times.asctime().split()[3]) + times.asctime().split()[-1]
    update.message.reply_text(ans)


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
