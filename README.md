# YouTube Downloader

This is a simple python script that uses the `pytube` package to download videos from YouTube.


# Requirements

- `Python` *3.8* or later will work.
- You need the *latest* version of `pytube`. Since YouTube changes some internal settings from time to time, `pytube` should be modified accordingly to enable downloads from YouTube. If the lastest version does not work, you have several options to fix this.
    - Wait for a `pytube` update that fixes the issue. However, `pytube` is not updated quickly, so you should probably try other options.
    - Check the [issues][2] tab on `pytube` repository for a possible fix.
    - Install a recent [fork][3] of `pytube` that works.
    - Check [stackoverflow][1] website for a possible fix.
- `ffmpeg` *6.0* or later is required for merging audio and video files. Usually, the highest quality media like `1080p` has separate audio and video files. In such cases, `ffmpeg` is required for merging the files after download. See the [official website][4] for installing it.


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


# Using Tor as Proxy

If YouTube is not accesible from your region due to censorship, you can reliably use Tor to circuvment this issue. Follow the instructions in [here][5] for installing Tor. Then, run Tor as below

```bash
tor -HTTPTunnelPort 8118
```
which creates an HTTP proxy for you. If Tor could not connect then you can configure [obs4][6] or [snowflake][7] bridges with Tor which can hopefully resolve this issue. After making sure that Tor has connected, while keeping this terminal open, use another terminal and run your python program in it

```bash
export https_proxy=https://127.0.0.1:8118
python exmaples.py
```

which will pass all the traffic of the python program through the HTTP proxy created by Tor.


[1]: https://stackoverflow.com/
[2]: https://github.com/pytube/pytube/issues
[3]: https://github.com/pytube/pytube/forks
[4]: https://www.ffmpeg.org/download.html
[5]: https://community.torproject.org/onion-services/setup/install/
[6]: https://community.torproject.org/relay/setup/bridge/debian-ubuntu/
[7]: https://askubuntu.com/a/1406572/1557464