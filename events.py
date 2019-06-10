<<<<<<< HEAD
import ticketpy

tm_client = ticketpy.ApiClient('TB4mGiWrYIGhlnSZntuCOcARexeMzGem')


venues = tm_client.venues.find(keyword='music').all()
for v in venues:
    print(v)


# pages = tm_client.events.find(
#     state_code='London',
#     start_date_time='2017-05-19T20:00:00Z',
#     end_date_time='2017-05-21T20:00:00Z'
# )

# print(pages.event)

# for page in pages:
#     for event in page:
#         print(event)



# pages = tm_client.events.find(
#     classification_name='Hip-Hop',
#     state_code='GA',
#     start_date_time='2017-05-19T20:00:00Z',
#     end_date_time='2017-05-21T20:00:00Z'
# )

# print(pages)
# for page in pages:
#     for event in page:
#         print(event)

# import requests
# import json

# resp = requests.get('https://app.ticketmaster.com/discovery/v2/events.json?apikey=TB4mGiWrYIGhlnSZntuCOcARexeMzGem')

# data = resp.text

# print(data)


# print('esgwh')
# for event in pages:
=======
import ticketpy

tm_client = ticketpy.ApiClient('TB4mGiWrYIGhlnSZntuCOcARexeMzGem')


venues = tm_client.venues.find(keyword='music').all()
for v in venues:
    print(v)


# pages = tm_client.events.find(
#     state_code='London',
#     start_date_time='2017-05-19T20:00:00Z',
#     end_date_time='2017-05-21T20:00:00Z'
# )

# print(pages.event)

# for page in pages:
#     for event in page:
#         print(event)



# pages = tm_client.events.find(
#     classification_name='Hip-Hop',
#     state_code='GA',
#     start_date_time='2017-05-19T20:00:00Z',
#     end_date_time='2017-05-21T20:00:00Z'
# )

# print(pages)
# for page in pages:
#     for event in page:
#         print(event)

# import requests
# import json

# resp = requests.get('https://app.ticketmaster.com/discovery/v2/events.json?apikey=TB4mGiWrYIGhlnSZntuCOcARexeMzGem')

# data = resp.text

# print(data)


# print('esgwh')
# for event in pages:
>>>>>>> origin/master
#     print(event)