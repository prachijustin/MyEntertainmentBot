<<<<<<< HEAD
<<<<<<< HEAD
import bandsintown
import requests
import json

BANDSINTOWN_API = '16e3347b-2e2f-4306-acf7-34833b29bbf7'


artist='nicki minaj'

url = 'https://rest.bandsintown.com/artists/' + artist + '/events?app_id=' + BANDSINTOWN_API
response = requests.get(url)
data = response.text
data = json.loads(data)
    #print(data)
new_dict = {item['id']:item for item in data}

print(len(new_dict))
=======
=======
>>>>>>> origin/master
import bandsintown
import requests
import json

BANDSINTOWN_API = '16e3347b-2e2f-4306-acf7-34833b29bbf7'


artist='nicki minaj'

url = 'https://rest.bandsintown.com/artists/' + artist + '/events?app_id=' + BANDSINTOWN_API
response = requests.get(url)
data = response.text
data = json.loads(data)
    #print(data)
new_dict = {item['id']:item for item in data}

print(len(new_dict))
<<<<<<< HEAD
>>>>>>> origin/master
=======
>>>>>>> origin/master
