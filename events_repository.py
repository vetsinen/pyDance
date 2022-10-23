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

def fetch_and_cache_data(filter="w2>=0"):
    at = airtable.Airtable('appW2upPBNl804iB1', 'keyqdwnX6NQUAqMyE')
    events = at.get('events', filter_by_formula=filter)

    file = open(events_file, 'wb')
    pickle.dump(events, file)
    file.close()

def take_events_from_cache():
    file = open(events_file, 'rb')
    events = pickle.load(file)['records']
    file.close()
    return events

if __name__ == '__main__':
    pass
