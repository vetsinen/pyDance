from init_bot import bot
import datetime
import events_repository
from announces import render_events_to_tg_markup

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
    weekday = datetime.datetime.today().weekday()
    events = events_repository.fetch(f'w2={weekday}')
    announces = render_events_to_tg_markup(events)
    bot.reply_to(message,announces,parse_mode='HTML')

if __name__ == '__main__':
    bot.polling()



