import instaloader
def download_instagram_content():
    loader = instaloader.Instaloader()
    instagram_username = input("Enter the Instagram username: ")
    try:
        loader.download_profile(instagram_username, profile_pic_only=True)
        print("Profile picture downloaded successfully!")
    except Exception as e:
        print("Error downloading profile picture:", str(e))

download_instagram_content()