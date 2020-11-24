from functions import *
from secret_stuff import *
from time import sleep

# To find Channel IDs, visit the following page:
# https://commentpicker.com/youtube-channel-id.php

bash_command('clear')
last_viewed_channel_1 = check_for_updates(channel_id_1)
last_viewed_channel_2 = check_for_updates(channel_id_2)
new_video_channel_1 = False
new_video_channel_2 = False


def check_channel(channel_num_int, most_recent_url):
    print(f'Last video viewed: {most_recent_url}')
    new_vid_check = check_for_updates(channel_id_1)

    if new_vid_check == most_recent_url:
        sleep(15)
    else:
        print(f'New video for Channel {channel_num_int}: {new_vid_check}')


while not new_video_channel_1 or not new_video_channel_2:
    if not new_video_channel_1 and not new_video_channel_2:
        check_channel(1, last_viewed_channel_1)
        check_channel(2, last_viewed_channel_2)
    elif not new_video_channel_1 and new_video_channel_2:
        check_channel(1, last_viewed_channel_1)
    elif new_video_channel_1 and not new_video_channel_2:
        check_channel(2, last_viewed_channel_2)
    else:
        print('All channels have posted new videos.')
