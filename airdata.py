from random import randint
import events_repository
import datetime
from telebot import TeleBot, types
from operator import itemgetter

def shuffle(list):
    l = len(list)-1
    for i in range(1,2*l):
        i1 = randint(0, l)
        i2 = randint(0, l)
        list[i1], list[i2] = list[i2], list[i1]
    return list

def get_plain_events(raw_events):
    events = []
    for item in raw_events:
        if 'draft' not in item['fields']:
            events.append({
                "title": item['fields']['title'],
                "brief": item['fields']['brief'] if 'brief' in item['fields'] else 'опис недоступний',
                "balance": item['fields']['balance'],
                "startTime": item['fields']['startTime'],
                "weekday": item['fields']['weekday'],
                "w2": item['fields']['w2'],
                "price": item['fields']['price'],
                "link": item['fields']['link'] if "link" in item['fields'] else None,
                "address": item['fields']['address']
            })

    events = shuffle(events)
    events = sorted(events, key=itemgetter('w2'))
    return events


def send_announce(announces='Hi'):
    bot = TeleBot("5602757659:AAHmbDMWM4iVQ9RTu79inwC3cCBTKqS361Q",
                  parse_mode=None)  # You can set parse_mode by default. HTML or MARKDOWN
    wild_dances_channel_id = -1001866935354
    social_dances_id = -1001287171602
    bot.send_message(wild_dances_channel_id, text=announces, parse_mode='HTML')


if __name__ == '__main__':

    weekday = datetime.datetime.today().weekday()
    filter = f'w2>={weekday}'

    # events_repository.fetch_and_cache_data(filter)
    # raw_events = events_repository.take_events_from_cache()

    events = get_plain_events(events_repository.fetch(filter))

    # events['records'][]['fields'].keys()
    # odict_keys(['startDate', 'startTime', 'priority', 'description', 'link', 'title', 'Стили танца?', 'Attachments', 'price'])
    # for item in raw_events:
    #     print(item['fields']['title'])
    # print(item['fields'].keys())

    announces = ''

    for item in events:
        print(item['title'])

        announces += f'<em>{item["weekday"]}</em>, 💃{item["title"]}🕺, початок⏰ {item["startTime"]}, баланс🎸: <b>{item["balance"]}</b>, \n📍адреса {item["address"]}\n' \
                     f' {item["brief"]}\n вартість💰: <b>{item["price"]}</b>, '
        if item['link']:
            announces += f'👉<a href="{item["link"]}">link</a>'
        announces += '\n----------\n'

    send_announce(announces)
