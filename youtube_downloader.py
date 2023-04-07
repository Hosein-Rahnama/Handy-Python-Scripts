from pytube import YouTube, Playlist
from http.client import IncompleteRead
from typing import List, Optional


def download_playlist(videos_URLs: List[str],
                      file_extension: str, 
                      file_resolution: str, 
                      video_number_start: Optional[int] = None, 
                      video_number_end: Optional[int] = None, 
                      video_number_digits: int = 2) -> None:
    video_list = []
    for URL in videos_URLs:
        if "watch" in URL:
            video_list.append(YouTube(URL))
        elif "playlist" in URL:
            video_list.extend(Playlist(URL).videos)
    if video_number_start == None:
        video_number_start = 1
    if video_number_end == None:
        video_number_end = len(video_list)
    for video_number in range(video_number_start - 1, video_number_end):
        video = video_list[video_number]
        download_video(video, file_extension, file_resolution, video_number + 1, video_number_digits)


def download_video(video: YouTube, 
                   file_extension: str, 
                   file_resolution: str, 
                   video_number: int = 1, 
                   video_number_digits: int = 2) -> None:
    file_name_prefix = str(video_number).zfill(video_number_digits) + '-'
    file_name = file_name_prefix + video.title
    filtered_streams = video.streams.filter(progressive = True, file_extension = file_extension).order_by('resolution').desc()
    if len(filtered_streams) >= 1:
        print('Available streams are:')
        for stream in filtered_streams:
            print(stream)
        all_resolutions = ['144p', '240p', '360p', '480p', '720p', '1080p']
        resolution_index = all_resolutions.index(file_resolution)
        while True:
            print(f'Downloading \'{file_name}\' with {file_resolution} resolution.')
            try:
                filtered_streams.get_by_resolution(file_resolution).download(filename_prefix = file_name_prefix, max_retries = 3)
                break
            except (IncompleteRead, AttributeError):
                resolution_index = resolution_index - 1
                if resolution_index == -1:
                    raise
                file_resolution = all_resolutions[resolution_index]
                print(f'***Error*** - \'{file_name}\'' + '\n' + f'could not be downloaded. Resolution was downgraded to {file_resolution}.')
    else:
        print(f'Filtered results for \'{file_name}\' streams matched no cases.')