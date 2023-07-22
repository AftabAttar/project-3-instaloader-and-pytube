from pytube import YouTube

def download_youtube_video():
    youtube_url = input("Enter the YouTube video URL: ")
    try:
        yt = YouTube(youtube_url)

        video_stream = yt.streams.get_highest_resolution()

        video_stream.download()
        print("Video downloaded successfully!")
    except Exception as e:
        print("Error downloading the video:", str(e))


download_youtube_video()