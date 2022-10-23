from init_bot import bot
import datetime
import events_repository
import pickle
logging_file = 'logging.pickle'
from announces import render_events_to_tg_markup

def loguser(message):
    with open("logging.pickle", 'wb') as f:
        pickle.dump(message, f)

@bot.message_handler(commands=['parties', 'digest',"вечірки"])
def send_welcome(message):
    print(str(message.from_user))
    weekday = datetime.datetime.today().weekday()
    events = events_repository.fetch(f'w2={weekday}')
    announces = render_events_to_tg_markup(events)
    bot.reply_to(message,announces,parse_mode='HTML')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привіт, я бот танцювального дайджесту, я вмію показувати вечірки на день"
                          "\nдля цього надішліть мені команду /digest",parse_mode='HTML')
    print((type(message)))
    print(str(message.from_user))

if __name__ == '__main__':
    bot.polling()



