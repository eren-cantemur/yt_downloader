### 🛠 1. Install Dependencies

```bash
pip install pytubefix
```

To extract audio as `.mp3`, we also need `ffmpeg`:

* **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/) and add it to your PATH.
* **macOS**: `brew install ffmpeg`
* **Linux**: `sudo apt install ffmpeg`


### ▶️ Example Usage

**Single video download:**
```bash
python yt_downloader.py https://www.youtube.com/watch?v=dQw4w9WgXcQ mp3
```

```bash
python yt_downloader.py https://www.youtube.com/watch?v=dQw4w9WgXcQ mp4
```

**Multiple videos download:**
```bash
python yt_downloader.py "url1" "url2" "url3" mp3
```

**Batch download from file:**
```bash
python yt_downloader.py --file example_urls.txt mp3
```

### 📝 Features

- ✅ Single video download (mp3/mp4)
- ✅ Multiple videos download
- ✅ Batch download from URLs file
- ✅ Progress tracking with download stats
- ✅ Files saved to `downloads/` folder
- ✅ Error handling and recovery
- ✅ Comments support in URLs file (lines starting with #)
