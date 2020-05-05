from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
import time as times


def time(update, context):
    update.message.reply_text(times.asctime().split()[3])


def date(update, context):
    ans = ' '.join(times.asctime().split()[:3]) + " " + times.asctime().split()[-1]
    update.message.reply_text(ans)


def task(context):
    job = context.job
    context.bot.send_message(job.context, text='Вернулся')


def set_timer(update, context):
    chat_id = update.message.chat_id
    try:
        due = (context.args[0])
        if due < 0:
            update.message.reply_text('Прошлое не круто')
            return
        if 'job' in context.chat_data:
            old_job = context.chat_data['job']
            old_job.shedule_removal()
        new_job = context.job_queue.run_once(task, due, context=chat_id)
        context.chat_data['job'] = new_job
        update.message.reply_text(f'Вернусь через {due} секунд')
    except (IndexError, ValueError):
        update.message.reply_text('Глупышка')

def echo(update, context):
    text = update.message.text
    update.message.reply_text(f'Я получил сообщение "{text}"')


def main():
    updater = Updater('1121846344:AAH6Xmry_2HfNc9i6YjxvSoBnMJbJ0jKeLo',
                      use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("date", date))
    dp.add_handler(CommandHandler("time", time))
    text_handler = MessageHandler(Filters.text, echo)
    dp.add_handler(text_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
