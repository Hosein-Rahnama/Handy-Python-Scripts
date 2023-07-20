from youtube_downloader import download_playlist


# put playlist or video urls into a list
playlist_url = ['https://www.youtube.com/playlist?list=PLFOYXCPEqdNUsrH3_DTUArtOeo10eGkiq']
videos_urls = ['https://www.youtube.com/watch?v=-G1FuEQqxVI']
mixed_urls = ['https://www.youtube.com/watch?v=_Uz6zTUoKBU',
              'https://www.youtube.com/playlist?list=PL-tKrPVkKKE1Y_o_h2w85dzVdoX5t7SI0']

# set file extension and resolution
file_extension = 'mp4'
file_resolution = '720p'

# set the range of videos you want to download from the list
video_number_start = 1
video_number_end = 9

# download
download_playlist(playlist_url, file_extension, file_resolution, video_number_start, video_number_end)
download_playlist(videos_urls, file_extension, file_resolution, numbering_downloads = False)
download_playlist(mixed_urls, file_extension, file_resolution)