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

    # events_repository.fetch_and_cache_data(filter)
    raw_events = events_repository.take_events_from_cache()

    # raw_events = events_repository.fetch(filter)

    # events['records'][]['fields'].keys()
    # odict_keys(['startDate', 'startTime', 'priority', 'description', 'link', 'title', 'Стили танца?', 'Attachments', 'price'])
    # for item in raw_events:
    #     print(item['fields']['title'])
    # print(item['fields'].keys())


    announces = ''
    events = []
    for item in raw_events:
            if 'draft' not in item['fields']:
                events.append({
                    "title": item['fields']['title'],
                    "description": item['fields']['description'] if 'description' in item['fields'] else 'опис недоступний',
                    "balance" : item['fields']['balance'],
                    "startTime" : item['fields']['startTime'],
                    "weekday": item['fields']['weekday'],
                    "w2" : item['fields']['w2'],
                    "price": item['fields']['price'],
                    "link" : item['fields']['link'] if "link" in item['fields'] else None,
                    "address" : item['fields']['address']
                })

    for item in events:
        print(item['title'])

        announces+= f'{item["weekday"]} <b>{item["title"]} початок: {item["startTime"]}</b> \n {item["description"]} '
        if item['link']:
            announces+=f'<a href="{item["link"]}">link</a>'
        announces+='\n----------\n'

    # send_announce(announces)
