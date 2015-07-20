#!/usr/bin/python
# vim: set fileencoding=utf-8 :
import urllib
import urllib.request
import json, io
import sys

def get_poster_url(name, year):
    name = name.replace(' ', '+')
    url = "http://www.omdbapi.com/?t=%s&y=%s&plot=short&r=json" % (name, year)
    print(url)
    urlopen = urllib.request.urlopen(url)
    content = urlopen.read().decode("utf-8")
    parsed = json.load(io.StringIO(content))
    return parsed["Poster"]

def download_poster(name, year):
    url = get_poster_url(name, year)
    ext = "jpg" # TODO: get extension from url 
    urllib.request.urlretrieve(url, "%s %s.%s" %(name, year, ext))

filename = sys.argv[1]
with open(filename, "r") as infile:
    for line in infile:
        (name, year) = line.split(";")
        year = year.strip()
        if name != "" and year != "":
            download_poster(name, year)
