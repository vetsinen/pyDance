import events_repository
import datetime
from init_bot import bot

def send_announce(announces='Hi'):
     # You can set parse_mode by default. HTML or MARKDOWN
    wild_dances_channel_id = -1001866935354
    social_dances_id = -1001287171602
    bot.send_message(wild_dances_channel_id, text=announces, parse_mode='HTML')

def render_events_to_tg_markup(events)->str:
    announces = ''
    for item in events:
        print(item['title'])

        announces += f'<em>{item["weekday"]}</em>, 💃{item["title"]}🕺, початок⏰ {item["startTime"]}, баланс🎸: <b>{item["balance"]}</b>, \n📍адреса {item["address"]}\n' \
                     f' {item["brief"]}\n вартість💰: <b>{item["price"]}</b>, '
        if item['link']:
            announces += f'👉<a href="{item["link"]}">link</a>'
        announces += '\n----------\n'
    return announces

if __name__ == '__main__':
    weekday = datetime.datetime.today().weekday()
    events = events_repository.fetch(f'w2>={weekday}')

    send_announce(render_events_to_tg_markup(events))

