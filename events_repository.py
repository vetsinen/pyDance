from airtable import airtable
import pickle
events_file = 'events.pickle'

def fetch(filter="w2>=0"):
    at = airtable.Airtable('appW2upPBNl804iB1', 'keyqdwnX6NQUAqMyE')
    return at.get('events',filter_by_formula=filter)['records']

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
