from functions import *
from secret_stuff import *

bash_command('clear')
last_viewed_channel_1 = check_for_updates(channel_1.id)
last_viewed_channel_2 = check_for_updates(channel_2.id)
last_viewed_channel_3 = check_for_updates(channel_3.id)

print(f"""The last videos posted:
{channel_1.name}: {last_viewed_channel_1}
{channel_2.name}: {last_viewed_channel_2}
{channel_3.name}: {last_viewed_channel_3}""")

while not channel_1.new_vid or not channel_2.new_vid or not channel_3.new_vid:
    check_channel(channel_1.name, channel_1.id, last_viewed_channel_1, channel_1.new_vid)
    check_channel(channel_2.name, channel_2.id, last_viewed_channel_2, channel_2.new_vid)
    check_channel(channel_3.name, channel_3.id, last_viewed_channel_3, channel_3.new_vid)

print('All YouTubers have new videos!')
downloaded = False

while not downloaded:
    download_request = input('Do you wish to download the new videos for later viewing? ').lower()

    if download_request == 'yes':
        for link in new_video_list:
            download_youtube_video(link)
            downloaded = True
    elif download_request == 'no':
        print('Have a nice day!')
        downloaded = True
    else:
        print(f'{download_request} is neither yes, nor no.  Please try again.')
