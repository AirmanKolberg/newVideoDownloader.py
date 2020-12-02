# newVideoDownloader.py
I used to download YouTube videos with YouTube Premium to watch them offline, however, I am no longer, 
after many years, a YouTube Premium member.  So, I decided to write a little Python program that checks 
some of my favourite YouTubers' channels for new videos, and when a new video is posted, it is then 
downloaded in the highest quality to be viewed!  I still have a long ways to go, as I've just started
this project, and it is my first project to ever incorporate an API.  Enjoy, I'll update as I go!

If, for any reason, you would like to donate- though unneccesary, is always apreciated!

BitCoin: 3Gj49JGVPXjw3994bSebQNrHsFJkZE9iRg && Etherium: 0x08b57537943BBb6A527C9c861E9550D9Be9f7729

Thank you all for reading!

# Update, 26Nov2020
It became apparent to me a couple of days ago that Google limits your requests with their YouTube API.
You know, as if Google, the giant monopoly that does evil, despite their "do no evil" propaganda,
couldn't afford to not limit requests for the few handful of people, probably millions at most, use
their API on a daily basis.  So, I've increased the amount of wait time between video searches from
10min to 15min in the file containing most of the functions.

# Update 1Dec2020
I've just been editing around the time delay between inquiries.  5min seems reasonable to me, based
on the number of daily requests this API limits.  However, this would also heavily depend on the
number of channels you had the program checking, but still.  Just a minor update.
