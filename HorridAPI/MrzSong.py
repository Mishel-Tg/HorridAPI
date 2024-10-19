# (c) @HORRIDduo

import requests

class Songmrz:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://horridapi.onrender.com/song"

    def download(self, song_name):
        response = requests.post(f"{self.base_url}?api_key={self.api_key}&query={song_name}")
        data = response.json()
        
        # Create an object to hold the song details
        song_details = {
            'duration': data['duration'],
            'link': data['link'],
            'thumb': data['thumb'],
            'title': data['title'],
            'url': data['url']
        }                
        return SongObject(song_details)

class SongObject:
    def __init__(self, details):
        self.duration = details['duration']
        self.link = details['link']
        self.thumb = details['thumb']
        self.title = details['title']
        self.url = details['url']
