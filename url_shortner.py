<<<<<<< HEAD
import pyshorteners
from pyshorteners import Shorteners

def shorten(url):
    s = pyshorteners.Shortener(Shorteners.TINYURL)
    shorturl = s.short(url)
    return shorturl


=======
import pyshorteners
from pyshorteners import Shorteners

def shorten(url):
    s = pyshorteners.Shortener(Shorteners.TINYURL)
    shorturl = s.short(url)
    return shorturl


>>>>>>> origin/master
