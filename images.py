<<<<<<< HEAD
<<<<<<< HEAD
from google_images_download import google_images_download  
import sys


response = google_images_download.googleimagesdownload()  
  
  
  
def get_images(query, limit): 
    orig_stdout = sys.stdout
    f = open('URLS.txt', 'w')
    sys.stdout = f
    arguments = {"keywords": query, 
                 "format": "jpg", 
                 "limit": limit, 
                 "print_urls":True, 
                 "size": "medium", 
                 "aspect_ratio": "panoramic"
                 } 
    try:     
        paths = response.download(arguments)

        sys.stdout = orig_stdout
        f.close()

        with open('URLS.txt') as f:
            content = f.readlines()
        f.close()

        urls = []
        for j in range(len(content)):
            if content[j][:9] == 'Completed':
                urls.append(content[j-1][11:-1])

        return urls
    
    except FileNotFoundError:  
        print('not found.....')

=======
=======
>>>>>>> origin/master
from google_images_download import google_images_download  
import sys


response = google_images_download.googleimagesdownload()  
  
  
  
def get_images(query, limit): 
    orig_stdout = sys.stdout
    f = open('URLS.txt', 'w')
    sys.stdout = f
    arguments = {"keywords": query, 
                 "format": "jpg", 
                 "limit": limit, 
                 "print_urls":True, 
                 "size": "medium", 
                 "aspect_ratio": "panoramic"
                 } 
    try:     
        paths = response.download(arguments)

        sys.stdout = orig_stdout
        f.close()

        with open('URLS.txt') as f:
            content = f.readlines()
        f.close()

        urls = []
        for j in range(len(content)):
            if content[j][:9] == 'Completed':
                urls.append(content[j-1][11:-1])

        return urls
    
    except FileNotFoundError:  
        print('not found.....')

<<<<<<< HEAD
>>>>>>> origin/master
=======
>>>>>>> origin/master
