from youtube_downloader import download_playlist


# put playlist or video URLs into a list
playlist_URL = ['https://www.youtube.com/playlist?list=PLD63A284B7615313A']
video_URL = ['https://www.youtube.com/watch?v=9UblCd8uXCs&list=PLfNiIduhuYeAu-LI2VsdKOL_u3CVBciZG&index=7']
videos_URLs = ['https://www.youtube.com/watch?v=103xX7EMyKc&list=PLA-ADVxROXnAQoQ00eU1njgxuDW7TER1s&index=98',
               'https://www.youtube.com/watch?v=1Vw3Js66eOw']
mixed_URLs = ['https://www.youtube.com/watch?v=_Uz6zTUoKBU',
              'https://www.youtube.com/playlist?list=PL-tKrPVkKKE1Y_o_h2w85dzVdoX5t7SI0']

# set file extension and resolution
file_extension = 'mp4'
file_resolution = '720p'

# set numbering parameters for downloaded videos
video_number_start = 1
video_number_end = 18
video_number_digits = 2

# download
download_playlist(playlist_URL, file_extension, file_resolution, video_number_start, video_number_end, video_number_digits)
download_playlist(video_URL, file_extension, file_resolution, video_number_digits = 2)
download_playlist(videos_URLs, file_extension, file_resolution, video_number_digits = 2)
download_playlist(mixed_URLs, file_extension, file_resolution, video_number_digits = 2)