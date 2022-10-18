from airtable import airtable
import pickle

at = airtable.Airtable('appW2upPBNl804iB1', 'keyqdwnX6NQUAqMyE')
events = at.get('events')
# print(events)

# open a file, where you ant to store the data
file = open('events.pickle', 'wb')
pickle.dump(events, file)
file.close()

