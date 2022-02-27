from pytube import YouTube, Playlist
from http.client import IncompleteRead
from typing import List, Optional, Union


def download_playlist(playlist: Union[Playlist, List[str]], 
                      file_extension: str, 
                      file_resolution: str, 
                      video_number_start: Optional[int] = None, 
                      video_number_end: Optional[int] = None, 
                      video_number_digits: int = 2) -> None:
    if type(playlist) == Playlist:
        video_list = playlist.videos
    elif type(playlist) == list:
        video_list = [YouTube(video) for video in playlist]
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
    file_name_prefix = str(video_number).zfill(video_number_digits) + ' - '
    file_name = file_name_prefix + video.title
    filtered_streams = video.streams.filter(progressive = True, file_extension = file_extension).order_by('resolution').desc()
    print('Available streams are as follows:')
    for stream in filtered_streams:
        print(stream)
    if len(filtered_streams) >= 1:
        for resoution in range(0, 6):
            print(f'Downloading \'{file_name}\' with {file_resolution} resolution.')
            try:
                filtered_streams.get_by_resolution(file_resolution).download(filename_prefix = file_name_prefix, max_retries = 1)
                break
            except (IncompleteRead, AttributeError):
                file_resolution = downgrade_resolution(file_resolution)
                if file_resolution == '':
                    raise
                print(f'***Error*** - \'{file_name}\'' + '\n' + f'could not be downloaded. Resolution was downgraded to {file_resolution}.')
    else:
        print(f'Filter results for \'{file_name}\' streams matched no cases.')


def downgrade_resolution(file_resolution: str) -> str:
    all_resolutions = ['144p', '240p', '360p', '480p', '720p', '1080p']
    if file_resolution == '144p':
        return ''
    for resolution in range(0, len(all_resolutions)):
        if file_resolution == all_resolutions[resolution]:
            return all_resolutions[resolution - 1]
