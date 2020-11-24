from os import system
from googleapiclient.discovery import build
from secret_stuff import api_key


def bash_command(user_input):
    _ = system(user_input)


def download_youtube_video(url):
    bash_command(f"youtube-dl '{url}'")


def check_for_updates(channel_id):
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.search().list(
        part='id',
        channelId=channel_id,
        type='video',
        order='date',
        maxResults=3
    )

    response = request.execute()

    video_link_array = [f"https://www.youtube.com/watch?v={video['id']['videoId']}" \
                        for video in response['items']]

    return video_link_array[0]
