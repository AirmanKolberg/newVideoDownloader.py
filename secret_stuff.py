# This file is just to show the basics of how I set up
# the 'secret_stuff.py' file.

api_key = 'INSERT API KEY'

class Channel:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.new_vid = False

    def found_new_video(self):
        self.new_vid = True


channel_1 = Channel('Channel 1 Name', 'YouTubeID')
channel_2 = Channel('Channel 2 Name', 'YouTubeID')
