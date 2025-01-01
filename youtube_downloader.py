import yt_dlp
import os

def download_video(link, quality):
    try:
        # Unapred definisana putanja za preuzimanje
        download_path = "C:\\Users\\emirg\\Desktop\\youtube videos downloaded"

        # Proveri da li folder postoji, ako ne postoji, kreiraj ga
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        # Opcije za preuzimanje sa izborom kvaliteta
        ydl_opts = {
            'format': f'bestvideo[height<={quality}]+bestaudio/best',  # Odabir kvaliteta
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  # Ime fajla u specificiranom folderu
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print(f"Download complete! Saved to: {download_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("YouTube Video Downloader")
    link = input("Enter the YouTube video link: ")
    print("Enter the video quality you want (e.g., 1080, 720, 480): ")
    quality = input("Quality: ")
    download_video(link, quality)

if __name__ == "__main__":
    main()
