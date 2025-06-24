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

def read_urls_from_file(file_path):
    """Read URLs from a text file, one URL per line."""
    urls = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):  # Skip empty lines and comments
                    urls.append(line)
        return urls
    except FileNotFoundError:
        print(f"[❌] File not found: {file_path}")
        return []
    except Exception as e:
        print(f"[❌] Error reading file: {str(e)}")
        return []

def download_multiple_videos(urls, as_audio=False):
    """Download multiple videos from a list of URLs."""
    total = len(urls)
    successful = 0
    failed = 0
    
    print(f"[📋] Starting download of {total} video(s)...")
    print("-" * 50)
    
    for i, url in enumerate(urls, 1):
        print(f"\n[{i}/{total}] Processing: {url}")
        try:
            download_video(url, as_audio)
            successful += 1
        except Exception as e:
            print(f"[❌] Failed to download {url}: {str(e)}")
            failed += 1
        
        if i < total:
            print("-" * 50)
    
    print(f"\n[📊] Download Summary:")
    print(f"   ✅ Successful: {successful}")
    print(f"   ❌ Failed: {failed}")
    print(f"   📁 Files saved to: downloads/")

def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  Single video: python yt_downloader.py <youtube_url> <mp3|mp4>")
        print("  Multiple videos: python yt_downloader.py <url1> <url2> <url3> ... <mp3|mp4>")
        print("  From file: python yt_downloader.py --file <file_path> <mp3|mp4>")
        print("\nExamples:")
        print("  python yt_downloader.py 'https://www.youtube.com/watch?v=dQw4w9WgXcQ' mp3")
        print("  python yt_downloader.py 'url1' 'url2' 'url3' mp4")
        print("  python yt_downloader.py --file urls.txt mp3")
        return
    
    format_type = sys.argv[-1].lower()  # Last argument is always the format
    
    if format_type not in ["mp3", "mp4"]:
        print("Invalid format. Use 'mp3' or 'mp4'.")
        return
    
    as_audio = format_type == "mp3"
    
    # Check if using file input
    if len(sys.argv) >= 4 and sys.argv[1] == "--file":
        file_path = sys.argv[2]
        urls = read_urls_from_file(file_path)
        if urls:
            download_multiple_videos(urls, as_audio)
        else:
            print("[❌] No valid URLs found in file.")
    
    # Check if multiple URLs provided
    elif len(sys.argv) > 3:
        urls = sys.argv[1:-1]  # All arguments except the last one (format)
        download_multiple_videos(urls, as_audio)
    
    # Single URL
    else:
        url = sys.argv[1]
        download_video(url, as_audio)

if __name__ == "__main__":
    main()
