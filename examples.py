from youtube_downloader import download_playlist


# put playlist or video urls into a list
playlist_url = ['https://www.youtube.com/playlist?list=PLD63A284B7615313A']
video_url = ['https://www.youtube.com/watch?v=qFZxTdjvl_w&list=PLDCsR2G1z9_u1kcZQ57x6iDW0fXpSn5EM&index=7']
videos_urls = ['https://www.youtube.com/watch?v=103xX7EMyKc&list=PLA-ADVxROXnAQoQ00eU1njgxuDW7TER1s&index=98',
               'https://www.youtube.com/watch?v=1Vw3Js66eOw']
mixed_urls = ['https://www.youtube.com/watch?v=_Uz6zTUoKBU',
              'https://www.youtube.com/playlist?list=PL-tKrPVkKKE1Y_o_h2w85dzVdoX5t7SI0']

# set file extension and resolution
file_extension = 'mp4'
file_resolution = '720p'

# set the range of videos you want to download from the list
video_number_start = 5
video_number_end = 7

# set number formatting for downloaded video files
video_number_digits = 2

# download
download_playlist(playlist_url, file_extension, file_resolution, video_number_start, video_number_end, video_number_digits)
download_playlist(video_url, file_extension, file_resolution, video_number_digits = 2)
download_playlist(videos_urls, file_extension, file_resolution, video_number_digits = 2)
download_playlist(mixed_urls, file_extension, file_resolution, video_number_digits = 2)