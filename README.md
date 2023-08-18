# YouTube Downloader

This is a simple python script that uses the `pytube` package to download vidoes from YouTube.

# Requirements

- `Python` 3.8 or later will work.
- You need the *latest* version of `pytube`. Since YouTube changes some internal settings from time to time, `pytube` should be modified accordingly to enable downloads from YouTube. If the lastest version does not work, you have several options to fix this.
    - Wait for a `pytube` update that fixes the issue. However, `pytube` is not updated quickly, so you should probably try other options.
    - Check the [issues][2] tab on `pytube` repository for a possible fix.
    - Install a recent [fork][3] of `pytube` that works.
    - Check [stackoverflow][1] website for a possible fix.
- `ffmpeg` is required for merging audio and video files. Usually, the highest quality media like `1080p` has separate audio and video files. In such cases, `ffmpeg` is required for merging the files after download. See the [official website][4] for installing it.

[1]: https://stackoverflow.com/
[2]: https://github.com/pytube/pytube/issues
[3]: https://github.com/pytube/pytube/forks
[4]: https://www.ffmpeg.org/download.html

# Quick Start

All you need is to make a list of video and playlist URLs you want to download and pass it to the `download_playlist` function.

```py
videos_urls = ['https://www.youtube.com/watch?v=-G1FuEQqxVI']
download_playlist(videos_urls, 'mp4', '720p')
```


Put this code snippet into `examples.py` and run

```bash
python examples.py
```

There are also other examples in `examples.py`.