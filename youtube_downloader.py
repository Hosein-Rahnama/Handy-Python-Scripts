import os
import subprocess
from typing import List, Optional
from pytube import YouTube, Playlist, StreamQuery
from settings import CWD, DOWNLOAD_PATH, MAX_RETRIES, DIGITS, BYTE_TO_MB


def download_playlist(videos_URLs: List[str],
                      file_extension: str, 
                      file_resolution: str, 
                      video_number_start: Optional[int] = None,
                      video_number_end: Optional[int] = None,
                      video_number_digits: int = DIGITS) -> None:
    video_list = []
    for URL in videos_URLs:
        if ("watch" in URL):
            video_list.append(YouTube(URL))
        elif ("playlist" in URL):
            video_list.extend(Playlist(URL).videos)
    if (video_number_start == None):
        video_number_start = 1
    if (video_number_end == None):
        video_number_end = len(video_list)
    for video_number in range(video_number_start - 1, video_number_end):
        video = video_list[video_number]
        download_video(video, file_extension, file_resolution, video_number + 1, video_number_digits)


def download_video(video: YouTube, 
                   file_extension: str,
                   file_resolution: str,
                   video_number: int = 1,
                   video_number_digits: int = DIGITS) -> None:
    file_name_prefix = str(video_number).zfill(video_number_digits) + '-'
    file_name = video.title.replace(':', '').replace('?', '').replace(' ', '-')
    filtered_streams_progressive = video.streams.filter(progressive = True)
    filtered_streams_adaptive = video.streams.filter(adaptive = True)
    all_resolutions = ['144p', '240p', '360p', '480p', '720p', '1080p']
    resolution_index = all_resolutions.index(file_resolution)
    while (resolution_index >= 0):
        downloaded = download_stream_progressive(filtered_streams_progressive, file_extension, file_resolution, file_name, file_name_prefix)
        if downloaded:
            return
        downloaded = download_stream_adaptive(filtered_streams_adaptive, file_extension, file_resolution, file_name, file_name_prefix)
        if downloaded:
            return
        resolution_index = resolution_index - 1
        file_resolution = all_resolutions[resolution_index]
        print(f'**Error** - \'{file_name}\'' + '\n' + f'Requested resolution was not available. Resolution was downgraded to {file_resolution}.')
    print(f'**Error** - \'{file_name}\'' + '\n' + f'File was not downloaded.')
    return


def download_stream_progressive(streams_progressive: StreamQuery,
                                file_extension: str,
                                file_resolution: str,
                                file_name: str,
                                file_name_prefix: str,
                                max_retries: int = MAX_RETRIES) -> bool:
    stream = streams_progressive.filter(res = file_resolution, file_extension = file_extension).first()
    if (stream != None):
        video_size = round(stream.filesize * BYTE_TO_MB, 2)
        video_name = file_name_prefix + file_name + '.' + file_extension
        print(f"Downloading '{file_name}' with {file_resolution} resolution. Media size is {video_size} MB.")
        stream.download(output_path = DOWNLOAD_PATH, filename = video_name, max_retries = max_retries)
        return True
    else:
        return False


def download_stream_adaptive(streams_adaptive: StreamQuery,
                             file_extension: str,
                             file_resolution: str,
                             file_name: str,
                             file_name_prefix: str,
                             max_retries: int = MAX_RETRIES) -> bool:
    stream_video = streams_adaptive.filter(res = file_resolution, file_extension = file_extension).first()
    stream_audio = streams_adaptive.filter(only_audio = True).order_by('abr').desc().first()
    if (stream_video != None):
        video_size = round(stream_video.filesize * BYTE_TO_MB, 2)
        video_name = file_name_prefix + 'video-' + file_name + '.' + file_extension
        print(f"Downloading video of '{file_name}' with {file_resolution} resolution. Video size is {video_size} MB.")
        stream_video.download(output_path = DOWNLOAD_PATH, filename = video_name , max_retries = max_retries)
        audio_size = round(stream_audio.filesize * BYTE_TO_MB, 2)
        audio_extension = stream_audio.mime_type.split('/')[1]
        audio_name = file_name_prefix + 'audio-' + file_name + '.' + audio_extension
        print(f"Downloading audio of '{file_name}' with {stream_audio.abr} average bitrate. Audio size is {audio_size} MB.")
        stream_audio.download(output_path = DOWNLOAD_PATH, filename = audio_name, max_retries = max_retries)
        output_name = file_name_prefix + file_name + '.' + file_extension
        print('Merging video and audio.')
        merge_audio_vdieo(video_name, audio_name, output_name)
        return True
    else:
        return False


def merge_audio_vdieo(video_name: str,
                      audio_name: str,
                      output_name: str) -> None:
    os.chdir(DOWNLOAD_PATH)
    subprocess.run(['ffmpeg',
                    '-v', 'quiet',
                    '-i', f'{video_name}',
                    '-i', f'{audio_name}',
                    '-c:', 'copy',
                    '-map', '0:v',
                    '-map', '1:a',
                    f'{output_name}'])
    os.remove(os.path.join(DOWNLOAD_PATH, video_name))
    os.remove(os.path.join(DOWNLOAD_PATH, audio_name))
    os.chdir(CWD)