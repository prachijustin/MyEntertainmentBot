import requests
from pymongo import MongoClient
from wiki_to_python import load_wiki
from images import get_images

client = MongoClient('mongodb+srv://Prachi:sharma@cluster0-sbg8n.mongodb.net/test?retryWrites=true&w=majority')
db = client.get_database('EntertainmentDB')
artist_record = db.ArtistData
x =db.Books


def load_python(artist):
    name, bio = load_wiki(artist)
    bio = bio.split('.', maxsplit=1)[0]
    url = get_images(artist, 1)
    pic_url = ''.join(url)
    artist_dict = {
        'name': name,
        'bio': bio,
        'pics': pic_url,
        'social_acc': 'social',
    }
    artist_record.insert_one(artist_dict)
    print('successfull')

