import pickle

file = open('events.pickle', 'rb')
events = pickle.load(file)['records']
file.close()
# events['records'][]['fields'].keys()
# odict_keys(['startDate', 'startTime', 'priority', 'description', 'link', 'title', 'Стили танца?', 'Attachments', 'price'])

for item in events:
    print(item['fields'].keys())
    print(item['fields']['title'])
    # print(item['fields']['styles'])


# iterating over the ordereddict
# for key, value in events.items():
#     print(type(key), type(value)) #<class 'str'> <class 'list'>
