from youtube_downloader import *


# inputs

playlist_URL = 'https://www.youtube.com/playlist?list=PL-tKrPVkKKE1Y_o_h2w85dzVdoX5t7SI0'
video_URL = 'https://www.youtube.com/watch?v=m2zlSAsePNg&t=12s'
video_URLs = ['https://www.youtube.com/watch?v=_Uz6zTUoKBU',
              'https://www.youtube.com/watch?v=5CoI3nIyxN8',
              'https://www.youtube.com/watch?v=yp6GwOX_axs',
              'https://www.youtube.com/watch?v=NVsefVUYLUM']
file_extension = 'mp4'
file_resolution = '720p'
video_number_start = 7
video_number_end = 50
video_number_digits = 2


# download

download_video(YouTube(video_URL), file_extension, file_resolution, 3, video_number_digits)
download_playlist(Playlist(playlist_URL), file_extension, file_resolution, video_number_start, video_number_end, video_number_digits)
download_playlist(video_URLs, file_extension, file_resolution, video_number_digits = 2)
