from os import system
from googleapiclient.discovery import build
from secret_stuff import api_key
from time import sleep


def bash_command(user_input):
    _ = system(user_input)


def download_youtube_video(url):
    bash_command(f"cd Downloads/YouTubeDownloads/ && youtube-dl '{url}'")


def check_for_updates(channel_id):
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.search().list(
        part='id',
        channelId=channel_id,
        type='video',
        order='date',
        maxResults=1
    )

    response = request.execute()

    video_link_array = [f"https://www.youtube.com/watch?v={video['id']['videoId']}"
                        for video in response['items']]

    return video_link_array[0]


def check_channel(channel_name, channel_id, most_recent_url, new_vid):
    if not new_vid:
        new_vid_link = check_for_updates(channel_id)

        if new_vid_link == most_recent_url:
            sleep(300)
            return False
        else:
            print(f'New video from {channel_name}: {new_vid_link}')
            from secret_stuff import new_video_list
            new_video_list += new_vid_link
            return True
    else:
        sleep(300)
