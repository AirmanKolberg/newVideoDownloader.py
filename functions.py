from os import system
from googleapiclient.discovery import build
from secret_stuff import api_key


def bash_command(user_input):
    _ = system(user_input)


def download_youtube_video(url):
    bash_command(f"youtube-dl '{url}'")


def check_for_updates():
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.channels().list(
        part='statistics',
        forUsername='INSERT YOUTUBER USERNAME HERE'
    )

    response = request.execute()
    bash_command('rm test_file.py')
    bash_command(f"""echo 'yt_data = "{response}"' >> test_file.py""")

    from test_file import yt_data
    string_data = str(yt_data)
    video_count = int(string_data[-8:-4])
    return video_count
