from init_bot import bot
import datetime
import pickle
import corean

logging_file = 'logging.pickle'

def loguser(message):
    with open("logging.pickle", 'wb') as f:
        pickle.dump(message, f)


@bot.message_handler(commands=['thisday', 'digest', "вечірки"])
def send_welcome(message):
    weekday = datetime.datetime.today().weekday()
    events = corean.fetch(f'w2={weekday}')
    announces = corean.render_events_to_tg_markup(events)
    bot.reply_to(message, announces, parse_mode='HTML')

@bot.message_handler(commands=['nextday'])
def send_welcome(message):
    weekday = datetime.datetime.today().weekday()
    events = corean.fetch(f'w2={weekday+1}')
    announces = corean.render_events_to_tg_markup(events)
    bot.reply_to(message, announces, parse_mode='HTML')


@bot.message_handler(commands=['weekdigest'])
def send_welcome(message):
    weekday = datetime.datetime.today().weekday()
    events = corean.fetch(f'w2>={weekday}')
    announces = corean.render_events_to_tg_markup(events)
    bot.reply_to(message, announces, parse_mode='HTML')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привіт, я бот танцювального дайджесту, я вмію показувати розклад вечірок"
                          "\nдля цього надішліть мені команду /thisday або /nextday", parse_mode='HTML')
    print((type(message)))
    print(str(message.from_user))


if __name__ == '__main__':
    bot.polling()
