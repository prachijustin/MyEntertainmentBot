import requests
from pymongo import MongoClient
from wiki_to_python import load_wiki

client = MongoClient('mongodb+srv://Prachi:sharma@cluster0-sbg8n.mongodb.net/test?retryWrites=true&w=majority')
db = client.get_database('EntertainmentDB')
artist_record = db.ArtistData


def load_python(artist):
    name, bio, pic = load_wiki(artist)
    bio = bio[:20]
    artist_dict = {
        'name': name,
        'age': 0,
        'desc': 'NA',
        'bio': bio,
        'pics': pic,
        'social_acc': 'social',
        'news': 'nnnn'
    }
    artist_record.insert_one(artist_dict)
    print('successfull')

