from pytube import YouTube

def download_youtube_video(url, save_path='.'):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()

        # Download the video
        print(f"Downloading {yt.title}...")
        stream.download(save_path)
        print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # URL of the YouTube video
    url = input("Enter the YouTube video URL: ")

    # Path where the video will be saved
    save_path = input("Enter the save path "
                      "(default is current directory): ") \
                or '.'

    # Call the function to download the video
    download_youtube_video(url, save_path)
