import subprocess

def get_video_info(url):
    result = subprocess.run(
        ['yt-dlp', '-F', url],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    if result.returncode != 0:
        print("Error fetching video information:", result.stderr)
        return None
    return result.stdout

def download_video(url, video_format=None, audio_format=None):
    # If only video format is provided (no audio)
    if audio_format is None and video_format is not None:
        command = ['yt-dlp', '-f', video_format, '-N 8', url]
    # If only audio format is provided
    elif video_format is None and audio_format is not None:
        command = ['yt-dlp', '-f', audio_format, '-N 8', url]
    # If both video and audio formats are provided
    else:
        command = ['yt-dlp', '-f', f"{video_format}+{audio_format}", '-N 8', url]

    subprocess.run(command)

def main():
    url = input("Please paste the YouTube video link: ")

    # Get video information
    video_info = get_video_info(url)
    if video_info is None:
        return
    
    # Display available formats
    print("\nAvailable Formats:")
    print(video_info)
    
    # Ask if the user wants to download audio, video, or both
    choice = input("Do you want to download: \n1. Video only\n2. Audio only\n3. Both video and audio\nEnter your choice (1/2/3): ").strip()

    if choice == "1":
        # Download video only
        video_format = input("Enter the format code for the video: ")
        download_video(url, video_format=video_format)
    elif choice == "2":
        # Download audio only
        audio_format = input("Enter the format code for the audio: ")
        download_video(url, audio_format=audio_format)
    elif choice == "3":
        # Download both video and audio
        video_format = input("Enter the format code for the video: ")
        audio_format = input("Enter the format code for the audio: ")
        download_video(url, video_format=video_format, audio_format=audio_format)
    else:
        print("Invalid choice. Exiting.")

    print("Download started!")

if __name__ == "__main__":
    main()
