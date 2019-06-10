<<<<<<< HEAD
from flask import Flask, render_template, request
from wikipedia import * 
from url_shortner import shorten

app = Flask(__name__)



def load_wiki(artist=''):
    if artist == '':
        artist = 'Justin Bieber'

    print('artist.......', artist)
    wiki_page = page(artist)

    try:
        artist_name = wiki_page.title
        artist_bio = wiki_page.summary
    except exceptions as e:
        artist_bio = e.options

    return artist_name, artist_bio



=======
from flask import Flask, render_template, request
from wikipedia import * 
from url_shortner import shorten

app = Flask(__name__)



def load_wiki(artist=''):
    if artist == '':
        artist = 'Justin Bieber'

    print('artist.......', artist)
    wiki_page = page(artist)

    try:
        artist_name = wiki_page.title
        artist_bio = wiki_page.summary
    except exceptions as e:
        artist_bio = e.options

    return artist_name, artist_bio



>>>>>>> origin/master
