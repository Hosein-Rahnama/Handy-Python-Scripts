# YouTube Downloader

This is a simple python script that uses the `pytube` package to download vidoes from YouTube.

# Requirements

- `Python 3.8` or later will work.
- You need the **latest** version of `pytube`. Since YouTube changes some internal settings from time to time, `pytube` should be modified accordingly to enable downloads from YouTube. If the lastest version does not work, check [stackoverflow][1] website or the [issues][2] tab on `pytube` repository for temporary and quick fixes.
- `ffmpeg` is required for merging audio and video files. Usually, the highest quality media like `1080p` has separate audio and video files. In such cases, `ffmpeg` is required for merging the files after download.

[1]: https://stackoverflow.com/
[2]: https://github.com/pytube/pytube/issues

# TODO

- [ ] Add a function for downloading subtitles.
- [ ] Add a function for converting Persian file names to Finglish.
- [ ] Beautify messages in the CMD.
- [ ] Create a GUI.
