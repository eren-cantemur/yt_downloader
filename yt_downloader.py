import sys
from pytubefix import YouTube
from pytubefix.cli import on_progress
import os

def download_video(url, as_audio=False):
    try:
        # Create downloads directory if it doesn't exist
        downloads_dir = "downloads"
        if not os.path.exists(downloads_dir):
            os.makedirs(downloads_dir)
        
        print(f"[⏳] Fetching video info from: {url}")
        yt = YouTube(url, on_progress_callback=on_progress)
        print(f"[📹] Title: {yt.title}")
        print(f"[⏱️] Duration: {yt.length // 60}:{yt.length % 60:02d}")
        
        if as_audio:
            print("[🎵] Downloading audio...")
            stream = yt.streams.filter(only_audio=True).first()
            if not stream:
                print("[❌] No audio stream available")
                return
            out_file = stream.download(output_path=downloads_dir)
            if out_file:
                base, ext = os.path.splitext(out_file)
                mp3_file = base + '.mp3'
                os.rename(out_file, mp3_file)
                print(f"[✔] Downloaded audio: {mp3_file}")
            else:
                print("[❌] Failed to download audio file")
        else:
            print("[🎥] Downloading video...")
            stream = yt.streams.get_highest_resolution()
            if not stream:
                print("[❌] No video stream available")
                return
            video_file = stream.download(output_path=downloads_dir)
            print(f"[✔] Downloaded video: {video_file}")
            
    except Exception as e:
        print(f"[❌] Error: {str(e)}")
        print("[💡] Try using a different URL or check your internet connection")

def main():
    if len(sys.argv) < 3:
        print("Usage: python yt_downloader.py <youtube_url> <mp3|mp4>")
        print("Example: python yt_downloader.py 'https://www.youtube.com/watch?v=dQw4w9WgXcQ' mp3")
        return
    
    url = sys.argv[1]
    format_type = sys.argv[2].lower()
    
    if format_type == "mp3":
        download_video(url, as_audio=True)
    elif format_type == "mp4":
        download_video(url, as_audio=False)
    else:
        print("Invalid format. Use 'mp3' or 'mp4'.")

if __name__ == "__main__":
    main()
