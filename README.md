# YouTube Downloader

This is a simple python script that uses the `pytube` package to download vidoes from YouTube.

# Requirements

- `Python 3.8` or later.
- `Pytube 12.1` or later.
- `ffmpeg` for merging audio and video files.

# TODO

- [x] Change `download_playlist` such that it only takes URLs as input.
- [x] Improve `download_video` such that it can download highest quality videos with DASH format.
- [ ] Write a function for creating proper file names that handles allowed characters and numbering in the video title.
- [ ] Add a feature for downloading subtitles.
- [ ] Create a GUI.
