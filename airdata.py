import events_repository
import datetime
from telebot import TeleBot, types

def send_announce(announces='Hi'):
    pass
    bot = TeleBot("5602757659:AAHmbDMWM4iVQ9RTu79inwC3cCBTKqS361Q",
                  parse_mode=None)  # You can set parse_mode by default. HTML or MARKDOWN
    wild_dances_channel_id =  -1001866935354
    social_dances_id = -1001287171602
    text = "Let's announce something"
    bot.send_message(wild_dances_channel_id, text=announces, parse_mode= 'HTML')

if __name__ == '__main__':

    weekday = datetime.datetime.today().weekday()
    filter = f'w2>={weekday}'

    # events_repository.fetch_and_cache_data()
    events = events_repository.take_events_from_cache()

    # events['records'][]['fields'].keys()
    # odict_keys(['startDate', 'startTime', 'priority', 'description', 'link', 'title', 'Стили танца?', 'Attachments', 'price'])

    announces = ''

    for item in events:
        # print(item['fields'].keys())
        print(item['fields']['title'], item['fields']['weekday'])
        title = item['fields']['title']
        description = item['fields']['description'] if 'description' in item['fields'] else 'немає повного опису'
        announces+= f'<b>{title}</b>\n {description}\n'


    print(announces)
    send_announce(announces)
