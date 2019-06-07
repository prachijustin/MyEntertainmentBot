import os
from pymongo import MongoClient
from wiki_to_python import load_wiki
from python_to_mongodb import load_python


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "client-secret.json"

import dialogflow_v2 as dialogflow
dialogflow_session_client = dialogflow.SessionsClient()

PROJECT_ID = 'entertainmentbot-uojwds'


client = MongoClient('mongodb+srv://Prachi:sharma@cluster0-sbg8n.mongodb.net/test?retryWrites=true&w=majority')
db = client.get_database('EntertainmentDB')
artist_record = db.ArtistData
event_record = db.EventsData




#print(artist_record.count_documents({}))

def ShowArtist(parameters):
    name = parameters.get('music-artist')
    record = artist_record.find_one({'name': name})
    return record


def ShowArtistEvents(parameters):
    #event = parameters.get('entertainment_type')
    artist = parameters.get('music-artist')
    record = event_record.find({'artist': artist}).limit(3)
    return record


def detect_intent_from_text(text, session_id, language_code='en'):
    session = dialogflow_session_client.session_path(PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = dialogflow_session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result


def fetch_reply(message, session_id):
    response = detect_intent_from_text(message, session_id)
    if response.intent.display_name == 'ShowArtist':
        records = ShowArtist(dict(response.parameters))
        records = str(records)
        NA = str(None)
        if records == NA:          
            name = response.parameters['music-artist']
            print('name........', name)
            load_python(name)
            print('done......')
            records = ShowArtist(dict(response.parameters))
            records = str(records)

        final_record = 'showing record: ' + records    
        return final_record

        
    elif response.intent.display_name == 'ShowEvents':
        records = ShowArtistEvents(dict(response.parameters))
        print(type(records))
        #records = str(records)
        #return records
        #erecord = {item[0]:item for item in records}
        #print(type(erecord))
        event_record = 'Showing events of ' 
        # for i in range(0,3):
        #     print(records[i])
        for row in records: 
            event_record += row['artist'] + ' :'
            event_record += '\n\nVenue: {}\nCountry: {}\nDate: {}\nTicket URL: {}'.format(row['venue'], row['country'], row['date'], row['tix_url'])
            #event_record = 'Venue: ' + row['venue'] + 'Country: ' + row['country'] + 'Date: ' + row['date'] + ' Ticket URL: ' + row['tix_url']
        print(event_record)
            #frecords += event_record
            #event_record += '\n\n{}'.format(row['id'])
        return event_record

    if response.intent.display_name == 'ShowNews':
        return 'ok i will show u news *{}*'.format(dict(response.parameters))
    else:
        return response.fulfillment_text

