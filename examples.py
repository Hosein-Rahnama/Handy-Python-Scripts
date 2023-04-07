from youtube_downloader import *


# put playlist or video urls into a list
playlist_URL = ['https://www.youtube.com/playlist?list=PL-tKrPVkKKE1Y_o_h2w85dzVdoX5t7SI0']
video_URL = ['https://www.youtube.com/watch?v=m2zlSAsePNg&t=12s']
videos_URLs = ['https://www.youtube.com/watch?v=_Uz6zTUoKBU',
               'https://www.youtube.com/watch?v=5CoI3nIyxN8',
               'https://www.youtube.com/watch?v=yp6GwOX_axs',
               'https://www.youtube.com/watch?v=NVsefVUYLUM']
mixed_URLs = ['https://www.youtube.com/watch?v=_Uz6zTUoKBU',
              'https://www.youtube.com/playlist?list=PL-tKrPVkKKE1Y_o_h2w85dzVdoX5t7SI0']

# set file extension and resolution
file_extension = 'mp4'
file_resolution = '720p'

# set numbering parameters for downloaded videos
video_number_start = 1
video_number_end = 1
video_number_digits = 2

# download
download_playlist(playlist_URL, file_extension, file_resolution, video_number_start, video_number_end, video_number_digits)
download_playlist(video_URL, file_extension, file_resolution, video_number_digits = 2)
download_playlist(videos_URLs, file_extension, file_resolution, video_number_digits = 2)
download_playlist(mixed_URLs, file_extension, file_resolution, video_number_digits = 2)

