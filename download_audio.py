import yt_dlp
import os

def download_audio(link, download_path):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print(f"Downloaded: {link}")
    except Exception as e:
        print(f"An error occurred with {link}: {e}")

def main():
    download_path = r"C:\Users\emirg\Desktop\youtube music downloaded"

    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # Ispravna putanja do fajla
    file_path = r"C:\Users\emirg\Desktop\lista pjesama\lista_youtube_videa.txt"

    try:
        with open(file_path, 'r') as file:
            links = file.readlines()

        for link in links:
            link = link.strip()
            if link:
                download_audio(link, download_path)

        print(f"All downloads complete! Files saved to: {download_path}")

    except FileNotFoundError:
        print("The specified file was not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
