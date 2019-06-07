import bandsintown
import requests
import json
from pymongo import MongoClient

BANDSINTOWN_API = '16e3347b-2e2f-4306-acf7-34833b29bbf7'

client = MongoClient('mongodb+srv://Prachi:sharma@cluster0-sbg8n.mongodb.net/test?retryWrites=true&w=majority')
db = client.get_database('EntertainmentDB')
event_record = db.EventsData

def get_artist_events(artist):
    url = 'https://rest.bandsintown.com/artists/' + artist + '/events?app_id=' + BANDSINTOWN_API
    response = requests.get(url)
    data = response.text
    data = json.loads(data)
    new_dict = {item['id']:item for item in data}
    
    for index in new_dict:
        #print('venue: ',new_dict[index]['venue']['name'], new_dict[index]['venue']['country'],new_dict[index]['datetime'])
        try:
            event_dict = {
                'artist': artist,
                'venue': new_dict[index]['venue']['name'],
                'country': new_dict[index]['venue']['country'],
                'date': new_dict[index]['datetime'],
                'tix_url': new_dict[index]['offers'][0]['url'],
            }
            event_record.insert_one(event_dict)
        except:
            print('exception......')
    print('success')

get_artist_events('Maroon 5')