from functions import *

starting_video_count = check_for_updates()

while True:
    new_video_count = check_for_updates()
    if new_video_count == starting_video_count:
        print(f'Still {starting_video_count} videos.')
    else:
        print(f'There are now {new_video_count} videos!')
        break
