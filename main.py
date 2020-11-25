from functions import *
from secret_stuff import *

# To find Channel IDs, visit the following page:
# https://commentpicker.com/youtube-channel-id.php

bash_command('clear')
last_viewed_channel_1 = check_for_updates(channel_1.id)
last_viewed_channel_2 = check_for_updates(channel_2.id)

print(f"""The last videos posted:
{channel_1.name}: {last_viewed_channel_1}
{channel_2.name}: {last_viewed_channel_2}""")

while not channel_1.new_vid or not channel_2.new_vid:
    if not channel_1.new_vid and not channel_2.new_vid:
        channel_1.new_vid = check_channel(channel_1.name, channel_1.id, last_viewed_channel_1, False)
        channel_2.new_vid = check_channel(channel_2.name, channel_2.id, last_viewed_channel_2, False)
    elif not channel_1.new_vid and channel_2.new_vid:
        channel_1.new_vid = check_channel(channel_1.name, channel_1.id, last_viewed_channel_1, False)
    elif channel_1.new_vid and not channel_2.new_vid:
        channel_2.new_vid = check_channel(channel_2.name, channel_2.id, last_viewed_channel_2, False)
    else:
        print('All YouTubers have new videos!')
