import datetime
from init_bot import bot

from airtable import airtable
import pickle
events_file = 'events.pickle'
from random import randint
from operator import itemgetter


def shuffle(list):
    l = len(list)-1
    for i in range(1,2*l):
        i1 = randint(0, l)
        i2 = randint(0, l)
        list[i1], list[i2] = list[i2], list[i1]
    return list


    # events['records'][]['fields'].keys()
    # odict_keys(['startDate', 'startTime', 'priority', 'description', 'link', 'title', 'Стили танца?', 'Attachments', 'price'])
    # for item in raw_events:
    #     print(item['fields']['title'])
    # print(item['fields'].keys())
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

def fetch(filter="w2>=0"):
    at = airtable.Airtable('appW2upPBNl804iB1', 'keyqdwnX6NQUAqMyE')
    raw_events =  at.get('events',filter_by_formula=filter)['records']
    return get_plain_events(raw_events)

def send_announce(announces='Hi'):
     # You can set parse_mode by default. HTML or MARKDOWN
    wild_dances_channel_id = -1001866935354
    social_dances_id = -1001287171602
    bot.send_message(social_dances_id, text=announces, parse_mode='HTML')

def render_events_to_tg_markup(events)->str:
    announces = ''
    for item in events:
        print(item['title'])

        announces += f'<em>{item["weekday"]}</em>, 💃{item["title"]}🕺, початок⏰ {item["startTime"]}, баланс🎸: <b>{item["balance"]}</b>, \n📍адреса {item["address"]}\n' \
                     f' {item["brief"]}\n вартість💰: <b>{item["price"]}</b>, '
        if item['link']:
            announces += f'👉<a href="{item["link"]}">link</a>'
        announces += '\n----------\n'
    announces+= '\n детальніша інформація про вечірки є на сайті https://opendance.life/' \
                '\n якщо якоїсь вечірки немає в списку, ви можете самостійно додати її до бази, ' \
                'після модерації вона з"явиться' \
                ' в загальному списку 👉<a href="https://airtable.com/shrMtHafY9TwmoTdZ">додати вечірку</a>'
    return announces

if __name__ == '__main__':
    weekday = datetime.datetime.today().weekday()
    events = fetch(f'w2>={weekday}')
    send_announce(render_events_to_tg_markup(events))

