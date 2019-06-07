from flask import Flask, render_template, request
from wikipedia import * 

app = Flask(__name__)



def load_wiki(artist=''):
    if artist == '':
        artist = 'Justin Bieber'

    print('artist.......', artist)
    wiki_page = page(artist)

    try:
        artist_name = wiki_page.title
        artist_bio = wiki_page.summary
        artist_pic = wiki_page.images[0]
    except exceptions as e:
        artist_bio = e.options

    return artist_name, artist_bio, artist_pic



