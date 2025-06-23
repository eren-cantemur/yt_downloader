### 🛠 1. Install Dependencies

```bash
pip install pytubefix
```

To extract audio as `.mp3`, we also need `ffmpeg`:

* **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/) and add it to your PATH.
* **macOS**: `brew install ffmpeg`
* **Linux**: `sudo apt install ffmpeg`


### ▶️ Example Usage

```bash
python yt_downloader.py https://www.youtube.com/watch?v=dQw4w9WgXcQ mp3
```

```bash
python yt_downloader.py https://www.youtube.com/watch?v=dQw4w9WgXcQ mp4
```

Let me know if you want to make it fancier (e.g. progress bar, interactive prompt, saving in a folder, etc.)
